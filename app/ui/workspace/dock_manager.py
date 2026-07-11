"""
=========================================================
ANURAG ERP PRO AI
Enterprise Edition

Module      : Dock Manager
Version     : 3.0.0
=========================================================
"""

from __future__ import annotations

import logging

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDockWidget,
    QMainWindow,
    QWidget,
)

logger = logging.getLogger(__name__)


class DockManager:
    """
    Enterprise Dock Manager

    Responsibilities
    ----------------
    • Register Dock
    • Remove Dock
    • Find Dock
    • Show / Hide Dock
    • Future Layout Support
    """

    def __init__(self, main_window: QMainWindow):

        self.main_window = main_window
        self._docks: dict[str, QDockWidget] = {}

        logger.info("Dock Manager Initialized")

    # ---------------------------------------------------------

    def register_dock(
        self,
        dock_id: str,
        title: str,
        widget: QWidget,
        area: Qt.DockWidgetArea = Qt.LeftDockWidgetArea,
    ) -> QDockWidget:
        """
        Register New Dock
        """

        if dock_id in self._docks:

            logger.warning("Dock already exists : %s", dock_id)

            return self._docks[dock_id]

        dock = QDockWidget(title, self.main_window)

        dock.setObjectName(dock_id)

        dock.setWidget(widget)

        dock.setAllowedAreas(
            Qt.AllDockWidgetAreas
        )

        dock.setFeatures(

            QDockWidget.DockWidgetMovable
            |
            QDockWidget.DockWidgetFloatable

        )

        self.main_window.addDockWidget(area, dock)

        self._docks[dock_id] = dock

        logger.info("Dock Registered : %s", dock_id)

        return dock

    # ---------------------------------------------------------

    def dock(self, dock_id: str):

        return self._docks.get(dock_id)

    # ---------------------------------------------------------

    def remove(self, dock_id: str):

        dock = self._docks.get(dock_id)

        if dock:

            self.main_window.removeDockWidget(dock)

            dock.deleteLater()

            del self._docks[dock_id]

            logger.info("Dock Removed : %s", dock_id)

    # ---------------------------------------------------------

    def show(self, dock_id: str):

        dock = self.dock(dock_id)

        if dock:

            dock.show()

    # ---------------------------------------------------------

    def hide(self, dock_id: str):

        dock = self.dock(dock_id)

        if dock:

            dock.hide()

    # ---------------------------------------------------------

    def registered_docks(self):

        return list(self._docks.keys())