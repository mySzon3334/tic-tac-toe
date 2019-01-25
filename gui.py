import sys
import socket
from PyQt5 import QtCore, QtWidgets
from webbrowser import open

launch = ''  # sp_game, lmp_game, mp_game
launch_settings = []
popup_text1 = 'This function in not available yet'
popup_text2 = 'It will be added in future updates'
after_game_text = 'test-abc'
help_page = 0

auto_ip = socket.gethostbyname(socket.gethostname())


# noinspection PyArgumentList
class PopUpWindow(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Pop Up Window')

        layout = QtWidgets.QGridLayout()

        self.label1 = QtWidgets.QLabel(popup_text1)
        self.label2 = QtWidgets.QLabel(popup_text2)

        self.button = QtWidgets.QPushButton('Ok')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.label1, 0, 0, 1, 1, QtCore.Qt.AlignCenter)
        layout.addWidget(self.label2, 1, 0, 1, 1, QtCore.Qt.AlignCenter)
        layout.addWidget(self.button, 2, 0, 1, 1, QtCore.Qt.AlignCenter)

        self.setLayout(layout)


# noinspection PyArgumentList
class HelpWindow(QtWidgets.QWidget):

    def __init__(self):
        self.help_list = []
        self.help_1 = [
            'Local Multiplayer Help',
            'If you want to play together with your friend you need to be in the same local network',
            'If you are not in the same network go back to Main Menu and select Multiplayer over Internet',
            'One of you should select "Host Game", and the other one "Join Game"',
            'Player that Host should put in his own local IP address',
            'Player that Join should put in local IP address of host',
            'Both players should put in the same port number (use 50001 for default)',
        ]
        self.help2 = [
            'Worldwide Multiplayer Help',
            'If you want to play with your friend but you are not in the same local network, follow these '
            'steps:',
            '1. Download and Install "Hamachi" (click button below)',
            '2. Register and Log in to the Hamachi',
            '3. One of you should click Network > Create a new network and follow on-screen instructions',
            '4. Other one should click Network > Join a network and follow on-screen instructions',
            '5. After you connected, go back to this window and click Next',
            '6. '
        ]

        self.help_list.append(self.help_1)
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Help Window')

        layout = QtWidgets.QGridLayout()

        self.labels = []
        for p in self.help_list[help_page]:
            self.labels.append(QtWidgets.QLabel(p))

        self.button = QtWidgets.QPushButton('Ok')
        self.button.clicked.connect(self.close)

        for p in self.labels:
            layout.addWidget(p)

        if help_page == 0:
            self.button2 = QtWidgets.QPushButton('How to check my IP?')
            self.button2.clicked.connect(self.open_page)

        layout.addWidget(self.button2, len(self.labels), 0, 1, 1, QtCore.Qt.AlignCenter)
        layout.addWidget(self.button, len(self.labels) + 1, 0, 1, 1, QtCore.Qt.AlignCenter)

        self.setLayout(layout)

    def open_page(self):
        open('https://www.groovypost.com/howto/find-windows-10-device-ip-address/', new=2, autoraise=True)


# noinspection PyArgumentList,PyMethodMayBeStatic
class GameOverWindow(QtWidgets.QWidget):
    back_to_mm = QtCore.pyqtSignal()
    close_all = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Game Over')
        self.setGeometry(400, 250, 150, 100)

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel(after_game_text)

        self.back_button = QtWidgets.QPushButton('Back to Main Menu')
        self.retry_button = QtWidgets.QPushButton('Play Again')

        self.back_button.clicked.connect(self.back_to_mm.emit)
        self.retry_button.clicked.connect(self.retry)

        layout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignCenter)
        layout.addWidget(self.back_button, 1, 0, 1, 1)
        layout.addWidget(self.retry_button, 2, 0, 1, 1)

        self.setLayout(layout)

    def retry(self):
        global launch
        launch = 'mp_game'
        self.close_all.emit()


