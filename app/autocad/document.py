import logging


class AutoCADDocument:

    def __init__(self, document):

        self.document = document

        self.logger = logging.getLogger(
            "AutoCAD_GOST_Tools"
        )

    def set_units(self):
        """
        Устанавливает миллиметры как единицы чертежа.
        """

        # AutoCAD INSUNITS:
        # 4 = Millimeters

        self.document.SetVariable(
            "INSUNITS",
            4
        )

        self.document.SetVariable(
            "MEASUREMENT",
            1
        )

        self.logger.info(
            "Единицы документа установлены: мм"
        )

    def get_layout(self):
        """
        Получает Layout1 и делает его активным.
        """

        layouts = self.document.Layouts

        layout = layouts.Item(
            "Layout1"
        )

        self.document.ActiveLayout = layout

        self.logger.info(
            "Активирован Layout1"
        )

        return layout

    def get_paper_space(self):
        """
        Возвращает PaperSpace активного Layout.
        """

        return self.document.PaperSpace

    def save_as(self, path):

        self.document.SaveAs(
            path
        )

        self.logger.info(
            f"DWG сохранен: {path}"
        )
