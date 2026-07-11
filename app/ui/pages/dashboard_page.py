"""
ANURAG ERP PRO AI
Dashboard Page
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QGridLayout,
    QFrame,
    QVBoxLayout,
)


class DashboardCard(QFrame):

    def __init__(self, title, value, color):
        super().__init__()

        self.setFixedSize(220, 90)

        self.setStyleSheet(f"""
        QFrame {{
            background: white;
            border: 2px solid {color};
            border-radius: 10px;
        }}
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(4)

        lbl1 = QLabel(title)
        lbl1.setAlignment(Qt.AlignCenter)
        lbl1.setStyleSheet("""
            font-size:12px;
            font-weight:600;
            color:#64748B;
        """)

        lbl2 = QLabel(value)
        lbl2.setAlignment(Qt.AlignCenter)
        lbl2.setStyleSheet(f"""
            font-size:18px;
            font-weight:700;
            color:{color};
        """)

        layout.addWidget(lbl1)
        layout.addWidget(lbl2)

class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()

        grid = QGridLayout(self)

        grid.setSpacing(15)

        cards = [

            ("Today's Sales", "₹ 0", "#10B981"),

            ("Purchase", "₹ 0", "#3B82F6"),

            ("Cash", "₹ 0", "#F59E0B"),

            ("Bank", "₹ 0", "#8B5CF6"),

            ("Stock Value", "₹ 0", "#EF4444"),

            ("Outstanding", "₹ 0", "#14B8A6"),

            ("GST", "₹ 0", "#EC4899"),

            ("Transactions", "0", "#6366F1"),

        ]
        grid.setAlignment(Qt.AlignTop)

        row = 0
        col = 0

        for title, value, color in cards:

            card = DashboardCard(title, value, color)

            grid.addWidget(card, row, col)

            col += 1

            if col == 4:
                col = 0
                row += 1