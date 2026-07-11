"""
=========================================================
ANURAG ERP PRO AI
Enterprise Sidebar V2
=========================================================
"""

import os

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)


# =========================================================
# Sidebar Section Header
# =========================================================

class SidebarHeader(QLabel):

    def __init__(self, text):
        super().__init__(text.upper())

        self.setStyleSheet("""
        QLabel{
            color:#800000;
            background:transparent;
            font-size:11px;
            font-weight:700;
            letter-spacing:1px;
            padding:12px 12px 4px 12px;
        }
        """)


# =========================================================
# Sidebar Button
# =========================================================

class SidebarButton(QPushButton):

    def __init__(self, text, icon_file):

        super().__init__(text)

        self.setCursor(Qt.PointingHandCursor)

        self.setCheckable(True)

        self.setMinimumHeight(46)

        self.setIconSize(QSize(22,22))

        # ---------------- Icon ----------------

        icon_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "resources",
                "icons",
                icon_file
            )
        )

        if os.path.exists(icon_path):

            self.setIcon(QIcon(icon_path))

        # ---------------- Style ----------------

        self.setStyleSheet("""
        QPushButton{

            background:transparent;

            color:#000000;

            border:none;

            border-radius:12px;

            padding:12px 16px;

            text-align:left;

            font-size:14px;

            font-weight:600;

        }

        QPushButton:hover{

            background:#1E3A8A;

            color:white;

        }

        QPushButton:checked{

            background:#2563EB;

            color:white;

        }
        """)
        # =========================================================
# Sidebar
# =========================================================

class Sidebar(QWidget):

    def __init__(self):

        super().__init__()

        self.setObjectName("Sidebar")

        self.setFixedWidth(245)

        self.setStyleSheet("""
        QWidget#Sidebar{
            background:#0F172A;
            border-right:1px solid #1E293B;
        }
        """)

        # ================= Main Layout =================

        self.main_layout = QVBoxLayout(self)

        self.main_layout.setContentsMargins(12,12,12,12)

        self.main_layout.setSpacing(6)

        # ===================================================
        # Company Area
        # ===================================================

        company = QLabel("🏢 ANURAG ERP PRO AI")

        company.setStyleSheet("""
        QLabel{
            color:#000000;
            font-size:17px;
            font-weight:700;
            padding:8px;
        }
        """)

        edition = QLabel("Enterprise Edition")

        edition.setStyleSheet("""
        QLabel{
            color:#000000;
            font-size:11px;
            padding-left:10px;
            padding-bottom:10px;
        }
        """)

        self.main_layout.addWidget(company)

        self.main_layout.addWidget(edition)

        # ===================================================
        # MENU
        # ===================================================

        self.main_layout.addWidget(SidebarHeader("MAIN"))

        self.btn_dashboard = SidebarButton(
            "Dashboard",
            "dashboard.png"
        )

        self.main_layout.addWidget(self.btn_dashboard)

        # ===================================================
        # SALES
        # ===================================================

        self.main_layout.addWidget(SidebarHeader("SALES"))

        self.btn_sales = SidebarButton(
            "Sales",
            "sales.png"
        )

        self.btn_purchase = SidebarButton(
            "Purchase",
            "purchase.png"
        )

        self.main_layout.addWidget(self.btn_sales)
        self.main_layout.addWidget(self.btn_purchase)

        # ===================================================
        # INVENTORY
        # ===================================================

        self.main_layout.addWidget(SidebarHeader("INVENTORY"))

        self.btn_inventory = SidebarButton(
            "Inventory",
            "inventory.png"
        )

        self.main_layout.addWidget(self.btn_inventory)

        # ===================================================
        # ACCOUNTS
        # ===================================================

        self.main_layout.addWidget(SidebarHeader("ACCOUNTS"))

        self.btn_accounts = SidebarButton(
            "Accounts",
            "accounts.png"
        )

        self.btn_banking = SidebarButton(
            "Banking",
            "banking.png"
        )

        self.main_layout.addWidget(self.btn_accounts)
        self.main_layout.addWidget(self.btn_banking)
                # ===================================================
        # REPORTS
        # ===================================================

        self.main_layout.addWidget(SidebarHeader("REPORTS"))

        self.btn_reports = SidebarButton(
            "Reports",
            "reports.png"
        )

        self.main_layout.addWidget(self.btn_reports)

        # ===================================================
        # MANAGEMENT
        # ===================================================

        self.main_layout.addWidget(SidebarHeader("MANAGEMENT"))

        self.btn_crm = SidebarButton(
            "CRM",
            "crm.png"
        )

        self.btn_payroll = SidebarButton(
            "Payroll",
            "payroll.png"
        )

        self.main_layout.addWidget(self.btn_crm)
        self.main_layout.addWidget(self.btn_payroll)

        # ===================================================
        # SYSTEM
        # ===================================================

        self.main_layout.addWidget(SidebarHeader("SYSTEM"))

        self.btn_settings = SidebarButton(
            "Settings",
            "settings.png"
        )

        self.btn_ai = SidebarButton(
            "AI Assistant",
            "ai.png"
        )

        self.main_layout.addWidget(self.btn_settings)
        self.main_layout.addWidget(self.btn_ai)

        # ===================================================
        # Spacer
        # ===================================================

        self.main_layout.addStretch()

        # ===================================================
        # User Card
        # ===================================================

        user_card = QFrame()

        user_card.setStyleSheet("""
        QFrame{

            background:#1E293B;

            border-radius:12px;

            padding:8px;

        }
        """)

        user_layout = QVBoxLayout(user_card)

        user_layout.setContentsMargins(10,10,10,10)

        lbl_user = QLabel("👤 Administrator")

        lbl_user.setStyleSheet("""
        QLabel{

            color:white;

            font-size:13px;

            font-weight:700;

            background:transparent;

        }
        """)

        lbl_status = QLabel("● Online")

        lbl_status.setStyleSheet("""
        QLabel{

            color:#22C55E;

            font-size:11px;

            background:transparent;

        }
        """)

        lbl_version = QLabel("ERP PRO AI 1.0")

        lbl_version.setStyleSheet("""
        QLabel{

            color:#94A3B8;

            font-size:10px;

            background:transparent;

        }
        """)

        user_layout.addWidget(lbl_user)
        user_layout.addWidget(lbl_status)
        user_layout.addWidget(lbl_version)

        self.main_layout.addWidget(user_card)

        # ===================================================
        # Default Selected Menu
        # ===================================================

        self.btn_dashboard.setChecked(True)