import logging
import os


def setup_logger():

    log_folder = "logs"

    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    logging.basicConfig(
        filename=os.path.join(
            log_folder,
            "app.log"
        ),
        level=logging.INFO,
        format=(
            "%(asctime)s "
            "%(levelname)s "
            "%(message)s"
        )
    )

    return logging.getLogger("AutoCAD_GOST_Tools")