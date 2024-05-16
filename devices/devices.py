'''
  Project       : Spectrometer
  Author        : chumadan
  Contacts      : dkc1@tpu.ru
  Workfile      : devices.py
  Description   : Classes describing various objects used for multi-channel spectrometer
'''
import sys
import os

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, 
    QAction, QLabel, QMessageBox, 
    QTreeWidget, QSpinBox, QFileDialog, 
    QPushButton, QWidget, QVBoxLayout, QGroupBox,
    QLineEdit, QGridLayout, QTableWidget,
    QListWidget, QTableWidgetItem, QComboBox,
    QHBoxLayout, QTabWidget, QToolBar, QCheckBox, QSpacerItem, QDoubleSpinBox
)
from PyQt5.QtCore import (
    pyqtSignal, QThread, 
    QThreadPool, QSettings, 
    QEvent, Qt, pyqtSlot
)
from PyQt5.QtGui import (
    QPixmap, QFont, QIcon
)

def conv_v_to_adc(val):
    adc_v_pp = 2
    adc_bitwidth = 2**14

    #self.adc_step = 1/8192*1000

    res = val * adc_bitwidth / adc_v_pp

    return int(res)

def conv_adc_to_v(val):
    adc_v_pp = 2
    adc_bitwidth = 2**14        
    res = adc_v_pp * val / adc_bitwidth

    return res


