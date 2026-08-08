iimport logging
import time

import pythoncom
import win32com.client


class AutoCADConnection:
    """
    Управление подключением к AutoCAD через COM.
    """

    def __init__(self):
        self.acad = None
        self.logger = logging.getLogger(
            "AutoCAD_GOST_Tools"
        )

    def connect(self):
        """
        Подключается к уже запущенному AutoCAD.
        Если AutoCAD не запущен — запускает его.
        """

        pythoncom.CoInitialize()

        # Сначала пробуем получить уже запущенный AutoCAD
        try:
            self.acad = win32com.client.GetActiveObject(
                "AutoCAD.Application"
            )

            self.acad.Visible = True

            self.logger.info(
                "Получено существующее подключение к AutoCAD"
            )

            self._wait_until_ready()

            return self.acad

        except Exception:
            self.logger.info(
                "Запущенного AutoCAD не найдено. "
                "Запускаем новый экземпляр."
            )

        # Если AutoCAD не запущен — запускаем
        try:
            self.acad = win32com.client.DispatchEx(
                "AutoCAD.Application"
            )

            self.acad.Visible = True

            self._wait_until_ready()

            self.logger.info(
                "AutoCAD успешно запущен"
            )

            return self.acad

        except Exception as error:

            self.logger.exception(
                "Не удалось запустить AutoCAD"
            )

            raise ConnectionError(
                "Не удалось запустить AutoCAD.\n"
                "Убедитесь, что AutoCAD установлен."
            ) from error

    def _wait_until_ready(
        self,
        timeout=30
    ):
        """
        Ждет, пока AutoCAD закончит запуск.
        """

        start_time = time.time()

        while time.time() - start_time < timeout:

            try:

                state = self.acad.GetAcadState()

                if state.IsQuiescent:
                    return

            except Exception:
                pass

            time.sleep(0.5)

        raise TimeoutError(
            "AutoCAD слишком долго запускается."
        )

    def create_document(self):
        """
        Создает новый DWG.
        """

        if self.acad is None:
            self.connect()

        document = self.acad.Documents.Add()

        self.logger.info(
            "Создан новый DWG"
        )

        return document
