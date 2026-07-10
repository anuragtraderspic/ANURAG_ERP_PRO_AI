import sys

from PySide6.QtWidgets import QApplication

from app.core.startup import startup
from app.ui.windows.splash_screen import SplashScreen


def main():

    startup()

    app = QApplication(sys.argv)

    splash = SplashScreen()

    splash.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()