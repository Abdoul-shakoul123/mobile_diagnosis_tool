from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from modules.diagnosis import Diagnosis
from modules.device_info import DeviceInfo

class DiagnosisTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        title = QLabel("🩺 Device Diagnosis")
        title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        self.label = QLabel("No diagnosis run yet")
        self.label.setAlignment(Qt.AlignCenter)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)

        btn = QPushButton("▶ Run Diagnosis")
        btn.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                padding: 10px;
                border-radius: 8px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #1e7e34;
            }
        """)
        btn.clicked.connect(self.run_diagnosis)

        layout.addWidget(title)
        layout.addWidget(line)
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def run_diagnosis(self):
        info = DeviceInfo().get_device_info()
        report = Diagnosis().run_diagnosis(info)
        text = "\n".join(report)
        self.label.setText(text)
