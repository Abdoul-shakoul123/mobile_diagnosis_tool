from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from modules.device_info import DeviceInfo

class DeviceTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Title
        title = QLabel("📱 Device Information")
        title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        # Info label
        self.label = QLabel("No device connected")
        self.label.setFont(QFont("Segoe UI", 11))
        self.label.setAlignment(Qt.AlignCenter)

        # Divider
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        # Button
        btn = QPushButton("🔍 Check Device")
        btn.setStyleSheet("""
            QPushButton {
                background-color: #00aaff;
                color: white;
                padding: 10px;
                border-radius: 8px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #008fcc;
            }
        """)
        btn.clicked.connect(self.check_device)

        layout.addWidget(title)
        layout.addWidget(line)
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def check_device(self):
        info = DeviceInfo().get_device_info()
        text = "\n".join([f"{k}: {v}" for k, v in info.items()])
        self.label.setText(text)
