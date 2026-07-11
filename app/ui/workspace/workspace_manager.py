"""
=========================================================
ANURAG ERP PRO AI
Enterprise Edition

Module      : Workspace Manager
Version     : 3.0.0
=========================================================
"""

from __future__ import annotations

import logging

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTabWidget,
)

logger = logging.getLogger(__name__)


class WorkspaceManager(QWidget):
    """
    Enterprise Workspace Manager

    Responsibilities
    ----------------
    • Open Module
    • Close Module
    • Switch Module
    • Workspace Navigation
    • Future Dock Support
    """

    def __init__(self, parent=None):

        super().__init__(parent)

        self.tabs = QTabWidget()

        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)

        self.tabs.tabCloseRequested.connect(self.close_tab)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.tabs)

        logger.info("Workspace Manager Initialized")

    # --------------------------------------------------

    def open_page(self, title: str, page: QWidget):

        """
        Open New Page
        """

        for index in range(self.tabs.count()):

            if self.tabs.tabText(index) == title:

                self.tabs.setCurrentIndex(index)

                return

        self.tabs.addTab(page, title)

        self.tabs.setCurrentWidget(page)

    # --------------------------------------------------

    def close_tab(self, index: int):

        widget = self.tabs.widget(index)

        if widget:

            widget.deleteLater()

        self.tabs.removeTab(index)

    # --------------------------------------------------

    def current_page(self):

        return self.tabs.currentWidget()

    # --------------------------------------------------

    def clear(self):

        self.tabs.clear()