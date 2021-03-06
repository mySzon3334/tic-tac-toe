from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

window = 'mainmenu'


def open_window():
    print('test')
    Ui_MainMenuWindow.open_window(Ui_MainMenuWindow)


# noinspection PyAttributeOutsideInit,PyArgumentList,PyMethodMayBeStatic
class Ui_MainMenuWindow(object):
    def setupUi(self, MainMenuWindow):
        MainMenuWindow.setObjectName("MainMenuWindow")
        MainMenuWindow.resize(217, 367)
        self.centralwidget = QtWidgets.QWidget(MainMenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.sp_button = QtWidgets.QPushButton(self.centralwidget)
        self.sp_button.setObjectName("sp_button")
        self.verticalLayout.addWidget(self.sp_button)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.lmp_button = QtWidgets.QPushButton(self.centralwidget)
        self.lmp_button.setObjectName("lmp_button")
        self.verticalLayout.addWidget(self.lmp_button)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.wlan_mp_button = QtWidgets.QPushButton(self.centralwidget)
        self.wlan_mp_button.setObjectName("wlan_mp_button")
        self.verticalLayout.addWidget(self.wlan_mp_button)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.ww_mp_button = QtWidgets.QPushButton(self.centralwidget)
        self.ww_mp_button.setObjectName("ww_mp_button")
        self.verticalLayout.addWidget(self.ww_mp_button)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.sett_button = QtWidgets.QPushButton(self.centralwidget)
        self.sett_button.setObjectName("sett_button")
        self.verticalLayout.addWidget(self.sett_button)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainMenuWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

        self.sp_button.clicked.connect(self.close_test)
        self.lmp_button.clicked.connect(self.lmp_button_pressed)
        self.wlan_mp_button.clicked.connect(self.wlan_mp_button_pressed)
        self.ww_mp_button.clicked.connect(self.ww_mp_button_pressed)
        # self.sett_button.clicked.connect(self.sett_button_pressed)
        self.sett_button.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def retranslateUi(self, MainMenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "MainWindow"))
        self.label.setText(_translate("MainMenuWindow", "Tic Tac Toe"))
        self.label_2.setText(_translate("MainMenuWindow", "Main Menu"))
        self.sp_button.setText(_translate("MainMenuWindow", "Single Player vs. CPU (will be added in future updates)"))
        self.lmp_button.setText(_translate("MainMenuWindow", "Local Multi Player (will be added in future updates)"))
        self.wlan_mp_button.setText(_translate("MainMenuWindow", "Multiplayer over Wi-Fi"))
        self.ww_mp_button.setText(_translate("MainMenuWindow", "Multiplayer over Internet"))
        self.sett_button.setText(_translate("MainMenuWindow", "Settings"))

    def close_test(self):
        print('hello')
        sys.exit()

    def sp_button_pressed(self):
        global window
        window = 'sp_menu'
        print('sp')

    def lmp_button_pressed(self):
        global window
        window = 'lmp_start'

    def wlan_mp_button_pressed(self):
        global window
        window = 'mp_menu'

    def ww_mp_button_pressed(self):
        global window
        window = 'wwmp_info'

    def sett_button_pressed(self):
        global window
        window = 'sett_menu'

    def open_window(self):
        app = QtWidgets.QApplication(sys.argv)
        MainMenuWindow = QtWidgets.QMainWindow()
        ui = Ui_MainMenuWindow()
        ui.setupUi(MainMenuWindow)
        print('show')
        MainMenuWindow.show()
        app.exec_()
        print('done')


open_window()
