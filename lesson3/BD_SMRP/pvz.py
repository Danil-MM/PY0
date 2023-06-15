import sys

from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog

from BD_SMRP.add_seller import Ui_Add
from BD_SMRP.database1 import Seller
from BD_SMRP.database1.base_meta1 import global_init, create_session
from BD_SMRP.database1.takeorder import Takeorder
from BD_SMRP.update_order import Ui_Dialog1
from BD_SMRP.update_seller import Ui_Dialog
from tabledb import Ui_MainWindow

class TableViewer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.seller_updater = None
        self.table_is_changeable = True

    def initUI(self):
            global_init("database1/db.db")
            self.session = create_session()
            self.btnupdate.clicked.connect(self.load_table)
            self.btnupdate_2.clicked.connect(self.load_sellers)
            self.tableWidget_3.doubleClicked.connect(self.update_seller)
            self.pushButton.clicked.connect(self.add_seller)
            self.tableWidget.doubleClicked.connect(self.update_order)


    def add_seller(self):
        self.seller_adder = SellerAdder(self.session)
        if self.seller_adder.exec_():
            new_seller = Seller(
                id=self.seller_adder.label_id.text(),
                name=self.seller_adder.lineEdit_1.text(),
                ProductName=self.seller_adder.lineEdit_2.text(),
                ProductPrice=self.seller_adder.lineEdit_3.text(),
            )
            self.session.add(new_seller)
            self.session.commit()
            self.load_table()
    def update_seller(self, index: QModelIndex):
        current_row = index.row()
        id_ = int(self.tableWidget_3.item(current_row, 0).text())
        self.seller_updater = SellerUpdater(id_)
        self.seller_updater.exec_()
        self.load_table()

    def update_order(self, index: QModelIndex):
        current_row = index.row()
        id_ = int(self.tableWidget.item(current_row, 0).text())
        self.order_updater = OrderUpdater(id_)
        self.order_updater.exec_()
        self.load_table()

    def load_table(self):
        takeorder = self.session.query(Takeorder).all()
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        for order in takeorder:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            tmp = QTableWidgetItem(str(order.order_id))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_position, 0, tmp)
            tmp = QTableWidgetItem(str(order.seller.ProductName))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_position, 1, tmp)
            tmp = QTableWidgetItem(str(order.seller.ProductPrice))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_position, 2, tmp)
            tmp = QTableWidgetItem(str(order.buyer.FirstName))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_position, 3, tmp)
            tmp = QTableWidgetItem(str(order.buyer.SecondName))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_position, 4, tmp)
            tmp = QTableWidgetItem(str(order.pvz.id))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_position, 5, tmp)
            tmp = QTableWidgetItem(str(order.status))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row_position, 6, tmp)
            if order.status == 'Выдано':  # проверка статуса заказа
                  tmp = QTableWidgetItem(str(order.order_id))
                  tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
                  self.tableWidget_2.insertRow(self.tableWidget_2.rowCount())
                  self.tableWidget_2.setItem(self.tableWidget_2.rowCount() - 1, 0, tmp)
                  tmp = QTableWidgetItem(str(order.seller.ProductName))
                  tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
                  self.tableWidget_2.setItem(self.tableWidget_2.rowCount() - 1, 1, tmp)
                  tmp = QTableWidgetItem(str(order.seller.ProductPrice))
                  tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
                  self.tableWidget_2.setItem(self.tableWidget_2.rowCount() - 1, 2, tmp)
                  tmp = QTableWidgetItem(str(order.buyer.FirstName))
                  tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
                  self.tableWidget_2.setItem(self.tableWidget_2.rowCount() - 1, 3, tmp)
                  tmp = QTableWidgetItem(str(order.buyer.SecondName))
                  tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
                  self.tableWidget_2.setItem(self.tableWidget_2.rowCount() - 1, 4, tmp)
                  tmp = QTableWidgetItem(str(order.pvz.id))
                  tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
                  self.tableWidget_2.setItem(self.tableWidget_2.rowCount() - 1, 5, tmp)
                  tmp = QTableWidgetItem(str(order.status))
                  tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
                  self.tableWidget_2.setItem(self.tableWidget_2.rowCount() - 1, 6, tmp)


    def load_sellers(self):
        sellers = self.session.query(Seller).all()
        self.tableWidget_3.setRowCount(0)
        for seller in sellers:
                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)
                tmp = QTableWidgetItem(str(seller.id))
                tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
                self.tableWidget_3.setItem(row_position, 0, tmp)
                tmp = QTableWidgetItem(str(seller.name))
                tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
                self.tableWidget_3.setItem(row_position, 1, tmp)
                tmp = QTableWidgetItem(str(seller.ProductName))
                tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
                self.tableWidget_3.setItem(row_position, 2, tmp)
                tmp = QTableWidgetItem(str(seller.ProductPrice))
                tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
                self.tableWidget_3.setItem(row_position, 3, tmp)
                tmp = QTableWidgetItem(str(seller.ProductPrice))
                tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
        self.table_is_changeable = True

class SellerUpdater(QDialog, Ui_Dialog):
    def __init__(self, seller_id):
        super().__init__()
        self.setupUi(self)

        self.session = create_session()
        self.seller = self.session.query(Seller).get(seller_id)
        self.label_id.setText(str(self.seller.id))
        self.lineEdit_1.setText(str(self.seller.name))
        self.lineEdit_2.setText(str(self.seller.ProductName))
        self.lineEdit_3.setText(str(self.seller.ProductPrice))
        self.pushButton.clicked.connect(self.save_data)
    def save_data(self):
        self.seller.name = self.lineEdit_1.text()
        self.seller.ProductName = self.lineEdit_2.text()
        self.seller.ProductPrice = self.lineEdit_3.text()
        self.session.commit()
        self.close()

class OrderUpdater(QDialog, Ui_Dialog1):
    def __init__(self, order_id):
        super().__init__()
        self.setupUi(self)

        self.session = create_session()
        self.order = self.session.query(Takeorder).get(order_id)
        self.label_id.setText(str(self.order.order_id))
        self.StatusOrders = ['Не выдано', 'Выдано']
        for StatusOrder in self.StatusOrders:
            self.statusBox.addItem(StatusOrder)
        self.pushButton.clicked.connect(self.save_data)
    def save_data(self):
        cb = self.statusBox.currentText()
        self.order.status = cb
        self.session.commit()
        self.close()
class SellerAdder(QDialog, Ui_Add):
    def __init__(self, session):
        super().__init__()
        self.setupUi(self)

        self.session = session
        self.seller = None
        self.label_id.setText("")
        self.lineEdit_1.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.pushButton.clicked.connect(self.save_data)

    def save_data(self):
        self.seller = Seller(
            id=self.label_id.text(),
            name=self.lineEdit_1.text(),
            ProductName=self.lineEdit_2.text(),
            ProductPrice=self.lineEdit_3.text()
        )
        self.accept()


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
    ex = TableViewer()
    ex.show()
    sys.exit(app.exec())