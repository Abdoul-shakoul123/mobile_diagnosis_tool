from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from modules.unlock import Unlock

class UnlockTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        title = QLabel("🔓 Unlock Options")
        title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        self.label = QLabel("Choose unlock method")
        self.label.setAlignment(Qt.AlignCenter)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)

        btn1 = QPushButton("🗝 Remove Screen Lock")
        btn2 = QPushButton("🔑 Bypass FRP")
        btn3 = QPushButton("📶 Carrier Unlock")

        for btn in (btn1, btn2, btn3):
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #dc3545;
                    color: white;
                    padding: 10px;
                    border-radius: 8px;
                    font-size: 11pt;
                }
                QPushButton:hover {
                    background-color: #a71d2a;
                }
            """)

        btn1.clicked.connect(lambda: self.label.setText(Unlock().remove_screen_lock()))
        btn2.clicked.connect(lambda: self.label.setText(Unlock().bypass_frp()))
        btn3.clicked.connect(lambda: self.label.setText(Unlock().carrier_unlock()))

        layout.addWidget(title)
        layout.addWidget(line)
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        self.setLayout(layout)
