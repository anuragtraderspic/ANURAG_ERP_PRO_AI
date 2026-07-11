import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from app.core.startup import startup
from app.ui.windows.main_window import MainWindow


def main():

    startup()

    app = QApplication(sys.argv)

    # ---------------- Load Theme ----------------

    theme = Path("app/resources/themes/light_theme.qss")

    if theme.exists():
        with open(theme, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())

    # --------------------------------------------

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()