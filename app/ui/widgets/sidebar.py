"""
ANURAG ERP PRO AI
Enterprise Sidebar
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
)


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(230)

        self.setStyleSheet("""
            QWidget{
                background:#1E3A8A;
            }

            QPushButton{
                background:transparent;
                color:white;
                border:none;
                text-align:left;
                padding:12px 15px;
                font-size:23px;
            }

            QPushButton:hover{
                background:#2563EB;
            }

            QPushButton:pressed{
                background:#0F4AA8;
            }
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(10,10,10,10)

        title = QLabel("MENU")
        title.setStyleSheet("""
            color:white;
            font-size:16px;
            font-weight:bold;
            padding:10px;
        """)

        layout.addWidget(title)

        menus = [

            "🏠 Dashboard",
            "💰 Sales",
            "🛒 Purchase",
            "📦 Inventory",
            "📒 Accounts",
            "🏦 Banking",
            "📊 Reports",
            "👥 CRM",
            "👨‍💼 Payroll",
            "⚙ Settings",
            "🤖 AI Assistant"

        ]

        for menu in menus:

            btn = QPushButton(menu)

            btn.setCursor(Qt.PointingHandCursor)

            layout.addWidget(btn)

        layout.addStretch()