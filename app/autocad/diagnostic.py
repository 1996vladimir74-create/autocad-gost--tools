import logging
import time


class AutoCADDiagnostic:

    def __init__(self, document):

        self.document = document

        self.logger = logging.getLogger(
            "AutoCAD_GOST_Tools"
        )

    def run(self):

        self.logger.info(
            "========== DIAGNOSTIC START =========="
        )

        time.sleep(1)

        self._set_paper_space()

        time.sleep(1)

        self._create_a3_frame()

        time.sleep(1)

        self._create_test_text()

        time.sleep(1)

        self._report_state()

        try:
            self.document.Regen(1)
        except Exception as error:
            self.logger.warning(
                f"Regen error: {error}"
            )

        self.logger.info(
            "========== DIAGNOSTIC END =========="
        )

    def _set_paper_space(self):

        self.logger.info(
            "Переключение в Paper Space..."
        )

        try:

            self.document.SetVariable(
                "TILEMODE",
                0
            )

            time.sleep(0.5)

            self.document.ActiveSpace = 0

            time.sleep(0.5)

            self.document.MSpace = False

            self.logger.info(
                "Paper Space активирован"
            )

        except Exception as error:

            self.logger.error(
                f"Paper Space error: {error}"
            )

            raise

    def _create_a3_frame(self):

        space = self.document.PaperSpace

        # A3 landscape
        sheet_width = 420.0
        sheet_height = 297.0

        # Рабочая рамка
        left = 20.0
        bottom = 5.0
        right = 5.0
        top = 5.0

        x1 = left
        y1 = bottom

        x2 = sheet_width - right
        y2 = sheet_height - top

        self.logger.info(
            f"A3: {sheet_width} x {sheet_height}"
        )

        self.logger.info(
            f"Frame: ({x1},{y1}) -> ({x2},{y2})"
        )

        # Нижняя
        self._line(
            space,
            x1,
            y1,
            x2,
            y1
        )

        # Правая
        self._line(
            space,
            x2,
            y1,
            x2,
            y2
        )

        # Верхняя
        self._line(
            space,
            x2,
            y2,
            x1,
            y2
        )

        # Левая
        self._line(
            space,
            x1,
            y2,
            x1,
            y1
        )

    def _create_test_text(self):

        space = self.document.PaperSpace

        text = space.AddText(
            "A3 GOST TEST",
            (
                25.0,
                280.0,
                0.0
            ),
            5.0
        )

        self.logger.info(
            f"TEXT created: {text.ObjectName}"
        )

    def _line(
        self,
        space,
        x1,
        y1,
        x2,
        y2
    ):

        entity = space.AddLine(
            (
                float(x1),
                float(y1),
                0.0
            ),
            (
                float(x2),
                float(y2),
                0.0
            )
        )

        self.logger.info(
            f"LINE created: {entity.ObjectName}"
        )

        return entity

    def _report_state(self):

        try:

            tilemode = self.document.GetVariable(
                "TILEMODE"
            )

        except Exception as error:

            tilemode = f"ERROR: {error}"

        try:

            active_space = self.document.ActiveSpace

        except Exception as error:

            active_space = f"ERROR: {error}"

        try:

            active_layout = (
                self.document.ActiveLayout.Name
            )

        except Exception as error:

            active_layout = f"ERROR: {error}"

        try:

            model_count = (
                self.document.ModelSpace.Count
            )

        except Exception as error:

            model_count = f"ERROR: {error}"

        try:

            paper_count = (
                self.document.PaperSpace.Count
            )

        except Exception as error:

            paper_count = f"ERROR: {error}"

        self.logger.info(
            f"TILEMODE = {tilemode}"
        )

        self.logger.info(
            f"ActiveSpace = {active_space}"
        )

        self.logger.info(
            f"ActiveLayout = {active_layout}"
        )

        self.logger.info(
            f"ModelSpace entities = {model_count}"
        )

        self.logger.info(
            f"PaperSpace entities = {paper_count}"
        )
