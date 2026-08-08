import time

from logger import setup_logger

from autocad.connection import AutoCADConnection
from autocad.document import AutoCADDocument
from autocad.diagnostic import AutoCADDiagnostic


def main():

    logger = setup_logger()

    logger.info(
        "Запуск AutoCAD Diagnostic"
    )

    connection = AutoCADConnection()

    connection.connect()

    logger.info(
        "AutoCAD connection established"
    )

    time.sleep(2)

    raw_document = (
        connection.create_document()
    )

    logger.info(
        "Document created"
    )

    time.sleep(3)

    document = AutoCADDocument(
        raw_document
    )

    document.set_units()

    time.sleep(1)

    document.get_layout()

    time.sleep(1)

    diagnostic = AutoCADDiagnostic(
        raw_document
    )

    diagnostic.run()

    print()
    print(
        "AutoCAD diagnostic completed."
    )

    input(
        "Нажмите Enter для завершения..."
    )


if __name__ == "__main__":
    main()
