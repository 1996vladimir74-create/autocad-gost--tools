import logging
import time

import pythoncom
import win32com.client


class AutoCADConnection:

    PROG_ID = "AutoCAD.Application.24"

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

        # -------------------------------------------------
        # 1. Пытаемся подключиться к уже запущенному AutoCAD
        # -------------------------------------------------

        try:

            self.app = (
                win32com.client.GetActiveObject(
                    self.PROG_ID
                )
            )

            self.logger.info(
                "Подключение к запущенному "
                "AutoCAD 2021 выполнено"
            )

            return self.app

        except Exception as error:

            self.logger.info(
                "Запущенный AutoCAD 2021 не найден: "
                f"{error}"
            )

        # -------------------------------------------------
        # 2. Если AutoCAD не запущен — запускаем его
        # -------------------------------------------------

        try:

            self.logger.info(
                f"Запуск {self.PROG_ID}..."
            )

            self.app = (
                win32com.client.Dispatch(
                    self.PROG_ID
                )
            )

            time.sleep(5)

            self.app.Visible = True

            self.logger.info(
                "AutoCAD 2021 успешно запущен"
            )

            return self.app

        except Exception as error:

            self.logger.exception(
                "Не удалось запустить AutoCAD 2021"
            )

            raise RuntimeError(
                "Не удалось подключиться к AutoCAD 2021 "
                "через COM ProgID "
                f"'{self.PROG_ID}'."
            ) from error

    def create_document(self):

        if self.app is None:

            raise RuntimeError(
                "AutoCAD не подключен."
            )

        self.logger.info(
            "Создание нового документа AutoCAD..."
        )

        try:

            document = (
                self.app.Documents.Add()
            )

            time.sleep(3)

            self.logger.info(
                "Новый документ AutoCAD создан"
            )

            return document

        except Exception as error:

            self.logger.exception(
                "Ошибка создания документа AutoCAD"
            )

            raise RuntimeError(
                "Не удалось создать новый документ "
                "AutoCAD."
            ) from error
