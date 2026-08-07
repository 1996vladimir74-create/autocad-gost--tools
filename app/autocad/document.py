import logging


class AutoCADDocument:


    def __init__(self, acad):

        self.acad = acad
        self.document = None

        self.logger = logging.getLogger(
            "AutoCAD_GOST_Tools"
        )


    def create(self):

        self.document = (
            self.acad.Documents.Add()
        )

        self.logger.info(
            "Создан новый DWG документ"
        )

        return self.document



    def save(self, path):

        if self.document:

            self.document.SaveAs(
                path
            )

            self.logger.info(
                f"Файл сохранен: {path}"
            )
    def save_as(
    self,
    path
):

    self.document.SaveAs(
        path
    )
