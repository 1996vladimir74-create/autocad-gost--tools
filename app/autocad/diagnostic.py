import logging


class AutoCADDiagnostic:

    def __init__(self, document):

        self.document = document

        self.logger = logging.getLogger(
            "AutoCAD_GOST_Tools"
        )

    def run(self):

        self.logger.info(
            "========== AUTOCADE DIAGNOSTIC START =========="
        )

        self._print_document_state()

        self._activate_paper_space()

        self._print_document_state()

        self._create_test_geometry()

        self._print_entity_counts()

        self.document.Regen(1)

        self.logger.info(
            "========== AUTOCADE DIAGNOSTIC END =========="
        )

    def _print_document_state(self):

        try:

            tilemode = self.document.GetVariable(
                "TILEMODE"
            )

        except Exception:

            tilemode = "ERROR"

        try:

            active_space = self.document.ActiveSpace

        except Exception:

            active_space = "ERROR"

        try:

            active_layout = (
                self.document.ActiveLayout.Name
            )

        except Exception:

            active_layout = "ERROR"

        self.logger.info(
            f"TILEMODE = {tilemode}"
        )

        self.logger.info(
            f"ActiveSpace = {active_space}"
        )

        self.logger.info(
            f"ActiveLayout = {active_layout}"
        )

    def _activate_paper_space(self):

        self.logger.info(
            "Переключение в Paper Space..."
        )

        # 0 = Paper Space
        self.document.SetVariable(
            "TILEMODE",
            0
        )

        self.document.ActiveSpace = 0

        self.document.MSpace = False

        self.logger.info(
            "Paper Space активирован"
        )

    def _create_test_geometry(self):

        paper_space = self.document.PaperSpace

        self.logger.info(
            "Получен PaperSpace объект"
        )

        # ---------------------------------
        # Тестовая внешняя рамка
        # ---------------------------------

        self._line(
            paper_space,
            20,
            20,
            400,
            20
        )

        self._line(
            paper_space,
            400,
            20,
            400,
            277
        )

        self._line(
            paper_space,
            400,
            277,
            20,
            277
        )

        self._line(
            paper_space,
            20,
            277,
            20,
            20
        )

        # ---------------------------------
        # Тестовая внутренняя рамка
        # ---------------------------------

        self._line(
            paper_space,
            25,
            25,
            395,
            25
        )

        self._line(
            paper_space,
            395,
            25,
            395,
            272
        )

        self._line(
            paper_space,
            395,
            272,
            25,
            272
        )

        self._line(
            paper_space,
            25,
            272,
            25,
            25
        )

        # ---------------------------------
        # Тестовый штамп
        # ---------------------------------

        x = 210
        y = 25

        width = 185
        height = 55

        self._rectangle(
            paper_space,
            x,
            y,
            width,
            height
        )

        # ---------------------------------
        # Одна тестовая надпись
        # ---------------------------------

        text = paper_space.AddText(
            "AUTO CAD GOST TEST",
            (
                215.0,
                50.0,
                0.0
            ),
            5.0
        )

        self.logger.info(
            f"Создан TEXT entity: {text.ObjectName}"
        )

    def _rectangle(
        self,
        space,
        x,
        y,
        width,
        height
    ):

        self._line(
            space,
            x,
            y,
            x + width,
            y
        )

        self._line(
            space,
            x + width,
            y,
            x + width,
            y + height
        )

        self._line(
            space,
            x + width,
            y + height,
            x,
            y + height
        )

        self._line(
            space,
            x,
            y + height,
            x,
            y
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
            f"Создан LINE: {entity.ObjectName}"
        )

        return entity

    def _print_entity_counts(self):

        try:

            model_count = (
                self.document.ModelSpace.Count
            )

        except Exception:

            model_count = "ERROR"

        try:

            paper_count = (
                self.document.PaperSpace.Count
            )

        except Exception:

            paper_count = "ERROR"

        self.logger.info(
            f"ModelSpace entities = {model_count}"
        )

        self.logger.info(
            f"PaperSpace entities = {paper_count}"
        )
