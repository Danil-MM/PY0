import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

from flag import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for btn in self.findChildren(QPushButton):
            btn.clicked.connect(self.color)
            self.radios = [self.top1, self.top2, self.top3, self.mid1, self.mid2, self.mid3, self.down1, self.down2,
                           self.down3]

    def color(self):
        text = "Цвета:"
        for radio in self.radios:
            if radio.isChecked():
                text += f" {radio.text()},"
        self.label.setText(text[:-1])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())