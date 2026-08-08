import logging


class AutoCADSetup:

    def __init__(self, document):

        self.document = document

        self.logger = logging.getLogger(
            "AutoCAD_GOST_Tools"
        )

    def prepare(self):

        self._set_units()

        self._set_background()

        self.logger.info(
            "Документ AutoCAD подготовлен"
        )

    def _set_units(self):

        self.document.SetVariable(
            "INSUNITS",
            4
        )

        self.document.SetVariable(
            "LUNITS",
            2
        )

        self.document.SetVariable(
            "LUPREC",
            2
        )

    def _set_background(self):

        # Цвет фона оставляем настройкой
        # самого AutoCAD.
        pass
