import tkinter as tk
from tkinter import ttk, messagebox

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

    from autocad.connection import AutoCADConnection
    from autocad.layers import LayerManager
    from gost.frame import GostFrame
    from gost.title_block import TitleBlock


    drawing = Drawing(

        number=self.number_entry.get(),

        name=self.name_entry.get(),

        sheet_format=self.format_box.get(),

        orientation=self.orientation_box.get()

    )


    errors = drawing.validate()


    if errors:

        messagebox.showerror(
            "Ошибка",
            "\n".join(errors)
        )

        self.logger.warning(
            str(errors)
        )

        return


    try:

        self.logger.info(
            "Запуск создания чертежа"
        )


        # подключение AutoCAD

        connection = AutoCADConnection()

        acad = connection.connect()


        document = connection.get_document()



        # создание слоев

        layers = LayerManager(
            document
        )

        layers.create_default_layers()



        # рамка

        frame = GostFrame(
            document
        )


        sheet = frame.create(

            drawing.sheet_format,

            drawing.orientation

        )



        # основная надпись

        title = TitleBlock(
            document
        )


        title.create(

            drawing,

            sheet["width"],

            sheet["height"]

        )



        self.logger.info(
            "Чертеж успешно создан"
        )


        messagebox.showinfo(

            "Готово",

            "Чертеж создан в AutoCAD"

        )


    except Exception as error:


        self.logger.error(
            str(error)
        )


        messagebox.showerror(

            "Ошибка",

            str(error)

        )

    def run(self):

        self.root.mainloop()
