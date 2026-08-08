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

    raw_document = (
        connection.create_document()
    )

    document = AutoCADDocument(
        raw_document
    )

    document.set_units()

    document.get_layout()

    document.activate_paper_space()

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
