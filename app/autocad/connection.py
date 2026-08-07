import win32com.client
import logging


class AutoCADConnection:

    def __init__(self):

        self.acad = None
        self.logger = logging.getLogger(
            "AutoCAD_GOST_Tools"
        )


    def connect(self):

        try:

            self.acad = win32com.client.Dispatch(
                "AutoCAD.Application"
            )

            self.acad.Visible = True

            self.logger.info(
                "Подключение к AutoCAD успешно"
            )

            return self.acad


        except Exception as error:

            self.logger.error(
                f"Ошибка подключения AutoCAD: {error}"
            )

            raise ConnectionError(
                "AutoCAD не найден или не запущен"
            )


    def get_document(self):

        if not self.acad:

            self.connect()


        return self.acad.Documents.Add()