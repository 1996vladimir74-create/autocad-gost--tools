import time

from logger import setup_logger
from autocad.connection import AutoCADConnection


def main():

    logger = setup_logger()

    logger.info(
        "========== AUTOCAD CONNECTION TEST =========="
    )

    connection = AutoCADConnection()

    app = connection.connect()

    logger.info(
        f"AutoCAD application: {app.Name}"
    )

    logger.info(
        f"AutoCAD version: {app.Version}"
    )

    logger.info(
        f"Documents count: {app.Documents.Count}"
    )

    time.sleep(2)

    print()
    print("COM connection to AutoCAD: OK")
    print(
        f"AutoCAD version: {app.Version}"
    )
    print(
        f"Documents: {app.Documents.Count}"
    )
    print()

    input(
        "Нажмите Enter для завершения..."
    )


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
