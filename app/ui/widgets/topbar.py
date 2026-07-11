"""
ANURAG ERP PRO AI
Enterprise Top Bar
"""

from datetime import datetime

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
)


class TopBar(QWidget):

    def __init__(self):

        super().__init__()

        self.setFixedHeight(70)

        self.setStyleSheet("""

        QWidget{

            background:#2563EB;

            color:white;

        }

        QLabel{

            color:white;

            font-size:20px;

            font-weight:bold;

        }

        """)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(20,10,20,10)

        self.company = QLabel("🏢  ANURAG TRADERS")

        self.user = QLabel("👤 Admin")

        self.time = QLabel()

        layout.addWidget(self.company)

        layout.addStretch()

        layout.addWidget(self.user)

        layout.addSpacing(30)

        layout.addWidget(self.time)

        self.timer = QTimer()

        self.timer.timeout.connect(self.update_time)

        self.timer.start(1000)

        self.update_time()

    def update_time(self):

        self.time.setText(

            datetime.now().strftime("%d-%m-%Y   %I:%M:%S %p")

        )