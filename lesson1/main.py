import sys
from math import factorial, sqrt

from PyQt5.QtWidgets import QApplication,  QPushButton, QMainWindow, QWidget

from calc import Ui_Form


class Example(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for btn in self.findChildren(QPushButton):
            btn.clicked.connect(self.action_digit)


    def action_digit(self):
        btn = self.sender()
        btn_text = btn.text()
        line_text = self.lineEdit.text()
        if btn_text.isdigit() or btn_text in "+*/-.":
            self.lineEdit.setText(line_text + btn_text)
        elif btn_text == "=":
            equation = line_text.replace("^", "**")
            value = str(eval(equation))
            self.lineEdit.setText(value)
        elif btn_text == "С":
            self.lineEdit.clear()
        elif btn_text == "!":
            current_text = int(line_text)
            self.lineEdit.setText(str(factorial(current_text)))
        elif btn_text == "√":
            current_text = int(line_text)
            self.lineEdit.setText(str(sqrt(current_text)))
        elif btn_text == "^":
            self.lineEdit.setText(line_text + "**")




def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())