# noinspection PyArgumentList
class MultiplayerSettingsWindow(QtWidgets.QWidget):
    back_to_mm = QtCore.pyqtSignal()
    start_mp_game = QtCore.pyqtSignal()
    open_mp_help = QtCore.pyqtSignal()
    open_popup = QtCore.pyqtSignal()

    def __init__(self):
        self.clicked = 0

        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Multiplayer connection settings')
        self.setGeometry(400, 250, 250, 180)

        layout = QtWidgets.QGridLayout()

        self.main_label = QtWidgets.QLabel("Connection settings")
        # self.main_label.setStyleSheet("QLabel {background-color: red;}")
        self.ip_label = QtWidgets.QLabel('IP: ')
        self.port_label = QtWidgets.QLabel('Port: ')

        self.host_button = QtWidgets.QRadioButton("Host game")
        self.host_button.setChecked(True)
        self.join_button = QtWidgets.QRadioButton("Join game")
        self.join_button.setChecked(False)

        self.host_button.toggled.connect(self.host_game_clicked)
        self.join_button.toggled.connect(self.join_game_clicked)

        self.ip_input = QtWidgets.QLineEdit()
        self.port_input = QtWidgets.QLineEdit()
        if len(launch_settings) > 0:
            if launch_settings[0] == 'mp_game':
                self.ip_input.setText(launch_settings[2])
                self.port_input.setText(launch_settings[3])

        self.start_button = QtWidgets.QPushButton('Start')
        self.help_button = QtWidgets.QPushButton('Help')
        self.back_button = QtWidgets.QPushButton('Back')
        self.autofill_button = QtWidgets.QPushButton('Autofill IP')
        self.start_button.clicked.connect(self.send_data)
        self.help_button.clicked.connect(self.open_mp_help.emit)
        self.back_button.clicked.connect(self.back_to_mm.emit)
        self.autofill_button.clicked.connect(self.autofill_ip)

        layout.addWidget(self.main_label, 0, 1, 1, 2, QtCore.Qt.AlignCenter)
        layout.addWidget(self.host_button, 1, 1)
        layout.addWidget(self.join_button, 1, 2)
        layout.addWidget(self.ip_label, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        layout.addWidget(self.ip_input, 2, 2)
        layout.addWidget(self.port_label, 3, 1, 1, 1, QtCore.Qt.AlignRight)
        layout.addWidget(self.port_input, 3, 2)
        layout.addWidget(self.back_button, 4, 1)
        layout.addWidget(self.autofill_button, 4, 2)
        layout.addWidget(self.help_button, 5, 1)
        layout.addWidget(self.start_button, 5, 2, 1, 1)

        self.setLayout(layout)

    def host_game_clicked(self):
        self.clicked = 0

    def join_game_clicked(self):
        self.clicked = 1

    def autofill_ip(self):
        if self.clicked == 0:
            self.ip_input.setText(auto_ip)
        elif self.clicked == 1:
            global popup_text1, popup_text2
            popup_text1 = 'Ask player hosting game for his IP address'
            popup_text2 = ''
            self.open_popup.emit()

    def send_data(self):
        global launch, launch_settings
        conn_list = ['mp_game', self.clicked, self.ip_input.text(), int(self.port_input.text())]
        print('conn', conn_list)
        launch = 'mp_game'
        launch_settings = conn_list
        self.start_mp_game.emit()


class MainMenuWindow(QtWidgets.QWidget):
    sp_window_switch = QtCore.pyqtSignal()
    lmp_window_switch = QtCore.pyqtSignal()
    mp_window_switch = QtCore.pyqtSignal()
    wwmp_window_switch = QtCore.pyqtSignal()
    sett_window_switch = QtCore.pyqtSignal()
    log_sett = QtCore.pyqtSignal()

    # noinspection PyArgumentList
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Tic Tac Toe')
        self.setGeometry(400, 250, 300, 300)

        layout = QtWidgets.QGridLayout()

        self.sp_button = QtWidgets.QPushButton('Singleplayer vs. CPU (will be added in future updates)')
        self.lmp_button = QtWidgets.QPushButton('Local Multiplayer (will be added in future updates)')
        self.wlan_mp_button = QtWidgets.QPushButton('Multiplayer over Wi-Fi')
        self.wwmp_button = QtWidgets.QPushButton('Multiplayer over Internet')
        self.sett_button = QtWidgets.QPushButton('Settings')
        # self.log_sett = QtWidgets.QPushButton('Log connection debug info to file')

        self.sp_button.clicked.connect(self.sp_window_switch.emit)
        self.lmp_button.clicked.connect(self.lmp_window_switch.emit)
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
        self.open_windows = []

    def show_main(self):
        self.close_all_windows()
        self.main = MainMenuWindow()
        self.open_windows.append(self.main)

        self.main.sp_window_switch.connect(self.show_popup)
        # self.main.lmp_window_switch.connect(self.main.QtCore.QCoreApplication.instance().quit)
        self.main.lmp_window_switch.connect(self.show_popup)
        self.main.mp_window_switch.connect(self.show_mp_window)
        self.main.wwmp_window_switch.connect(self.show_popup)
        self.main.sett_window_switch.connect(self.show_popup)

        self.main.show()

    def show_sp_window(self):
        pass
        # QtCore.QCoreApplication.instance().quit

    def show_lmp_window(self):
        pass

    def show_mp_window(self):
        self.mp_sett = MultiplayerSettingsWindow()
        self.open_windows.append(self.mp_sett)

        self.mp_sett.start_mp_game.connect(self.close_all_windows)
        self.mp_sett.back_to_mm.connect(self.show_main)
        self.mp_sett.open_mp_help.connect(self.show_help)
        self.mp_sett.open_popup.connect(self.show_popup2)
        self.main.close()
        self.open_windows.remove(self.main)
        self.mp_sett.show()

    def show_go_window(self):
        self.g_over = GameOverWindow()
        self.open_windows.append(self.g_over)
        self.g_over.back_to_mm.connect(self.show_main)
        self.g_over.close_all.connect(self.close_all_windows)
        self.g_over.show()

    def show_popup(self):
        global popup_text1, popup_text2
        popup_text1 = 'This function in not available yet'
        popup_text2 = 'It will be added in future updates'
        self.pop_up = PopUpWindow()
        self.open_windows.append(self.pop_up)
        self.pop_up.show()

    def show_popup2(self):
        self.pop_up = PopUpWindow()
        self.open_windows.append(self.pop_up)
        self.pop_up.show()

    def show_help(self):
        self.help_window = HelpWindow()
        self.open_windows.append(self.help_window)
        self.help_window.show()

    def close_all_windows(self):
        for p in self.open_windows:
            p.close()


def main(open_option=1):
    app = QtWidgets.QApplication(sys.argv)
    # app.setQuitOnLastWindowClosed(False)
    controller = Controller()
    if open_option == 0:
        controller.show_popup()
    elif open_option == 1:
        controller.show_main()
    elif open_option == 2:
        controller.show_mp_window()
    app.exec_()


if __name__ == '__main__':
    main()
