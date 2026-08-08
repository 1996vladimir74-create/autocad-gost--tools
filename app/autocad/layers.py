import logging


class LayerManager:

    def __init__(self, document):

        self.document = document

        self.logger = logging.getLogger(
            "AutoCAD_GOST_Tools"
        )

    def create_layer(
        self,
        name
    ):

        layers = self.document.Layers

        try:

            layer = layers.Item(
                name
            )

            return layer

        except Exception:

            layer = layers.Add(
                name
            )

            self.logger.info(
                f"Создан слой: {name}"
            )

            return layer

    def create_default_layers(self):

        for name in [
            "FRAME",
            "TITLE_BLOCK",
            "TEXT",
            "AUXILIARY"
        ]:

            self.create_layer(
                name
            )
