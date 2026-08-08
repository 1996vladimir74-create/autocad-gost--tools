from logger import setup_logger

from autocad.connection import AutoCADConnection


def main():

    logger = setup_logger()

    logger.info(
        "========== AUTOCAD CONNECTION TEST =========="
    )

    connection = AutoCADConnection()

    app = connection.connect()

    print()
    print("=" * 50)
    print("COM connection to AutoCAD: OK")
    print("=" * 50)

    print(
        f"Name: {app.Name}"
    )

    print(
        f"Version: {app.Version}"
    )

    print(
        f"Documents: {app.Documents.Count}"
    )

    print("=" * 50)

    input(
        "Нажмите Enter для завершения..."
    )


if __name__ == "__main__":
    main()
