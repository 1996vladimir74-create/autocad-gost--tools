from dataclasses import dataclass


@dataclass
class Drawing:
    """
    Модель создаваемого чертежа
    """

    number: str
    name: str
    sheet_format: str
    orientation: str

    scale: str = "1:1"

    designer: str = ""
    checker: str = ""
    organization: str = ""

    def validate(self):
        """
        Проверка обязательных данных
        """

        errors = []

        if not self.number:
            errors.append("Не указан номер чертежа")

        if not self.name:
            errors.append("Не указано наименование")

        if not self.sheet_format:
            errors.append("Не выбран формат")

        if not self.orientation:
            errors.append("Не выбрана ориентация")

        return errors