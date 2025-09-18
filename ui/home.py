from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout
import sys
from ui.device_tab import DeviceTab
from ui.diagnosis_tab import DiagnosisTab
from ui.unlock_tab import UnlockTab

class HomeUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📱 Mobile Diagnosis Tool")
        self.setGeometry(200, 200, 700, 500)

        # Main layout
        layout = QVBoxLayout()
        tabs = QTabWidget()

        # Add tabs
        tabs.addTab(DeviceTab(), "📱 Device Info")
        tabs.addTab(DiagnosisTab(), "🩺 Diagnosis")
        tabs.addTab(UnlockTab(), "🔓 Unlock")

        layout.addWidget(tabs)
        self.setLayout(layout)

        # Apply modern stylesheet
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f7f9;
                font-family: Segoe UI, Arial;
                font-size: 12pt;
            }
            QTabWidget::pane {
                border: 1px solid #cccccc;
                background: white;
                border-radius: 6px;
            }
            QTabBar::tab {
                background: #e0e0e0;
                border: 1px solid #aaa;
                padding: 10px 20px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background: #00aaff;
                color: white;
                font-weight: bold;
            }
            QPushButton {
                background-color: #00aaff;
                color: white;
                padding: 8px 15px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #008fcc;
            }
            QLabel {
                font-size: 11pt;
            }
        """)

    def run(self):
        self.show()

def main():
    app = QApplication(sys.argv)
    window = HomeUI()
    window.run()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
