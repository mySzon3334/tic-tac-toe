import sys
from PyQt5 import QtCore, QtWidgets

launch = ''  # sp_game_easy, sp_game_med, sp_game_hard lmp_game, mp_game


class MainWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Menu Window')

        layout = QtWidgets.QGridLayout()

        self.line_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.line_edit)

        self.button = QtWidgets.QPushButton('Switch Window')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def switch(self):
        print(self.line_edit.text())
        self.switch_window.emit(self.line_edit.text())


class MultiplayerSettingsWindow(QtWidgets.QWidget):
    back_to_mainmenu = QtCore.pyqtSignal()

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Multiplayer connection settings')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel("test")
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.button)

        self.setLayout(layout)


class MainMenuWindow(QtWidgets.QWidget):
    sp_window_switch = QtCore.pyqtSignal()
    lmp_window_switch = QtCore.pyqtSignal()
    mp_window_switch = QtCore.pyqtSignal()
    wwmp_window_switch = QtCore.pyqtSignal()
    sett_window_switch = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Tic Tac Toe')

        layout = QtWidgets.QGridLayout()

        self.sp_button = QtWidgets.QPushButton('Singleplayer vs. CPU (will be added in future updates)')
        self.lmp_button = QtWidgets.QPushButton('Local Multiplayer (will be added in future updates)')
        self.wlan_mp_button = QtWidgets.QPushButton('Multiplayer over Wi-Fi')
        self.wwmp_button = QtWidgets.QPushButton('Multiplayer over Internet')
        self.sett_button = QtWidgets.QPushButton('Settings')

        self.sp_button.clicked.connect(self.sp_window_switch.emit)
        self.lmp_button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.wlan_mp_button.clicked.connect(self.mp_window_switch.emit)
        self.wwmp_button.clicked.connect(self.wwmp_window_switch.emit)
        self.sett_button.clicked.connect(self.sett_window_switch.emit)

        layout.addWidget(self.sp_button)
        layout.addWidget(self.lmp_button)
        layout.addWidget(self.wlan_mp_button)
        layout.addWidget(self.wwmp_button)
        layout.addWidget(self.sett_button)

        self.setLayout(layout)
    """
    def close(self):
        QtCore.QCoreApplication.instance().quit

    def test(self):
        self.switch_window2.emit()"""


# noinspection PyAttributeOutsideInit
class Controller:
    # QtCore.QCoreApplication.instance().quit

    def __init__(self):
        pass

    def show_main(self):
        self.main = MainMenuWindow()

        self.main.sp_window_switch.connect(self.show_sp_window)
        # self.main.lmp_window_switch.connect(self.main.QtCore.QCoreApplication.instance().quit)
        self.main.mp_window_switch.connect(self.show_mp_window)
        # self.main.wwmp_window_switch.connect(self.show_main)
        # self.main.sett_window_switch.connect(self.show_main)

        self.main.show()

    def show_sp_window(self):
        pass
        # QtCore.QCoreApplication.instance().quit

    def show_lmp_window(self):
        pass

    def show_mp_window(self):
        global launch
        launch = 'mp_game'
        self.main.close()
        print('launch set')
        # self.mp_window = MultiplayerWindow()


def main():
    app = QtWidgets.QApplication(sys.argv)
    # app.setQuitOnLastWindowClosed(False)
    controller = Controller()
    controller.show_main()
    app.exec_()


if __name__ == '__main__':
    main()
    print('koniec')
