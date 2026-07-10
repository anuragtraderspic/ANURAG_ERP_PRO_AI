import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

from app.core.startup import startup
from app.core.version import FULL_TITLE


def main():
    startup()

    app = QApplication(sys.argv)

    label = QLabel(FULL_TITLE)
    label.setAlignment(Qt.AlignCenter)
    label.setWindowTitle(FULL_TITLE)
    label.resize(700, 400)
    label.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()