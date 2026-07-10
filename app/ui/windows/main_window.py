"""
ANURAG ERP PRO AI
Main Window
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QMainWindow,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)
from app.ui.widgets.sidebar import Sidebar

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ANURAG ERP PRO AI")
        self.resize(1400, 800)

        self.build_ui()

    def build_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        root = QVBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ---------------- Top Bar ----------------

        topbar = QLabel("🏢  ANURAG ERP PRO AI  |  Enterprise Edition")
        topbar.setFixedHeight(55)
        topbar.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        topbar.setStyleSheet("""
            background:#2563EB;
            color:white;
            font-size:26px;
            font-weight:bold;
            padding-left:20px;
        """)

        root.addWidget(topbar)

        # ---------------- Body ----------------

        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)

        # Sidebar Placeholder
        sidebar = Sidebar()      

        # Workspace Placeholder
        workspace = QLabel("Dashboard Area")
        workspace.setAlignment(Qt.AlignCenter)
        workspace.setStyleSheet("""
            background:#F4F7FC;
            color:#1E293B;
            font-size:22px;
            font-weight:bold;
        """)

        body.addWidget(sidebar)
        body.addWidget(workspace)

        root.addLayout(body)

        # ---------------- Status Bar ----------------

        status = QStatusBar()
        status.showMessage(
            "Ready   |   PostgreSQL Connected   |   Version 2.0"
        )

        self.setStatusBar(status)