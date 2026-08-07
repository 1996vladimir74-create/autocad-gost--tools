"""AutoCAD GOST Tools - GOST drawing frame generator.

A standalone Windows GUI that collects drawing metadata and creates a
GOST-style sheet frame and title block directly in a running AutoCAD session.

The application is intentionally terminal-free for the end user: the final
Windows .exe is built with PyInstaller. AutoCAD must be installed on the
workstation because the utility uses AutoCAD's COM automation interface.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

FORMATS_MM: dict[str, tuple[int, int]] = {
    "A0": (841, 1189),
    "A1": (594, 841),
    "A2": (420, 594),
    "A3": (297, 420),
    "A4": (210, 297),
}

LEFT_MARGIN = 20
OTHER_MARGIN = 5
TITLE_BLOCK_WIDTH = 185
TITLE_BLOCK_HEIGHT = 55


def get_sheet_size(format_name: str, orientation: str) -> tuple[int, int]:
    """Return width and height in millimetres for the requested orientation."""
    width, height = FORMATS_MM[format_name]
    if orientation == "Landscape":
        return max(width, height), min(width, height)
    return min(width, height), max(width, height)


def add_line(space, x1: float, y1: float, x2: float, y2: float) -> None:
    """Add one line to AutoCAD model space."""
    space.AddLine((x1, y1, 0.0), (x2, y2, 0.0))


def add_text(space, text: str, x: float, y: float, height: float = 3.5) -> None:
    """Add single-line text to AutoCAD model space."""
    if not text:
        return
    space.AddText(text, (x, y, 0.0), height)


def draw_frame(space, width: int, height: int) -> None:
    """Draw the sheet border with a 20 mm binding margin on the left."""
    x0, y0 = 0, 0
    x1, y1 = width, height

    # Outer sheet boundary (reference geometry).
    add_line(space, x0, y0, x1, y0)
    add_line(space, x1, y0, x1, y1)
    add_line(space, x1, y1, x0, y1)
    add_line(space, x0, y1, x0, y0)

    # Drawing frame: 20 mm left, 5 mm on the other sides.
    fx0 = LEFT_MARGIN
    fy0 = OTHER_MARGIN
    fx1 = width - OTHER_MARGIN
    fy1 = height - OTHER_MARGIN
    add_line(space, fx0, fy0, fx1, fy0)
    add_line(space, fx1, fy0, fx1, fy1)
    add_line(space, fx1, fy1, fx0, fy1)
    add_line(space, fx0, fy1, fx0, fy0)


def draw_title_block(space, width: int, drawing_number: str, name: str) -> None:
    """Draw a basic Form-1-style title-block envelope and populate key fields.

    The 185 x 55 mm envelope is used for the standard machine-drawing title
    block. Internal fields are kept deliberately simple in this first release;
    the geometry can be expanded as the project adds the remaining ESKD fields.
    """
    x0 = width - OTHER_MARGIN - TITLE_BLOCK_WIDTH
    y0 = OTHER_MARGIN
    x1 = width - OTHER_MARGIN
    y1 = y0 + TITLE_BLOCK_HEIGHT

    add_line(space, x0, y0, x1, y0)
    add_line(space, x1, y0, x1, y1)
    add_line(space, x1, y1, x0, y1)
    add_line(space, x0, y1, x0, y0)

    # Main horizontal divisions.
    for y in (y0 + 5, y0 + 15, y0 + 30, y0 + 40, y0 + 47):
        add_line(space, x0, y, x1, y)

    # Vertical divisions for the upper information area.
    for x in (x0 + 15, x0 + 65, x0 + 125):
        add_line(space, x, y0 + 30, x, y1)

    # Lower information area.
    add_line(space, x0 + 95, y0, x0 + 95, y0 + 30)
    add_line(space, x0 + 140, y0, x0 + 140, y0 + 15)

    # User-provided fields.
    add_text(space, drawing_number, x0 + 3, y0 + 42, 4.0)
    add_text(space, name, x0 + 3, y0 + 33, 3.5)
    add_text(space, "AutoCAD GOST Tools", x0 + 3, y0 + 18, 3.0)


def connect_to_autocad():
    """Connect to AutoCAD through COM, starting it if necessary."""
    try:
        import win32com.client  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "Не найден модуль pywin32. Установите зависимости или используйте собранный EXE."
        ) from exc

    try:
        try:
            acad = win32com.client.GetActiveObject("AutoCAD.Application")
        except Exception:
            acad = win32com.client.Dispatch("AutoCAD.Application")
        acad.Visible = True
        return acad
    except Exception as exc:
        raise RuntimeError(
            "Не удалось подключиться к AutoCAD. Убедитесь, что AutoCAD установлен."
        ) from exc


def create_drawing(drawing_number: str, name: str, format_name: str, orientation: str) -> None:
    """Create the requested frame and title block in AutoCAD model space."""
    width, height = get_sheet_size(format_name, orientation)
    acad = connect_to_autocad()

    if acad.Documents.Count == 0:
        document = acad.Documents.Add()
    else:
        document = acad.ActiveDocument

    # AutoCAD INSUNITS value 4 = millimetres.
    try:
        document.SetVariable("INSUNITS", 4)
    except Exception:
        pass

    space = document.ModelSpace
    draw_frame(space, width, height)
    draw_title_block(space, width, drawing_number, name)
    document.Regen(1)


def build_gui() -> tk.Tk:
    root = tk.Tk()
    root.title("AutoCAD GOST Tools")
    root.resizable(False, False)

    frame = ttk.Frame(root, padding=18)
    frame.grid(row=0, column=0)

    ttk.Label(frame, text="AutoCAD GOST Tools", font=("Segoe UI", 15, "bold")).grid(
        row=0, column=0, columnspan=2, pady=(0, 14)
    )

    ttk.Label(frame, text="Номер чертежа:").grid(row=1, column=0, sticky="w", pady=5)
    number_var = tk.StringVar()
    ttk.Entry(frame, textvariable=number_var, width=35).grid(row=1, column=1, pady=5)

    ttk.Label(frame, text="Наименование:").grid(row=2, column=0, sticky="w", pady=5)
    name_var = tk.StringVar()
    ttk.Entry(frame, textvariable=name_var, width=35).grid(row=2, column=1, pady=5)

    ttk.Label(frame, text="Формат:").grid(row=3, column=0, sticky="w", pady=5)
    format_var = tk.StringVar(value="A4")
    ttk.Combobox(
        frame, textvariable=format_var, values=list(FORMATS_MM), state="readonly", width=32
    ).grid(row=3, column=1, pady=5)

    ttk.Label(frame, text="Ориентация:").grid(row=4, column=0, sticky="w", pady=5)
    orientation_var = tk.StringVar(value="Portrait")
    ttk.Combobox(
        frame,
        textvariable=orientation_var,
        values=("Portrait", "Landscape"),
        state="readonly",
        width=32,
    ).grid(row=4, column=1, pady=5)

    def generate() -> None:
        drawing_number = number_var.get().strip()
        name = name_var.get().strip()
        format_name = format_var.get()
        orientation = orientation_var.get()

        if not drawing_number or not name:
            messagebox.showwarning("Не хватает данных", "Заполните номер чертежа и наименование.")
            return

        try:
            create_drawing(drawing_number, name, format_name, orientation)
        except Exception as exc:
            messagebox.showerror("Ошибка", str(exc))
            return

        width, height = get_sheet_size(format_name, orientation)
        messagebox.showinfo(
            "Готово",
            f"Рамка создана в AutoCAD.\nФормат: {format_name} ({width} × {height} мм).",
        )

    ttk.Button(frame, text="Создать рамку в AutoCAD", command=generate).grid(
        row=5, column=0, columnspan=2, pady=(16, 0), ipadx=10, ipady=5
    )

    ttk.Label(
        frame,
        text="Требуется установленный AutoCAD. Терминал для запуска EXE не нужен.",
    ).grid(row=6, column=0, columnspan=2, pady=(10, 0))

    return root


def main() -> None:
    root = build_gui()
    root.mainloop()


if __name__ == "__main__":
    main()
