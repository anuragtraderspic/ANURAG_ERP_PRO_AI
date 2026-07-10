from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QProgressBar,
)


class SplashScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ANURAG ERP PRO AI")
        self.setFixedSize(650, 350)

        self.setWindowFlag(Qt.FramelessWindowHint)

        layout = QVBoxLayout(self)

        layout.setSpacing(20)

        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("ANURAG ERP PRO AI")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:#2563EB;
        """)

        subtitle = QLabel("Enterprise Edition")

        subtitle.setStyleSheet("""
            font-size:15px;
            color:#64748B;
        """)

        self.status = QLabel("Initializing ERP...")

        self.progress = QProgressBar()

        self.progress.setMaximum(100)

        layout.addWidget(title)

        layout.addWidget(subtitle)

        layout.addWidget(self.status)

        layout.addWidget(self.progress)

        self.value = 0

        self.timer = QTimer()

        self.timer.timeout.connect(self.update_progress)

        self.timer.start(40)

    def update_progress(self):

        self.value += 2

        self.progress.setValue(self.value)

        if self.value == 20:
            self.status.setText("Loading Database...")

        elif self.value == 40:
            self.status.setText("Loading Theme...")

        elif self.value == 60:
            self.status.setText("Loading Modules...")

        elif self.value == 80:
            self.status.setText("Preparing Dashboard...")

        elif self.value >= 100:
            self.timer.stop()

            self.close()