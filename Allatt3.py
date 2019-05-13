# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Nisha S Gowda\Desktop\Allatt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox
import datetime
import sqlite3

class Ui_MainWindow(object):
    def mathsload(self):

        self.tableWidget.setRowCount(0)

        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str("Sl.No.")))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str("ID")))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str("Name")))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str("Date")))
        self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str("Time")))
        self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str("Attendence Status")))
        
        conn = sqlite3.connect('Face-DataBase.db')
        date = datetime.datetime.today().strftime('%d-%m-%Y')
        query = "SELECT DISTINCT Id, Roll, Name, Date, Time FROM Attendance5 WHERE Subject='Maths' AND Date=?"
        print (date)
        result = conn.execute(query, (date,))

        all_students = "SELECT * from Student"
        all_students_result = conn.execute(all_students)
        
        time = ""
        all_student_list = {}
        present_student_list = []
        tot_count = 0
        tot_pres_count = 0
        
        for row in all_students_result :
            entry = [row[0], row[1]]
            all_student_list[tot_count] = entry
            tot_count += 1

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number+1)
            time = row_data[4]
            present_student_list.append(row_data[1])
            count = 0
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number+1, colum_number, QtWidgets.QTableWidgetItem(str(data)))
                count += 1
            self.tableWidget.setItem(row_number+1, count, QtWidgets.QTableWidgetItem(str("Y")))
            tot_pres_count += 1

        extra_it = 1
        
        for key, value in all_student_list.items() :
            
            if(value[0] not in present_student_list):
                self.tableWidget.insertRow(tot_pres_count + extra_it)
                self.tableWidget.setItem(tot_pres_count + extra_it, 0, QtWidgets.QTableWidgetItem(str(tot_pres_count + extra_it)))
                self.tableWidget.setItem(tot_pres_count + extra_it, 1, QtWidgets.QTableWidgetItem(str(value[0])))
                self.tableWidget.setItem(tot_pres_count + extra_it, 2, QtWidgets.QTableWidgetItem(str(value[1])))
                self.tableWidget.setItem(tot_pres_count + extra_it, 3, QtWidgets.QTableWidgetItem(str(date)))
                self.tableWidget.setItem(tot_pres_count + extra_it, 4, QtWidgets.QTableWidgetItem(str(time)))
                self.tableWidget.setItem(tot_pres_count + extra_it, 5, QtWidgets.QTableWidgetItem(str("N")))
                extra_it += 1
            
        conn.close()
    def scienceload(self):
        self.tableWidget.setRowCount(0)

        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str("Sl.No.")))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str("ID")))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str("Name")))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str("Date")))
        self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str("Time")))
        self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str("Attendence Status")))
        
        conn = sqlite3.connect('Face-DataBase.db')
        date = datetime.datetime.today().strftime('%d-%m-%Y')
        query = "SELECT DISTINCT Id, Roll, Name, Date, Time FROM Attendance5 WHERE Subject='Science' AND Date=?"
        print (date)
        result = conn.execute(query, (date,))

        all_students = "SELECT * from Student"
        all_students_result = conn.execute(all_students)
        
        time = ""
        all_student_list = {}
        present_student_list = []
        tot_count = 0
        tot_pres_count = 0
        
        for row in all_students_result :
            entry = [row[0], row[1]]
            all_student_list[tot_count] = entry
            tot_count += 1

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number+1)
            time = row_data[4]
            present_student_list.append(row_data[1])
            count = 0
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number+1, colum_number, QtWidgets.QTableWidgetItem(str(data)))
                count += 1
            self.tableWidget.setItem(row_number+1, count, QtWidgets.QTableWidgetItem(str("Y")))
            tot_pres_count += 1

        extra_it = 1
        
        for key, value in all_student_list.items() :
            
            if(value[0] not in present_student_list):
                self.tableWidget.insertRow(tot_pres_count + extra_it)
                self.tableWidget.setItem(tot_pres_count + extra_it, 0, QtWidgets.QTableWidgetItem(str(tot_pres_count + extra_it)))
                self.tableWidget.setItem(tot_pres_count + extra_it, 1, QtWidgets.QTableWidgetItem(str(value[0])))
                self.tableWidget.setItem(tot_pres_count + extra_it, 2, QtWidgets.QTableWidgetItem(str(value[1])))
                self.tableWidget.setItem(tot_pres_count + extra_it, 3, QtWidgets.QTableWidgetItem(str(date)))
                self.tableWidget.setItem(tot_pres_count + extra_it, 4, QtWidgets.QTableWidgetItem(str(time)))
                self.tableWidget.setItem(tot_pres_count + extra_it, 5, QtWidgets.QTableWidgetItem(str("N")))
                extra_it += 1
            
        conn.close()
        
       
    def englishload(self):
        self.tableWidget.setRowCount(0)

        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str("Sl.No.")))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str("ID")))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str("Name")))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str("Date")))
        self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str("Time")))
        self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str("Attendence Status")))
        
        conn = sqlite3.connect('Face-DataBase.db')
        date = datetime.datetime.today().strftime('%d-%m-%Y')
        query = "SELECT DISTINCT Id, Roll, Name, Date, Time FROM Attendance5 WHERE Subject='English' AND Date=?"
        print (date)
        result = conn.execute(query, (date,))

        all_students = "SELECT * from Student"
        all_students_result = conn.execute(all_students)
        
        time = ""
        all_student_list = {}
        present_student_list = []
        tot_count = 0
        tot_pres_count = 0
        
        for row in all_students_result :
            entry = [row[0], row[1]]
            all_student_list[tot_count] = entry
            tot_count += 1

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number+1)
            time = row_data[4]
            present_student_list.append(row_data[1])
            count = 0
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number+1, colum_number, QtWidgets.QTableWidgetItem(str(data)))
                count += 1
            self.tableWidget.setItem(row_number+1, count, QtWidgets.QTableWidgetItem(str("Y")))
            tot_pres_count += 1

        extra_it = 1
        
        for key, value in all_student_list.items() :
            
            if(value[0] not in present_student_list):
                self.tableWidget.insertRow(tot_pres_count + extra_it)
                self.tableWidget.setItem(tot_pres_count + extra_it, 0, QtWidgets.QTableWidgetItem(str(tot_pres_count + extra_it)))
                self.tableWidget.setItem(tot_pres_count + extra_it, 1, QtWidgets.QTableWidgetItem(str(value[0])))
                self.tableWidget.setItem(tot_pres_count + extra_it, 2, QtWidgets.QTableWidgetItem(str(value[1])))
                self.tableWidget.setItem(tot_pres_count + extra_it, 3, QtWidgets.QTableWidgetItem(str(date)))
                self.tableWidget.setItem(tot_pres_count + extra_it, 4, QtWidgets.QTableWidgetItem(str(time)))
                self.tableWidget.setItem(tot_pres_count + extra_it, 5, QtWidgets.QTableWidgetItem(str("N")))
                extra_it += 1
            
        conn.close()
        
        
        
    def hindiload(self):
        self.tableWidget.setRowCount(0)

        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str("Sl.No.")))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str("ID")))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str("Name")))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str("Date")))
        self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str("Time")))
        self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str("Attendence Status")))
        
        conn = sqlite3.connect('Face-DataBase.db')
        date = datetime.datetime.today().strftime('%d-%m-%Y')
        query = "SELECT DISTINCT Id, Roll, Name, Date, Time FROM Attendance5 WHERE Subject='Hindi' AND Date=?"
        print (date)
        result = conn.execute(query, (date,))

        all_students = "SELECT * from Student"
        all_students_result = conn.execute(all_students)
        
        time = ""
        all_student_list = {}
        present_student_list = []
        tot_count = 0
        tot_pres_count = 0
        
        for row in all_students_result :
            entry = [row[0], row[1]]
            all_student_list[tot_count] = entry
            tot_count += 1

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number+1)
            time = row_data[4]
            present_student_list.append(row_data[1])
            count = 0
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number+1, colum_number, QtWidgets.QTableWidgetItem(str(data)))
                count += 1
            self.tableWidget.setItem(row_number+1, count, QtWidgets.QTableWidgetItem(str("Y")))
            tot_pres_count += 1

        extra_it = 1
        
        for key, value in all_student_list.items() :
            
            if(value[0] not in present_student_list):
                self.tableWidget.insertRow(tot_pres_count + extra_it)
                print(tot_pres_count + extra_it + 1)
                print(value[0])
                self.tableWidget.setItem(tot_pres_count + extra_it, 0, QtWidgets.QTableWidgetItem(str(tot_pres_count + extra_it)))
                self.tableWidget.setItem(tot_pres_count + extra_it, 1, QtWidgets.QTableWidgetItem(str(value[0])))
                self.tableWidget.setItem(tot_pres_count + extra_it, 2, QtWidgets.QTableWidgetItem(str(value[1])))
                self.tableWidget.setItem(tot_pres_count + extra_it, 3, QtWidgets.QTableWidgetItem(str(date)))
                self.tableWidget.setItem(tot_pres_count + extra_it, 4, QtWidgets.QTableWidgetItem(str(time)))
                self.tableWidget.setItem(tot_pres_count + extra_it, 5, QtWidgets.QTableWidgetItem(str("N")))
                extra_it += 1
            
        conn.close()
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("View Attendance")
        MainWindow.resize(875, 623)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 480, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.mathsload)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 480, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.scienceload)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 480, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.englishload)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 480, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.hindiload)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 841, 431))
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Maths"))
        self.pushButton_2.setText(_translate("MainWindow", "Science"))
        self.pushButton_3.setText(_translate("MainWindow", "English"))
        self.pushButton_4.setText(_translate("MainWindow", "Hindi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

