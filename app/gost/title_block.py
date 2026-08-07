from autocad.geometry import Geometry
from autocad.text import TextManager


class TitleBlock:


    def __init__(self, document):

        self.geometry = Geometry(
            document
        )

        self.text = TextManager(
            document
        )



    def create(
        self,
        drawing,
        sheet_width,
        sheet_height
    ):


        width = 185
        height = 55


        x0 = (
            sheet_width - 5 - width
        )

        y0 = 5


        # границы основной надписи

        self.geometry.line(
            x0,
            y0,
            x0 + width,
            y0,
            "TITLE_BLOCK"
        )


        self.geometry.line(
            x0 + width,
            y0,
            x0 + width,
            y0 + height,
            "TITLE_BLOCK"
        )


        self.geometry.line(
            x0 + width,
            y0 + height,
            x0,
            y0 + height,
            "TITLE_BLOCK"
        )


        self.geometry.line(
            x0,
            y0 + height,
            x0,
            y0,
            "TITLE_BLOCK"
        )


        # текстовые поля


        self.text.add_text(
            drawing.number,
            x0 + 10,
            y0 + 40,
            5
        )


        self.text.add_text(
            drawing.name,
            x0 + 10,
            y0 + 30,
            5
        )


        self.text.add_text(
            "Разработал: "
            + drawing.designer,

            x0 + 10,
            y0 + 20,
            3.5
        )


        self.text.add_text(
            "Проверил: "
            + drawing.checker,

            x0 + 10,
            y0 + 10,
            3.5
        )
