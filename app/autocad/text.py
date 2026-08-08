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
        """
        Создание обычного AutoCAD TEXT.
        Пока намеренно не используем MText:
        это уменьшает количество COM-зависимостей.
        """

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
