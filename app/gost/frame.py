from autocad.geometry import Geometry
from gost.formats import get_sheet_size
from gost.standards import GOST_FRAME


class GostFrame:


    def __init__(self, document):

        self.geometry = Geometry(
            document
        )


    def create(
        self,
        sheet_format,
        orientation
    ):

        size = get_sheet_size(
            sheet_format,
            orientation
        )


        width = size["width"]
        height = size["height"]


        left = GOST_FRAME["left_margin"]
        right = GOST_FRAME["right_margin"]
        top = GOST_FRAME["top_margin"]
        bottom = GOST_FRAME["bottom_margin"]


        x1 = left
        y1 = bottom

        x2 = width - right
        y2 = height - top


        # нижняя линия

        self.geometry.line(
            x1,
            y1,
            x2,
            y1,
            "FRAME"
        )


        # правая линия

        self.geometry.line(
            x2,
            y1,
            x2,
            y2,
            "FRAME"
        )


        # верхняя линия

        self.geometry.line(
            x2,
            y2,
            x1,
            y2,
            "FRAME"
        )


        # левая линия

        self.geometry.line(
            x1,
            y2,
            x1,
            y1,
            "FRAME"
        )


        return {
            "width": width,
            "height": height
        }
