from gui import MainWindow
from logger import setup_logger


def main():

    logger = setup_logger()

    logger.info(
        "AutoCAD GOST Tools запущен"
    )


    window = MainWindow(
        logger
    )


    window.run()



if __name__ == "__main__":

    main()