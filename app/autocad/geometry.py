class Geometry:

    def __init__(self, space):

        self.space = space

    def line(
        self,
        x1,
        y1,
        x2,
        y2,
        layer=None
    ):

        entity = self.space.AddLine(
            (
                float(x1),
                float(y1),
                0.0
            ),
            (
                float(x2),
                float(y2),
                0.0
            )
        )

        if layer:
            entity.Layer = layer

        return entity

    def rectangle(
        self,
        x,
        y,
        width,
        height,
        layer=None
    ):

        self.line(
            x,
            y,
            x + width,
            y,
            layer
        )

        self.line(
            x + width,
            y,
            x + width,
            y + height,
            layer
        )

        self.line(
            x + width,
            y + height,
            x,
            y + height,
            layer
        )

        self.line(
            x,
            y + height,
            x,
            y,
            layer
        )
