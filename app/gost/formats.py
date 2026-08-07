"""
Форматы листов по ГОСТ 2.301
Размеры указаны в миллиметрах
"""


FORMATS = {

    "A4": {
        "width": 210,
        "height": 297
    },

    "A3": {
        "width": 297,
        "height": 420
    },

    "A2": {
        "width": 420,
        "height": 594
    },

    "A1": {
        "width": 594,
        "height": 841
    },

    "A0": {
        "width": 841,
        "height": 1189
    }

}


def get_sheet_size(sheet_format, orientation):
    """
    Возвращает размеры листа
    с учетом ориентации
    """

    if sheet_format not in FORMATS:
        raise ValueError(
            f"Неизвестный формат {sheet_format}"
        )

    size = FORMATS[sheet_format].copy()

    if orientation.lower() in [
        "landscape",
        "альбомная"
    ]:
        size["width"], size["height"] = (
            size["height"],
            size["width"]
        )

    return size