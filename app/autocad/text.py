class TextManager:

    def __init__(self, space):

        self.space = space

    def add_text(
        self,
        text,
        x,
        y,
        height=3.5,
        layer="TEXT"
    ):

        entity = self.space.AddText(
            str(text),
            (
                float(x),
                float(y),
                0.0
            ),
            float(height)
        )

        entity.Layer = layer

        return entity

    def add_mtext(
        self,
        text,
        x,
        y,
        width,
        height=3.5,
        layer="TEXT"
    ):
        """
        MText с ограниченной шириной.
        Используется для длинных наименований.
        """

        entity = self.space.AddMText(
            (
                float(x),
                float(y),
                0.0
            ),
            float(width),
            str(text)
        )

        entity.Height = float(height)

        entity.Layer = layer

        return entity
