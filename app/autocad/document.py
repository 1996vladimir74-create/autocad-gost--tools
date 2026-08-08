import logging


class AutoCADDocument:

    def __init__(self, document):

        self.document = document

        self.logger = logging.getLogger(
            "AutoCAD_GOST_Tools"
        )

    def set_units(self):

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

        return self.document.PaperSpace

    def activate_paper_space(self):

        self.document.SetVariable(
            "TILEMODE",
            0
        )

        self.document.ActiveSpace = 0

        self.document.MSpace = False

        self.logger.info(
            "Paper Space активирован"
        )

    def save_as(self, path):

        self.document.SaveAs(
            path
        )

        self.logger.info(
            f"DWG сохранен: {path}"
        )
