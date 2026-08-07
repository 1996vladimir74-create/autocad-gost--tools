import logging


class Geometry:


    def __init__(self, document):

        self.document = document

        self.space = (
            document.ModelSpace
        )

        self.logger = logging.getLogger(
            "AutoCAD_GOST_Tools"
        )



    def line(
        self,
        x1,
        y1,
        x2,
        y2
    ):

        start = (
            x1,
            y1,
            0
        )

        end = (
            x2,
            y2,
            0
        )


        self.space.AddLine(
            start,
            end
        )


    def rectangle(
        self,
        width,
        height
    ):

        self.line(
            0,
            0,
            width,
            0
        )

        self.line(
            width,
            0,
            width,
            height
        )

        self.line(
            width,
            height,
            0,
            height
        )

        self.line(
            0,
            height,
            0,
            0
        )