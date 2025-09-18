# main.py
import sys
import threading
from PyQt5.QtWidgets import QApplication
from ui.home import HomeUI
from server import app

def run_server():
    app.run(host="0.0.0.0", port=5000, debug=False)

def main():
    print("🚀 Mobile Diagnosis Tool is starting...")

    # anzisha server kwenye background
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # anzisha UI
    qapp = QApplication(sys.argv)
    window = HomeUI()
    window.run()
    sys.exit(qapp.exec_())

if __name__ == "__main__":
    main()
