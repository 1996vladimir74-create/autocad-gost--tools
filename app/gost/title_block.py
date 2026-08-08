from autocad.geometry import Geometry
from autocad.text import TextManager


class TitleBlock:

    WIDTH = 185.0
    HEIGHT = 55.0

    def __init__(self, space):

        self.geometry = Geometry(space)
        self.text = TextManager(space)

    def create(
        self,
        drawing,
        sheet_width,
        sheet_height
    ):

        # Нижний правый угол рамки штампа.
        x0 = float(sheet_width) - 5.0 - self.WIDTH
        y0 = 5.0

        self._create_outer_frame(
            x0,
            y0
        )

        self._create_grid(
            x0,
            y0
        )

        self._create_text(
            drawing,
            x0,
            y0
        )

        return {
            "x": x0,
            "y": y0,
            "width": self.WIDTH,
            "height": self.HEIGHT
        }

    def _create_outer_frame(
        self,
        x0,
        y0
    ):

        self.geometry.line(
            x0,
            y0,
            x0 + self.WIDTH,
            y0,
            "TITLE_BLOCK"
        )

        self.geometry.line(
            x0 + self.WIDTH,
            y0,
            x0 + self.WIDTH,
            y0 + self.HEIGHT,
            "TITLE_BLOCK"
        )

        self.geometry.line(
            x0 + self.WIDTH,
            y0 + self.HEIGHT,
            x0,
            y0 + self.HEIGHT,
            "TITLE_BLOCK"
        )

        self.geometry.line(
            x0,
            y0 + self.HEIGHT,
            x0,
            y0,
            "TITLE_BLOCK"
        )

    def _create_grid(
        self,
        x0,
        y0
    ):
        """
        Внутренняя сетка штампа.

        На этом этапе задача —
        гарантированно получить полностью
        прорисованную сетку.
        """

        # Горизонтальные линии

        horizontal_lines = [
            7.0,
            17.0,
            32.0
        ]

        for offset in horizontal_lines:

            self.geometry.line(
                x0,
                y0 + offset,
                x0 + self.WIDTH,
                y0 + offset,
                "TITLE_BLOCK"
            )

        # Вертикальные линии

        vertical_lines = [
            70.0,
            105.0,
            125.0,
            145.0,
            165.0
        ]

        for offset in vertical_lines:

            self.geometry.line(
                x0 + offset,
                y0,
                x0 + offset,
                y0 + self.HEIGHT,
                "TITLE_BLOCK"
            )

    def _create_text(
        self,
        drawing,
        x0,
        y0
    ):

        # ----------------------------
        # Наименование
        # ----------------------------

        self.text.add_text(
            drawing.name,
            x0 + 2.0,
            y0 + 43.0,
            3.5,
            "TEXT"
        )

        # ----------------------------
        # Номер чертежа
        # ----------------------------

        self.text.add_text(
            drawing.number,
            x0 + 72.0,
            y0 + 43.0,
            3.5,
            "TEXT"
        )

        # ----------------------------
        # Разработал
        # ----------------------------

        self.text.add_text(
            "Разраб.",
            x0 + 2.0,
            y0 + 28.0,
            3.0,
            "TEXT"
        )

        self.text.add_text(
            drawing.designer or "",
            x0 + 2.0,
            y0 + 20.0,
            3.0,
            "TEXT"
        )

        # ----------------------------
        # Проверил
        # ----------------------------

        self.text.add_text(
            "Пров.",
            x0 + 72.0,
            y0 + 28.0,
            3.0,
            "TEXT"
        )

        self.text.add_text(
            drawing.checker or "",
            x0 + 72.0,
            y0 + 20.0,
            3.0,
            "TEXT"
        )

        # ----------------------------
        # Масштаб
        # ----------------------------

        self.text.add_text(
            "Масштаб",
            x0 + 127.0,
            y0 + 28.0,
            3.0,
            "TEXT"
        )

        self.text.add_text(
            drawing.scale,
            x0 + 127.0,
            y0 + 20.0,
            3.0,
            "TEXT"
        )

        # ----------------------------
        # Организация
        # ----------------------------

        self.text.add_text(
            drawing.organization or "",
            x0 + 2.0,
            y0 + 10.0,
            3.0,
            "TEXT"
        )

        # ----------------------------
        # Лист
        # ----------------------------

        self.text.add_text(
            "Лист",
            x0 + 147.0,
            y0 + 12.0,
            3.0,
            "TEXT"
        )

        self.text.add_text(
            "1",
            x0 + 149.0,
            y0 + 3.0,
            3.5,
            "TEXT"
        )

        # ----------------------------
        # Листов
        # ----------------------------

        self.text.add_text(
            "Листов",
            x0 + 167.0,
            y0 + 12.0,
            3.0,
            "TEXT"
        )

        self.text.add_text(
            "1",
            x0 + 169.0,
            y0 + 3.0,
            3.5,
            "TEXT"
        )
