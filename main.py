from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QDoubleValidator, QValidator
import sys
import mysql.connector
import pyautogui
import string
import re
import random

try:
    with open('data.log') as f:
        baris = list(f)
        hostData = baris[0].strip('\n')
        userData = baris[1].strip('\n')
        passData = baris[2].strip('\n')
        dbData = baris[3].strip('\n')
    f.close()
except:
    pyautogui.alert("File data.log tidak di temukan !!","Peringatan")

try:
    serverData = mysql.connector.connect(
    host=hostData,
    user=userData,
    password=passData,
    database=dbData
)
except mysql.connector.errors.ProgrammingError:
    pyautogui.alert("Gagal mendapatkan basis data !","Peringatan")
except mysql.connector.errors.InterfaceError:
    pyautogui.alert("Koneksi gagal !","Peringatan")

cursor = serverData.cursor()
cursor.execute("SELECT * FROM db_produk")
dataBarang = cursor.fetchall()
hasilKodeBarang = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 541)
        MainWindow.setMinimumSize(QtCore.QSize(969, 541))
        MainWindow.setMaximumSize(QtCore.QSize(969, 541))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.namaBarang = QtWidgets.QLineEdit(self.centralwidget)
        self.namaBarang.setGeometry(QtCore.QRect(30, 90, 351, 31))
        self.namaBarang.setStyleSheet("font: 75 12pt \"Arial\";")
        self.namaBarang.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.namaBarang.setObjectName("namaBarang")
        self.stokBarang = QtWidgets.QLineEdit(self.centralwidget)
        self.stokBarang.setGeometry(QtCore.QRect(30, 160, 351, 31))
        self.stokBarang.setStyleSheet("font: 75 12pt \"Arial\";")
        self.stokBarang.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.stokBarang.setObjectName("stokBarang")
        self.hargaBarang = QtWidgets.QLineEdit(self.centralwidget)
        self.hargaBarang.setGeometry(QtCore.QRect(30, 230, 351, 31))
        self.hargaBarang.setStyleSheet("font: 75 12pt \"Arial\";")
        self.hargaBarang.setObjectName("hargaBarang")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 300, 351, 111))
        self.textEdit.setStyleSheet("font: 75 12pt \"Arial\";")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 111, 31))
        self.label.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 111, 31))
        self.label_2.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 111, 31))
        self.label_3.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 141, 31))
        self.label_4.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 430, 201, 51))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(460, 430, 431, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(400, 70, 541, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 10, 541, 41))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet("font: 75 18pt \"Arial\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 969, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Maulid"))
        self.namaBarang.setPlaceholderText(_translate("MainWindow", "Nama Barang"))
        self.stokBarang.setPlaceholderText(_translate("MainWindow", "Stok Barang"))
        self.hargaBarang.setPlaceholderText(_translate("MainWindow", "Harga Barang"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Deskripsi Barang ...."))
        self.label.setText(_translate("MainWindow", "Nama Barang :"))
        self.label_2.setText(_translate("MainWindow", "Stok Barang :"))
        self.label_3.setText(_translate("MainWindow", "Harga Barang :"))
        self.label_4.setText(_translate("MainWindow", "Deskripsi Barang :"))
        self.pushButton.setText(_translate("MainWindow", "Tambah Data"))
        self.pushButton.clicked.connect(self.tambahDataBarang)
        self.pushButton_3.setText(_translate("MainWindow", "Edit Data"))
        self.pushButton_3.clicked.connect(self.updateDataBarang)
        self.pushButton_4.setText(_translate("MainWindow", "Ekstrak Data"))
        self.pushButton_4.clicked.connect(self.loadDataBarang)
        self.pushButton_2.setText(_translate("MainWindow", "Hapus Data"))
        self.pushButton_2.clicked.connect(self.hapusDataBarang)
        self.tableWidget.setHorizontalHeaderLabels(("Kode Barang","Nama Barang", "Stok Barang", "Harga Barang","Deskripsi Barang"))
        indexBaris = 0
        self.tableWidget.setRowCount(dataBarang.__len__())
        for barang in dataBarang:
            hargaBarang = f"Rp.{barang[4]}"
            self.tableWidget.setItem(indexBaris,0,QTableWidgetItem(str(barang[1])))
            self.tableWidget.setItem(indexBaris,1,QTableWidgetItem(str(barang[2])))
            self.tableWidget.setItem(indexBaris,2,QTableWidgetItem(str(barang[3])))
            self.tableWidget.setItem(indexBaris,3,QTableWidgetItem(str(f"Rp.{barang[4]}")))
            self.tableWidget.setItem(indexBaris,4,QTableWidgetItem(str(barang[5])))
            indexBaris += 1
        self.label_5.setText(_translate("MainWindow", "Pengelola DataBase Perusahaan "))
        self.tableWidget.itemSelectionChanged.connect(self.pilihDataBarang)

    def aturanValidasi(self):
        aturanValidasi = QDoubleValidator(0,sys.maxsize,0)
        return aturanValidasi
      
    def kodeBarang(self):
        for barang in dataBarang:
            hasilKodeBarang.append(barang[1])
        return hasilKodeBarang   

    def tambahDataBarang(self):
        kodeBarang = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for _ in range(9))
        namaBarang = self.namaBarang.text()
        stokBarang = self.stokBarang.text()
        hargaBarang = self.hargaBarang.text()
        deskripsiBarang = self.textEdit.toPlainText()
        #if aturanValidasi.validate(stokBarang,14)[0] == QValidator.Acceptable:
            #print("oke")
        #else:
            #print("gagal")
        if not namaBarang or not deskripsiBarang:
            pyautogui.alert("Input pada data tidak boleh kosong !","Peringatan")
        elif len(namaBarang.strip()) == 0 or len(deskripsiBarang.strip()) == 0 or len(stokBarang.strip()) == 0 or len(hargaBarang.strip()) == 0:
            pyautogui.alert("Input pada data tidak boleh kosong !","Peringatan")
        elif not self.aturanValidasi().validate(stokBarang,14)[0] == QValidator.Acceptable or not self.aturanValidasi().validate(hargaBarang,14)[0] == QValidator.Acceptable:
            pyautogui.alert("Input harus dalam bentuk angka !","Peringatan")
        else:
            hasilKodeBarang.append(kodeBarang)
            cursor.execute("INSERT INTO db_produk (id,kodeBarang, namaBarang, hargaBarang, stokBarang, deskripsiBarang) VALUES (%s ,%s, %s, %s, %s, %s)",("", kodeBarang, namaBarang, hargaBarang, stokBarang, deskripsiBarang))
            serverData.commit()
            indexBaris = self.tableWidget.rowCount()
            indexgetData = 0
            self.tableWidget.insertRow(indexBaris)
            for barangTambahan in dataBarang:
                self.tableWidget.setItem(indexBaris , 0, QTableWidgetItem(kodeBarang))
                self.tableWidget.setItem(indexBaris , 1, QTableWidgetItem(namaBarang))
                self.tableWidget.setItem(indexBaris , 2, QTableWidgetItem(stokBarang))
                self.tableWidget.setItem(indexBaris , 3, QTableWidgetItem(f"Rp.{hargaBarang}"))
                self.tableWidget.setItem(indexBaris , 4, QTableWidgetItem(deskripsiBarang))
                indexBaris +=1
            if cursor.rowcount > 0:
                self.namaBarang.clear()
                self.hargaBarang.clear()
                self.stokBarang.clear()
                self.textEdit.clear()
                pyautogui.alert("Data Telah Berhasil Di Tambahkan !","Status")
            else:
                pyautogui.alert("Data Telah Gagal Di Tambahkan !","Status")
    
    def pilihDataBarang(self):
        items = self.tableWidget.selectedItems()
        for i in range(len(items)):
            return items[i].text()
           
    def hapusDataBarang(self):
        print(self.pilihDataBarang())
        if self.tableWidget.rowCount() > 0:
            if self.pilihDataBarang() not in self.kodeBarang():
                pyautogui.alert("Kode barang tidak valid !","Peringatan")
            else:
                itemHapus = self.pilihDataBarang()
                queryHapus = f"DELETE FROM db_produk WHERE kodeBarang = '{itemHapus}'"
                cursor.execute(queryHapus)
                serverData.commit()
                itemData = self.tableWidget.currentRow()
                self.tableWidget.removeRow(itemData)
                pyautogui.alert(f"Data dengan kode barang : {itemHapus} telah dihapus !","Status")
        else:
            pyautogui.alert("Seluruh data pada database telah di hapus !", "Peringatan")
            
    def loadDataBarang(self):
        barisData = self.tableWidget.currentRow()
        namaUbah =  self.tableWidget.item(barisData,1).text()
        stokUbah = self.tableWidget.item(barisData,2).text()
        hargaUbah = self.tableWidget.item(barisData,3).text()
        deskripsiUbah = self.tableWidget.item(barisData,4).text()
        self.namaBarang.setText(namaUbah)
        self.stokBarang.setText(stokUbah)
        self.hargaBarang.setText(hargaUbah.split(".")[1])
        self.textEdit.setText(deskripsiUbah)
        
    def updateDataBarang(self):
        namaBarang = self.namaBarang.text()
        stokBarang = self.stokBarang.text()
        hargaBarang = self.hargaBarang.text()
        deskripsiBarang = self.textEdit.toPlainText()
        barisData = self.tableWidget.currentRow()
        namaUbah =  self.tableWidget.item(barisData,1).text()
        stokUbah = self.tableWidget.item(barisData,2).text()
        hargaUbah = self.tableWidget.item(barisData,3).text()
        deskripsiUbah = self.tableWidget.item(barisData,4).text()
        if not namaBarang or not deskripsiBarang:
            pyautogui.alert("Input pada data tidak boleh kosong !","Peringatan")
        elif len(namaBarang.strip()) == 0 or len(deskripsiBarang.strip()) == 0 or len(stokBarang.strip()) == 0 or len(hargaBarang.strip()) == 0:
            pyautogui.alert("Input pada data tidak boleh kosong !","Peringatan")
        elif not self.aturanValidasi().validate(stokBarang,14)[0] == QValidator.Acceptable or not self.aturanValidasi().validate(hargaBarang,14)[0] == QValidator.Acceptable:
            pyautogui.alert("Input harus dalam bentuk angka !","Peringatan")
        else:
            updateData = f"UPDATE `db_produk` SET `namaBarang`=%s, `stokBarang`=%s, `hargaBarang`=%s, `deskripsiBarang`=%s WHERE `kodeBarang`='{self.tableWidget.item(barisData,0).text()}'"
            value = (namaBarang, stokBarang, hargaBarang, deskripsiBarang)
            cursor.execute(updateData, value)
            serverData.commit()           
            self.tableWidget.setItem(barisData , 1, QTableWidgetItem(namaBarang))
            self.tableWidget.setItem(barisData , 2, QTableWidgetItem(stokBarang))
            self.tableWidget.setItem(barisData , 3, QTableWidgetItem(f"Rp.{hargaBarang}"))
            self.tableWidget.setItem(barisData , 4, QTableWidgetItem(deskripsiBarang))
            serverData.commit()
            
            self.namaBarang.clear()
            self.hargaBarang.clear()
            self.stokBarang.clear()
            self.textEdit.clear()

            pyautogui.alert("Data berhasil di edit !","Status")
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
