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

        layers = (
            self.document.Layers
        )


        try:

            layer = layers.Add(
                name
            )

            self.logger.info(
                f"Создан слой {name}"
            )

            return layer


        except Exception:

            return layers.Item(
                name
            )


    def create_default_layers(self):

        layers = [

            "FRAME",
            "TITLE_BLOCK",
            "TEXT",
            "AUXILIARY"

        ]


        for layer in layers:

            self.create_layer(
                layer
            )