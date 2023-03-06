import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("PyQt App")
    window.setGeometry(100, 100, 280, 80)
    helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
    helloMsg.move(60, 15)
    window.show()
    sys.exit(app.exec())

