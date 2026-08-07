import logging


class TextManager:


    def __init__(self, document):

        self.space = (
            document.ModelSpace
        )

        self.logger = logging.getLogger(
            "AutoCAD_GOST_Tools"
        )



    def add_text(
        self,
        text,
        x,
        y,
        height=5
    ):

        point = (
            x,
            y,
            0
        )


        entity = (
            self.space.AddText(
                text,
                point,
                height
            )
        )


        return entity