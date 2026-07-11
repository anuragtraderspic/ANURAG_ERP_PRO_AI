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
from app.ui.widgets.topbar import TopBar
from app.ui.widgets.statusbar import Status
from app.ui.pages.dashboard_page import DashboardPage

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

        topbar = TopBar()

        # ---------------- Body ----------------

        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)

        # Sidebar Placeholder
        sidebar = Sidebar()      

        # Workspace Placeholder
        workspace = DashboardPage()
       

        body.addWidget(sidebar)
        body.addWidget(workspace)

        root.addLayout(body)

        # ---------------- Status Bar ----------------

        status = Status()

        self.setStatusBar(status)
        

        self.setStatusBar(status)