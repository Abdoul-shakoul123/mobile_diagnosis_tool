from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
import sys

def main():
    app = QApplication(sys.argv)

    # Window kuu
    window = QWidget()
    window.setWindowTitle("📱 Mobile Diagnosis Tool")
    window.setGeometry(200, 200, 400, 300)

    layout = QVBoxLayout()

    # Title
    label = QLabel("Welcome to Mobile Diagnosis Tool")
    layout.addWidget(label)

    # Buttons
    btn1 = QPushButton("Device Info")
    btn2 = QPushButton("Diagnosis")
    btn3 = QPushButton("Unlock")

    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
