from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QComboBox,
    QCheckBox,
    QMessageBox,
)


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ANURAG ERP PRO AI - Login")
        self.setFixedSize(450, 600)

        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(40, 30, 40, 30)

        # Logo
        logo = QLabel("🏢")
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("font-size:60px;")

        # Title
        title = QLabel("ANURAG ERP PRO AI")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#2563EB;
        """)

        subtitle = QLabel("Enterprise Edition")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("""
            color:gray;
            font-size:13px;
        """)

        # Username
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        # Password
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        # Company
        self.company = QComboBox()
        self.company.addItem("ANURAG TRADERS")

        # Financial Year
        self.financial = QComboBox()
        self.financial.addItems([
            "2026-27",
            "2027-28"
        ])

        # Remember
        self.remember = QCheckBox("Remember Login")

        # Login Button
        login_btn = QPushButton("LOGIN")
        login_btn.clicked.connect(self.login)

        # Exit Button
        exit_btn = QPushButton("EXIT")
        exit_btn.clicked.connect(self.close)

        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addWidget(subtitle)

        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.company)
        layout.addWidget(self.financial)
        layout.addWidget(self.remember)

        layout.addWidget(login_btn)
        layout.addWidget(exit_btn)

    def login(self):

        if self.username.text() == "":
            QMessageBox.warning(
                self,
                "Login",
                "Please enter Username."
            )
            return

        if self.password.text() == "":
            QMessageBox.warning(
                self,
                "Login",
                "Please enter Password."
            )
            return

        QMessageBox.information(
            self,
            "Success",
            "Login Module Ready.\nDatabase Authentication Next Step."
        )