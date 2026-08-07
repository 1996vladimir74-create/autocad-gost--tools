import tkinter as tk
from tkinter import ttk, messagebox

from models.drawing import Drawing


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


        self.logger.info(
            f"Создан запрос: {drawing}"
        )


        messagebox.showinfo(
            "Готово",
            "Данные чертежа приняты.\n"
            "Ожидание AutoCAD Engine."
        )


    def run(self):

        self.root.mainloop()