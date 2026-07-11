"""
ANURAG ERP PRO AI
Enterprise Ribbon Bar
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
)


class RibbonBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(110)

        self.setStyleSheet("""
        QWidget{
            background:#FFFFFF;
            border-bottom:1px solid #D6DCE5;
        }

        QLabel{
            color:#374151;
            font-size:11pt;
            font-weight:bold;
        }

        QPushButton{
            background:transparent;
            border:none;
            padding:8px 15px;
            font-size:11pt;
            font-weight:600;
            color:#374151;
        }

        QPushButton:hover{
            background:#E8F0FE;
            border-radius:6px;
        }
        """)

        root = QVBoxLayout(self)
        root.setContentsMargins(10,5,10,5)

        # ---------- Top Menu ----------

        menu = QHBoxLayout()

        menus = [
            "File",
            "Edit",
            "View",
            "Masters",
            "Transactions",
            "Accounts",
            "Inventory",
            "Reports",
            "Window",
            "Help"
        ]

        for item in menus:
            lbl = QLabel(item)
            menu.addWidget(lbl)

        menu.addStretch()

        # ---------- Ribbon ----------

        ribbon = QHBoxLayout()

        tabs = [

            "🏠 Home",
            "💰 Sales",
            "🛒 Purchase",
            "📦 Inventory",
            "📒 Accounts",
            "🏦 Banking",
            "📊 Reports",
            "👥 CRM",
            "💼 Payroll",
            "🤖 AI"

        ]

        for tab in tabs:

            btn = QPushButton(tab)
            btn.setCursor(Qt.PointingHandCursor)
            ribbon.addWidget(btn)

        ribbon.addStretch()

        root.addLayout(menu)
        root.addSpacing(5)
        root.addLayout(ribbon)