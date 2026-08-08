from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

from models.drawing import Drawing

from autocad.connection import AutoCADConnection
from autocad.document import AutoCADDocument
from autocad.layers import LayerManager
from autocad.setup import AutoCADSetup

from gost.frame import GostFrame
from gost.title_block import TitleBlock
class MainWindow:

    def __init__(self, logger):

        self.logger = logger

        self.root = tk.Tk()

        self.root.title(
            "AutoCAD GOST Tools v1.0"
        )

        self.root.geometry(
            "450x350"
        )

        self.create_widgets()


    def create_widgets(self):

        frame = ttk.Frame(
            self.root,
            padding=20
        )

        frame.pack(
            fill="both",
            expand=True
        )


        ttk.Label(
            frame,
            text="Номер чертежа:"
        ).pack(anchor="w")


        self.number_entry = ttk.Entry(
            frame
        )

        self.number_entry.pack(
            fill="x"
        )


        ttk.Label(
            frame,
            text="Наименование:"
        ).pack(anchor="w",
               pady=(10,0))


        self.name_entry = ttk.Entry(
            frame
        )

        self.name_entry.pack(
            fill="x"
        )


        ttk.Label(
            frame,
            text="Формат:"
        ).pack(anchor="w",
               pady=(10,0))


        self.format_box = ttk.Combobox(
            frame,
            values=[
                "A4",
                "A3",
                "A2",
                "A1",
                "A0"
            ]
        )

        self.format_box.current(1)

        self.format_box.pack(
            fill="x"
        )


        ttk.Label(
            frame,
            text="Ориентация:"
        ).pack(anchor="w",
               pady=(10,0))


        self.orientation_box = ttk.Combobox(
            frame,
            values=[
                "Альбомная",
                "Книжная"
            ]
        )

        self.orientation_box.current(0)

        self.orientation_box.pack(
            fill="x"
        )


        create_button = ttk.Button(
            frame,
            text="Создать чертеж",
            command=self.create_drawing
        )

        create_button.pack(
            pady=20
        )


   def create_drawing(self):

    drawing = Drawing(

        number=self.number_entry.get().strip(),

        name=self.name_entry.get().strip(),

        sheet_format=self.format_box.get(),

        orientation=self.orientation_box.get(),

        scale="1:1"

    )

    errors = drawing.validate()

    if errors:

        messagebox.showerror(
            "Ошибка",
            "\n".join(errors)
        )

        self.logger.warning(
            "Ошибка проверки: %s",
            errors
        )

        return

    try:

        self.logger.info(
            "Начало создания чертежа: %s",
            drawing
        )

        # --------------------------------
        # 1. AutoCAD
        # --------------------------------

        connection = AutoCADConnection()

        acad = connection.connect()

        # --------------------------------
        # 2. Новый DWG
        # --------------------------------

        raw_document = (
            connection.create_document()
        )

        document = AutoCADDocument(
            raw_document
        )

        document.set_units()

        # --------------------------------
        # 3. Layout
        # --------------------------------

        document.get_layout()

        paper_space = (
            document.get_paper_space()
        )

        # --------------------------------
        # 4. Подготовка AutoCAD
        # --------------------------------

        setup = AutoCADSetup(
            raw_document
        )

        setup.prepare()

        # --------------------------------
        # 5. Слои
        # --------------------------------

        layers = LayerManager(
            raw_document
        )

        layers.create_default_layers()

        # --------------------------------
        # 6. Рамка
        # --------------------------------

        frame = GostFrame(
            paper_space
        )

        sheet = frame.create(

            drawing.sheet_format,

            drawing.orientation

        )

        # --------------------------------
        # 7. Основная надпись
        # --------------------------------

        title_block = TitleBlock(
            paper_space
        )

        title_block.create(

            drawing,

            sheet["width"],

            sheet["height"]

        )

        # --------------------------------
        # 8. Обновление AutoCAD
        # --------------------------------

        raw_document.Regen(
            1
        )

        self.logger.info(
            "Чертеж успешно создан"
        )

        messagebox.showinfo(
            "AutoCAD GOST Tools",
            "Чертеж успешно создан в AutoCAD."
        )

    except Exception as error:

        self.logger.exception(
            "Ошибка создания чертежа"
        )

        messagebox.showerror(
            "Ошибка",
            (
                "Не удалось создать чертеж.\n\n"
                f"{error}"
            )
        )
    def run(self):

        self.root.mainloop()