#Roles: master/slave
class RolesList(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItems(["Master", "Slave"])


class ChannelWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
        #calculates value of threshold in adc ticks
        self.lne_threshold.valueChanged.connect(lambda: self.lbl_threshold_ticks.setText(str(conv_v_to_adc(self.lne_threshold.value()))))
        self.lne_bline.valueChanged.connect(lambda: self.lbl_bline_ticks.setText(str(conv_v_to_adc(self.lne_bline.value()))))


    def setupUI(self):
        self.channel_id = QLabel("")
        self.isChannelActive = QCheckBox("Channel is active")
        self.isChannelActive.setChecked(False)

        self.grid_chProps = QGridLayout()

        #threshold settings
        self.lbl_threshold_capt = QLabel("Threshold value")
        self.lne_threshold = QDoubleSpinBox()
        self.lne_threshold.setSingleStep(1e-3)
        self.lne_threshold.setDecimals(3)
        self.lbl_threshold_ticks = QLabel("0")
        self.chk_hyst = QCheckBox("Enable hystheresis")
        #gate settings
        self.lbl_gate_start = QLabel("Gate start, bins")
        self.lne_gate_start = QSpinBox()
        self.lne_gate_start.setRange(0,255)
        self.lbl_gate_end = QLabel("Gate end, bins")
        self.lne_gate_end = QSpinBox()
        self.lne_gate_end.setRange(0,255)
        self.lbl_movavg = QLabel("Moving average, bins")
        self.lne_gate_movavg = QSpinBox()
        self.lne_gate_movavg.setRange(0,255)
        #baseline settings
        self.lbl_bline = QLabel("Baseline value")
        self.lne_bline = QDoubleSpinBox()
        self.lne_bline.setSingleStep(1e-3)
        self.lne_bline.setDecimals(3)
        self.lbl_bline_ticks = QLabel("0")
        #positioning in layout
        self.grid_chProps.addWidget(self.channel_id, 0, 0, 1, 1)
        self.grid_chProps.addWidget(self.isChannelActive, 0, 1, 1, 1)

        self.grid_chProps.addWidget(self.lbl_threshold_capt, 1, 0, 1, 1)
        self.grid_chProps.addWidget(self.lne_threshold, 1, 1, 1, 1)
        self.grid_chProps.addWidget(self.lbl_threshold_ticks, 1, 2, 1, 1)
        self.grid_chProps.addWidget(self.chk_hyst, 2, 0, 1, 1)

        self.grid_chProps.addWidget(self.lbl_gate_start, 3, 0, 1, 1)
        self.grid_chProps.addWidget(self.lne_gate_start, 3, 1, 1, 1)
        self.grid_chProps.addWidget(self.lbl_gate_end, 4, 0, 1, 1)
        self.grid_chProps.addWidget(self.lne_gate_end, 4, 1, 1, 1)

        self.grid_chProps.addWidget(self.lbl_movavg, 5, 0, 1, 1)
        self.grid_chProps.addWidget(self.lne_gate_movavg, 5, 1, 1, 1)
        self.grid_chProps.addWidget(self.lbl_bline, 6, 0, 1, 1)
        self.grid_chProps.addWidget(self.lne_bline, 6, 1, 1, 1)
        self.grid_chProps.addWidget(self.lbl_bline_ticks, 6, 2, 1, 1)

        layout = QVBoxLayout(self)
        layout.addLayout(self.grid_chProps)
        layout.addStretch()

        self.setLayout(layout)

    def updUI(self, channel):
        self.isChannelActive.setChecked(channel.isActive)


class BoardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.board_ip = QLabel("")
        self.channels_tab = QTabWidget()
        self.btn_sendData = QPushButton("Send data to board")

        layout = QVBoxLayout(self)
        #layout.addWidget(self.board_ip)
        layout.addWidget(self.channels_tab)
        layout.addWidget(self.btn_sendData)

        self.setLayout(layout)
        self.setEnabled(True)

#container for device tabs
class BoardsManager(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(250)
        self.setFixedWidth(450)
        self.setEnabled(True)


#Channel of board: its number, should we use its data, data container,
#name to be used as label in main window, tab
class Channel:
    def __init__(self):
        self.number = 0
        self.isActive = True
        self.data = [0] * 1024
        self.name = ""
        self.channelTab = None
    def change_name(self, name):
        self.name = name
    def changeStatus(self, status):
        self.isActive = status
        print("Current status: {0}".format(self.isActive))
    def updUI(self):
        self.channelTab.isChannelActive.setChecked(self.isActive)
    def connectActive(self):
        isChecked = self.channelTab.isChannelActive.isChecked
        self.channelTab.isChannelActive.stateChanged.connect(lambda: self.changeStatus(isChecked()))


#Device describes specific board with its IP address, current role, connection status,
#uptime, connection port, its instance in memory after connection, number of channels
# and list of Channel instances, tab widget
class Device:
    def __init__(self):
        self.ip = '192.168.0.20'
        self.role = "Slave"
        self.status = 'Not connected'
        self.uptime = 0.0
        self.port = '5000'
        self.board = None
        self.nChannels = 0
        self.channels = []
        self.deviceTab = None


    def setIP(self, ip):
        self.ip = ip
    def setRole(self, role):
        self.role = role
    def setStatus(self, status):
        self.status = status
    def setUptime(self, uptime):
        self.uptime = uptime
    
    #when our device is recognized by system and its tab widget is created, make connections to deal with data from widget
    def updTab(self, value):
        self.deviceTab = value
        self.deviceTab.btn_sendData.clicked.connect(self.sendData)

    def sendData(self):
        for chan in self.channels:
            print("Threshold: {0}".format(chan.channelTab.lbl_threshold_ticks.text()))
            print("Gate start: {0}".format(chan.channelTab.lne_gate_start.text()))
            print("Gate end: {0}".format(chan.channelTab.lne_gate_end.text()))
            print("Moving avg: {0}".format(chan.channelTab.lne_gate_movavg.text()))
            print("Baseline: {0}".format(chan.channelTab.lbl_bline_ticks.text()))





#Basic widget for connection to single device
#contains line for device IP, connection and deletion buttons
class DeviceConn(QWidget):
    def __init__(self):
        super().__init__()
        self.isTableDevices = False

        self.properties = Device()

        lbl_ip_info = QLabel("Device IP & port")
        self.lne_ip_edit = QLineEdit()
        self.lne_ip_edit.setInputMask('000.000.000.000;_')
        self.lne_ip_edit.setText(self.properties.ip)
        self.lne_port_edit = QLineEdit()
        self.lne_port_edit.setText(self.properties.port)

        self.lbl_status = QLabel(self.properties.status)
        self.lbl_uptime = QLabel('Uptime: 0.0 hrs')

        self.btn_connect = QPushButton("Connect")

        self.ly_box = QGridLayout()
        self.ly_box.addWidget(lbl_ip_info, 0, 0, 1, 1)
        self.ly_box.addWidget(self.lne_ip_edit, 0, 1, 1, 1)
        self.ly_box.addWidget(self.lne_port_edit, 0, 2, 1, 1)

        self.ly_box.addWidget(self.lbl_status, 2,0, 1,1)
        self.ly_box.addWidget(self.lbl_uptime, 2,1,1,1)
        self.ly_box.addWidget(self.btn_connect, 1,1,1,1)

        self.setLayout(self.ly_box)
        self.setFixedSize(400,100)   

        self.updUI()

#after Connect button is pressed, updates uptime and status of 
#device and shows it on the widget
    def setValuesAfterConnection(self, uptime, connStatus):
        if connStatus:
            self.properties.uptime = uptime
            self.properties.status = 'Connected'
        else:
            self.properties.uptime = 0.0
            self.properties.status = 'Not connected'
        self.updUI()
    
    def updUI(self):
        self.lbl_uptime.setText('Uptime: {:10.3f} hrs'.format(self.properties.uptime/3600))
        self.lbl_status.setText(self.properties.status)

#widget for connection to device taking into account master/slave configuration
class DeviceConn_MasterSlave(DeviceConn):
    def __init__(self):
        super().__init__()

        self.isTableDevices = True
        self.cmb_role = RolesList()
        self.cmb_role.setCurrentIndex(1)

        self.btn_delete = QPushButton("Delete")

        self.ly_box.addWidget(self.cmb_role, 1,0, 1, 1)
        self.ly_box.addWidget(self.btn_delete, 1,2, 1, 1)

        self.setLayout(self.ly_box)
        self.setFixedSize(400,100)  

    #create signal on connection established that fills the table  

#container (map or dict) for connected devices
class DevicesMap(QTableWidget):
    devicesMap = dict()
    def __init__(self):
        super().__init__()
        self.initUI()
 

    def initUI(self):
        self.setColumnCount(4)
        self.setRowCount(len(self.devicesMap))

        self.setHorizontalHeaderLabels([
            "Device IP", "Role", "Status", "Uptime"
        ])
        for item in range (0, self.rowCount()):
            list_roles = QLabel("Undefined")
            line_ip_device_tbl = QLabel('000.000.000.000;_')
            self.setCellWidget(item, 0, line_ip_device_tbl)
            self.setCellWidget(item, 1, list_roles)

#updates UI redrawing it fow all the dictionary entries
    def updUI(self):
        self.setRowCount(len(self.devicesMap))
        for index, (ip, props) in enumerate(self.devicesMap.items()):
            list_roles = QLabel(props.role)
            line_ip_device_tbl = QLabel(props.ip)
            list_status = QLabel(props.status)
            line_uptime = QLabel('{:10.3f} hrs'.format(props.uptime/3600))

            print(props.role, props.ip, props.status, str(props.uptime))

            self.setCellWidget(index, 0, line_ip_device_tbl)
            self.setCellWidget(index, 1, list_roles)
            self.setCellWidget(index, 2, list_status)
            self.setCellWidget(index, 3, line_uptime)


#add info about device in container
    def addData(self, ip, devProps):
        #only one master can be connected
        if devProps.role == "Master":
            for k in self.devicesMap:
                prop = Device()
                prop.ip = k
                prop.role = "Slave"
                prop.status = self.devicesMap[k].status
                prop.uptime = self.devicesMap[k].uptime
                self.devicesMap.update({k: prop})
        self.devicesMap.update({ip: devProps})
        self.updUI()

    def removeData(self, ip):
        #only one master can be connected
        if ip in self.devicesMap:
            self.devicesMap.pop(ip)
        self.updUI()
