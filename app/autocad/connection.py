import logging
import time

import pythoncom
import win32com.client


class AutoCADConnection:

    def __init__(self):

        self.logger = logging.getLogger(
            "AutoCAD_GOST_Tools"
        )

        self.app = None

    def connect(self):

        self.logger.info(
            "Инициализация COM..."
        )

        pythoncom.CoInitialize()

        # Сначала пробуем уже запущенный AutoCAD.
        try:

            self.app = (
                win32com.client.GetActiveObject(
                    "AutoCAD.Application"
                )
            )

            self.logger.info(
                "Подключение к уже запущенному AutoCAD выполнено"
            )

            return self.app

        except Exception as error:

            self.logger.info(
                f"Запущенный AutoCAD не найден: {error}"
            )

        # Затем пробуем создать AutoCAD через
        # стандартный ProgID.
        try:

            self.logger.info(
                "Попытка запуска AutoCAD.Application..."
            )

            self.app = (
                win32com.client.Dispatch(
                    "AutoCAD.Application"
                )
            )

            self.logger.info(
                "AutoCAD успешно запущен"
            )

            time.sleep(3)

            self.app.Visible = True

            return self.app

        except Exception as error:

            self.logger.error(
                f"AutoCAD.Application не запустился: {error}"
            )

        # AutoCAD 2021 использует COM ProgID
        # с версией 24.0.
        try:

            self.logger.info(
                "Попытка запуска AutoCAD.Application.24.0..."
            )

            self.app = (
                win32com.client.Dispatch(
                    "AutoCAD.Application.24.0"
                )
            )

            self.logger.info(
                "AutoCAD 2021 успешно запущен через ProgID 24.0"
            )

            time.sleep(3)

            self.app.Visible = True

            return self.app

        except Exception as error:

            self.logger.error(
                f"AutoCAD.Application.24.0 не запустился: {error}"
            )

            raise RuntimeError(
                "Не удалось подключиться к AutoCAD через COM. "
                "Проверь регистрацию AutoCAD."
            ) from error

    def create_document(self):

        if self.app is None:

            raise RuntimeError(
                "AutoCAD не подключен."
            )

        self.logger.info(
            "Создание нового документа AutoCAD..."
        )

        document = self.app.Documents.Add()

        time.sleep(3)

        self.logger.info(
            "Новый документ AutoCAD создан"
        )

        return document
