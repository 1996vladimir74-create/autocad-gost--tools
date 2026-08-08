from autocad.geometry import Geometry
from autocad.text import TextManager


class TitleBlock:

    WIDTH = 185.0
    HEIGHT = 55.0

    def __init__(self, space):

        self.geometry = Geometry(
            space
        )

        self.text = TextManager(
            space
        )

    def create(
        self,
        drawing,
        sheet_width,
        sheet_height
    ):

        # Основная надпись располагается
        # в правом нижнем углу рамки.

        x0 = (
            float(sheet_width)
            - 5.0
            - self.WIDTH
        )

        y0 = 5.0

        self._draw_outer(
            x0,
            y0
        )

        self._draw_grid(
            x0,
            y0
        )

        self._draw_text(
            drawing,
            x0,
            y0
        )

    def _draw_outer(
        self,
        x0,
        y0
    ):

        self.geometry.rectangle(
            x0,
            y0,
            self.WIDTH,
            self.HEIGHT,
            "TITLE_BLOCK"
        )

    def _draw_grid(
        self,
        x0,
        y0
    ):
        """
        Внутренняя сетка формы 1.

        Геометрия вынесена в отдельный метод,
        чтобы её можно было точно корректировать
        без изменения остальной программы.
        """

        # Горизонтальные уровни.
        #
        # 55 мм общей высоты.
        #
        # Нижний ряд: 7
        # Следующий: 10
        # Следующий: 15
        # Верхний: 23

        rows = [
            7.0,
            17.0,
            32.0
        ]

        for row in rows:

            self.geometry.line(
                x0,
                y0 + row,
                x0 + self.WIDTH,
                y0 + row,
                "TITLE_BLOCK"
            )

        # Основные вертикальные разделители.

        verticals = [
            70.0,
            105.0,
            125.0,
            145.0,
            165.0
        ]

        for value in verticals:

            self.geometry.line(
                x0 + value,
                y0,
                x0 + value,
                y0 + self.HEIGHT,
                "TITLE_BLOCK"
            )

    def _draw_text(
        self,
        drawing,
        x0,
        y0
    ):
        """
        Текст размещается внутри отдельных ячеек,
        с отступом от линий.
        """

        padding = 2.0

        # Наименование

        self.text.add_mtext(
            drawing.name,
            x0 + padding,
            y0 + 49.0,
            66.0,
            5.0,
            "TEXT"
        )

        # Обозначение

        self.text.add_mtext(
            drawing.number,
            x0 + 72.0,
            y0 + 49.0,
            31.0,
            3.5,
            "TEXT"
        )

        # Разработал

        self.text.add_text(
            "Разраб.",
            x0 + padding,
            y0 + 35.0,
            3.5,
            "TEXT"
        )

        self.text.add_text(
            drawing.designer,
            x0 + padding,
            y0 + 27.0,
            3.5,
            "TEXT"
        )

        # Проверил

        self.text.add_text(
            "Пров.",
            x0 + 72.0,
            y0 + 35.0,
            3.5,
            "TEXT"
        )

        self.text.add_text(
            drawing.checker,
            x0 + 72.0,
            y0 + 27.0,
            3.5,
            "TEXT"
        )

        # Масштаб

        self.text.add_text(
            "Масштаб",
            x0 + 127.0,
            y0 + 35.0,
            3.0,
            "TEXT"
        )

        self.text.add_text(
            drawing.scale,
            x0 + 127.0,
            y0 + 27.0,
            3.5,
            "TEXT"
        )

        # Организация

        self.text.add_mtext(
            drawing.organization,
            x0 + 2.0,
            y0 + 13.0,
            101.0,
            3.5,
            "TEXT"
        )

        # Лист

        self.text.add_text(
            "Лист",
            x0 + 147.0,
            y0 + 13.0,
            3.0,
            "TEXT"
        )

        self.text.add_text(
            "1",
            x0 + 147.0,
            y0 + 5.0,
            3.5,
            "TEXT"
        )

        # Листов

        self.text.add_text(
            "Листов",
            x0 + 167.0,
            y0 + 13.0,
            3.0,
            "TEXT"
        )

        self.text.add_text(
            "1",
            x0 + 167.0,
            y0 + 5.0,
            3.5,
            "TEXT"
        )
