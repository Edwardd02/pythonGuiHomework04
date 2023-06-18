# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exercise07.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import Exercise03
import Exercise05
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

import mysql.connector

#############################################################
#                                                           #
#                       UI Generation                       #
#                                                           #
#############################################################

from PyQt5 import QtCore, QtGui, QtWidgets

categories = []
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.twtMain = QtWidgets.QTabWidget(self.centralwidget)
        self.twtMain.setGeometry(QtCore.QRect(10, 0, 900, 541))
        self.twtMain.setObjectName("twtMain")
        self.tabCategories = QtWidgets.QWidget()
        self.tabCategories.setObjectName("tabCategories")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tabCategories)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 875, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tblCategories = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tblCategories.setObjectName("tblCategories")
        self.tblCategories.setColumnCount(2)
        self.tblCategories.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblCategories.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCategories.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.tblCategories)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnNewCategories = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnNewCategories.setObjectName("btnNewCategories")
        self.verticalLayout_4.addWidget(self.btnNewCategories)
        self.btnEditCategories = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnEditCategories.setObjectName("btnEditCategories")
        self.verticalLayout_4.addWidget(self.btnEditCategories)
        self.btnDeleteCategories = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnDeleteCategories.setObjectName("btnDeleteCategories")
        self.verticalLayout_4.addWidget(self.btnDeleteCategories)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.twtMain.addTab(self.tabCategories, "")
        self.tabExpenses = QtWidgets.QWidget()
        self.tabExpenses.setObjectName("tabExpenses")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tabExpenses)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 875, 501))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tblExpenses = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.tblExpenses.setObjectName("tblExpenses")
        self.tblExpenses.setColumnCount(6)
        self.tblExpenses.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblExpenses.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblExpenses.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblExpenses.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblExpenses.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblExpenses.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblExpenses.setHorizontalHeaderItem(5, item)
        self.horizontalLayout_2.addWidget(self.tblExpenses)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btnNewExpenses = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnNewExpenses.setObjectName("btnNewExpenses")
        self.verticalLayout_5.addWidget(self.btnNewExpenses)
        self.btnEditExpenses = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnEditExpenses.setObjectName("btnEditExpenses")
        self.verticalLayout_5.addWidget(self.btnEditExpenses)
        self.btnDeleteExpenses = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnDeleteExpenses.setObjectName("btnDeleteExpenses")
        self.verticalLayout_5.addWidget(self.btnDeleteExpenses)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.twtMain.addTab(self.tabExpenses, "")
        self.tabReports = QtWidgets.QWidget()
        self.tabReports.setObjectName("tabReports")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tabReports)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 875, 501))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tblReports = QtWidgets.QTableWidget(self.horizontalLayoutWidget_3)
        self.tblReports.setObjectName("tblReports")
        self.tblReports.setColumnCount(2)
        self.tblReports.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblReports.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReports.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_3.addWidget(self.tblReports)
        self.twtMain.addTab(self.tabReports, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.twtMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Update UI Here
        self.initialSetup()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tblCategories.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category ID"))
        item = self.tblCategories.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category"))
        self.btnNewCategories.setText(_translate("MainWindow", "New"))
        self.btnEditCategories.setText(_translate("MainWindow", "Edit"))
        self.btnDeleteCategories.setText(_translate("MainWindow", "Delete"))
        self.twtMain.setTabText(self.twtMain.indexOf(self.tabCategories), _translate("MainWindow", "Categories"))
        item = self.tblExpenses.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Expense ID"))
        item = self.tblExpenses.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tblExpenses.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Expense Date"))
        item = self.tblExpenses.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Expense"))
        item = self.tblExpenses.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.tblExpenses.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Notes"))
        self.btnNewExpenses.setText(_translate("MainWindow", "New"))
        self.btnEditExpenses.setText(_translate("MainWindow", "Edit"))
        self.btnDeleteExpenses.setText(_translate("MainWindow", "Delete"))
        self.twtMain.setTabText(self.twtMain.indexOf(self.tabExpenses), _translate("MainWindow", "Expenses"))
        item = self.tblReports.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tblReports.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Total Expenses"))
        self.twtMain.setTabText(self.twtMain.indexOf(self.tabReports), _translate("MainWindow", "Reports"))

    ##################### End UI Generation ###################

    def initialSetup(self):
        self.setupEvents()
        self.setupDatabase()

    #############################################################
    #                                                           #
    #                          Events                           #
    #                                                           #
    #############################################################
    def setupEvents(self):
        self.connectButtonClicked(self.btnNewCategories, self.btnNewCategories_clicked)
        self.connectButtonClicked(self.btnNewExpenses, self.btnNewExpenses_clicked)
        self.connectButtonClicked(self.btnEditCategories, self.btnEditCategories_clicked)
        self.connectButtonClicked(self.btnEditExpenses, self.btnEditExpenses_clicked)
        self.connectButtonClicked(self.btnDeleteCategories, self.btnDeleteCategories_clicked)
        self.connectButtonClicked(self.btnDeleteExpenses, self.btnDeleteExpenses_clicked)

    def connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)


    # Functions for buttons in categories
    def btnNewCategories_clicked(self):
        listValues = self.openDialog(Exercise03, None)

        if listValues is not None:
            self.insertCategories(listValues)
            self.refreshCategories()

    def btnEditCategories_clicked(self):
        currentRow = self.tblCategories.currentRow()

        if currentRow == -1:
            QMessageBox.warning(None, "Select Row", "Please select row first")
            return

        listValues = []
        listValues.append(self.tblCategories.item(currentRow, 0).text())
        listValues.append(self.tblCategories.item(currentRow, 1).text())

        listValues = self.openDialog(Exercise03, listValues)
        if listValues is not None:

            self.updateCategories(listValues)
            self.refreshCategories()

    def btnDeleteCategories_clicked(self):
        # Delete selected row
        currentRow = self.tblCategories.currentRow()

        if currentRow == -1:  # No row selected
            QMessageBox.warning(None, "Select Row", "Please select row first")
            return

        answer = QMessageBox.question(
            None,
            "Delete row?",
            "Are you sure you want to delete this row?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        # Check if user clicked Yes button
        if answer == QMessageBox.StandardButton.Yes:
            ID = self.tblCategories.item(currentRow, 0).text()

            # Delete from database
            self.deleteCategories(ID)

            # Requery
            self.refreshCategories()

    def btnNewExpenses_clicked(self):
        listValues = self.openDialog(Exercise05, None)

        if listValues is not None:
            self.insertExpenses(listValues)
            self.refreshExpenses()


    def btnEditExpenses_clicked(self):
        currentRow = self.tblExpenses.currentRow()

        if currentRow == -1:
            QMessageBox.warning(None, "Select Row", "Please select row first")
            return

        listValues = []
        listValues.append(self.tblExpenses.item(currentRow, 0).text())
        listValues.append(self.tblExpenses.item(currentRow, 1).text())
        listValues.append(self.tblExpenses.item(currentRow, 2).text())
        listValues.append(self.tblExpenses.item(currentRow, 3).text())
        listValues.append(self.tblExpenses.item(currentRow, 4).text())
        listValues.append(self.tblExpenses.item(currentRow, 5).text())

        listValues = self.openDialog(Exercise05, listValues)

        if listValues is not None:
            self.updateExpenses(listValues)
            self.refreshExpenses()

    def btnDeleteExpenses_clicked(self):
        # Delete selected row
        currentRow = self.tblExpenses.currentRow()

        if currentRow == -1:  # No row selected
            QMessageBox.warning(None, "Select Row", "Please select row first")
            return

        answer = QMessageBox.question(
            None,
            "Delete row?",
            "Are you sure you want to delete this row?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        # Check if user clicked Yes button
        if answer == QMessageBox.StandardButton.Yes:
            ID = self.tblExpenses.item(currentRow, 0).text()

            # Delete from database
            self.deleteExpenses(ID)

            # Requery
            self.refreshExpenses()

    def refreshCategoriesComboBox(self):
        exercise05_ui = Exercise05.Ui_Dialog()
        exercise05_ui.setupComboBox(categories)

    def openDialog(self, dialogClass, listValues):
        Dialog = QtWidgets.QDialog()
        form = dialogClass.Ui_Dialog()
        form.setupUi(Dialog, listValues)
        result = Dialog.exec_()

        if result == 1:
            return form.getValues()

        return None
    #############################################################
    #                                                           #
    #                          Database                         #
    #                                                           #
    #############################################################

    def setupDatabase(self):
        # Establishes the connection and refreshes category and expense data
        self.connect()
        self.refreshCategories()
        self.refreshExpenses()
        self.refreshReports()

    def connect(self):
        # Connects to the database
        self.cnx = mysql.connector.connect(user="root",
                                           password="yourOwnPassword",
                                           host="127.0.0.1",
                                           database="homework04")

    def execute_query(self, query, values=None):
        # Creates a cursor, executes a query, and then returns the cursor
        cursor = self.cnx.cursor()
        cursor.execute(query, values)
        return cursor

    def commit_and_close(self, cursor):
        # Commits any changes and closes the cursor
        self.cnx.commit()
        cursor.close()

    def refreshCategories(self):
        self.refreshReports()
        # Refreshes the categories view by clearing the table and inserting the new data
        self.tblCategories.setRowCount(0)

        cursor = self.execute_query("Select * From Categories")

        for (category_ID, category) in cursor:  # Field names in DB
            rowCount = self.tblCategories.rowCount()
            self.tblCategories.insertRow(rowCount)
            self.tblCategories.setItem(rowCount, 0, QTableWidgetItem(str(category_ID)))
            self.tblCategories.setItem(rowCount, 1, QTableWidgetItem(category))

        self.commit_and_close(cursor)

    def insertCategories(self, a_listValues):
        # Inserts a new category into the database
        cursor = self.execute_query("Insert Into Categories (category) Values (%s)", (a_listValues[1],))
        self.commit_and_close(cursor)

    def updateCategories(self, a_listValues):
        # Updates an existing category in the database
        cursor = self.execute_query("Update Categories Set category = %s Where category_ID = %s",
                                    [a_listValues[1], a_listValues[0]])
        self.commit_and_close(cursor)

    def deleteCategories(self, a_ID):
        # Deletes a category from the database
        cursor = self.execute_query("Delete from Categories Where category_ID = %s", [a_ID])
        self.commit_and_close(cursor)

    def refreshExpenses(self):
        self.refreshReports()
        # Refreshes the expenses view by clearing the table and inserting the new data
        self.tblExpenses.setRowCount(0)

        cursor = self.execute_query("Select expense_ID, category, expense_date, expense, amount, notes "
                                    "from Expenses natural join Categories"
                                    " order by expense_ID")

        for (expense_ID, category, expense_date, expense, amount, notes) in cursor:
            rowCount = self.tblExpenses.rowCount()
            self.tblExpenses.insertRow(rowCount)
            self.tblExpenses.setItem(rowCount, 0, QTableWidgetItem(str(expense_ID)))
            self.tblExpenses.setItem(rowCount, 1, QTableWidgetItem(str(category)))
            self.tblExpenses.setItem(rowCount, 2, QTableWidgetItem(str(expense_date)))
            self.tblExpenses.setItem(rowCount, 3, QTableWidgetItem(expense))
            self.tblExpenses.setItem(rowCount, 4, QTableWidgetItem(str(amount)))
            self.tblExpenses.setItem(rowCount, 5, QTableWidgetItem(notes))

        self.commit_and_close(cursor)

    def insertExpenses(self, a_listValues):
        # Inserts a new expense into the database
        category_id = self.getCategoryID(a_listValues)
        cursor = self.execute_query(
            "Insert Into Expenses (category_ID, expense_date, expense, amount, notes) Values (%s, %s, %s, %s, %s )",
            (category_id, a_listValues[2], a_listValues[3], a_listValues[4], a_listValues[5]))
        self.commit_and_close(cursor)

    def updateExpenses(self, a_listValues):
        # Updates an existing expense in the database
        category_id = self.getCategoryID(a_listValues)
        cursor = self.execute_query(
            "Update Expenses Set category_ID = %s, expense_date = %s, expense = %s, amount = %s, notes = %s Where expense_ID = %s",
            (category_id, a_listValues[2], a_listValues[3], a_listValues[4], a_listValues[5], a_listValues[0]))
        self.commit_and_close(cursor)

    def getCategoryID(self, a_listValues):
        # Returns the ID of a category based on its name
        cursor = self.execute_query("Select category_ID From Categories Where category = %s", (a_listValues[1],))
        result = cursor.fetchone()
        category_id = result[0]
        cursor.close()

        return category_id

    def deleteExpenses(self, a_ID):
        # Deletes an expense from the database
        cursor = self.execute_query("Delete from Expenses Where expense_ID = %s", [a_ID])
        self.commit_and_close(cursor)

    def refreshReports(self):
        # Refreshes the categories view by clearing the table and inserting the new data
        self.tblReports.setRowCount(0)

        cursor = self.execute_query("Select category, sum(amount) amount "
                                    "from Expenses natural join Categories"
                                    " group by category")

        for (category, amount) in cursor:  # Field names in DB
            rowCount = self.tblReports.rowCount()
            self.tblReports.insertRow(rowCount)
            self.tblReports.setItem(rowCount, 0, QTableWidgetItem(category))
            self.tblReports.setItem(rowCount, 1, QTableWidgetItem(str(amount)))

        self.commit_and_close(cursor)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
