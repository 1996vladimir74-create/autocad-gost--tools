from autocad.geometry import Geometry
from gost.formats import get_sheet_size
from gost.standards import GOST_FRAME


class GostFrame:

    def __init__(self, space):

        self.geometry = Geometry(
            space
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

        width = float(
            size["width"]
        )

        height = float(
            size["height"]
        )

        left = float(
            GOST_FRAME["left_margin"]
        )

        right = float(
            GOST_FRAME["right_margin"]
        )

        top = float(
            GOST_FRAME["top_margin"]
        )

        bottom = float(
            GOST_FRAME["bottom_margin"]
        )

        frame_width = (
            width - left - right
        )

        frame_height = (
            height - top - bottom
        )

        self.geometry.rectangle(
            left,
            bottom,
            frame_width,
            frame_height,
            "FRAME"
        )

        return {
            "width": width,
            "height": height,
            "frame_x": left,
            "frame_y": bottom,
            "frame_width": frame_width,
            "frame_height": frame_height
        }
