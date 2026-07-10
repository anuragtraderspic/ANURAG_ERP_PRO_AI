import sys

from PySide6.QtWidgets import QApplication

from app.core.startup import startup
from app.ui.windows.main_window import MainWindow


def main():

    startup()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()