"""
Enterprise Status Bar
"""

from PySide6.QtWidgets import QStatusBar


class Status(QStatusBar):

    def __init__(self):

        super().__init__()

        self.showMessage(

            "🟢 Ready      |      PostgreSQL Connected      |      Local Server"

        )