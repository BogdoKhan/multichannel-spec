# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dkc1\Desktop\test-spec\test-spec\oscilloscope\forms\waveform.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WaveformWidget(object):
    def setupUi(self, WaveformWidget):
        WaveformWidget.setObjectName("WaveformWidget")
        WaveformWidget.resize(672, 810)
        self.gridLayout = QtWidgets.QGridLayout(WaveformWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.m_plot_oscilloscope = PlotWidget(WaveformWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_plot_oscilloscope.sizePolicy().hasHeightForWidth())
        self.m_plot_oscilloscope.setSizePolicy(sizePolicy)
        self.m_plot_oscilloscope.setMinimumSize(QtCore.QSize(0, 500))
        self.m_plot_oscilloscope.setObjectName("m_plot_oscilloscope")
        self.gridLayout.addWidget(self.m_plot_oscilloscope, 2, 0, 1, 1)
        self.widget = QtWidgets.QWidget(WaveformWidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.m_check_wave_repeat = QtWidgets.QCheckBox(self.widget)
        self.m_check_wave_repeat.setObjectName("m_check_wave_repeat")
        self.gridLayout_2.addWidget(self.m_check_wave_repeat, 1, 0, 1, 1)
        self.m_checkBox_autoClear = QtWidgets.QCheckBox(self.widget)
        self.m_checkBox_autoClear.setObjectName("m_checkBox_autoClear")
        self.gridLayout_2.addWidget(self.m_checkBox_autoClear, 0, 8, 1, 1)
        self.m_push_get_wave = QtWidgets.QPushButton(self.widget)
        self.m_push_get_wave.setObjectName("m_push_get_wave")
        self.gridLayout_2.addWidget(self.m_push_get_wave, 0, 3, 1, 1)
        self.m_spin_smples_num = QtWidgets.QSpinBox(self.widget)
        self.m_spin_smples_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.m_spin_smples_num.setMinimum(1)
        self.m_spin_smples_num.setMaximum(2048)
        self.m_spin_smples_num.setObjectName("m_spin_smples_num")
        self.gridLayout_2.addWidget(self.m_spin_smples_num, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 5, 2, 1)
        self.m_label_dumped = QtWidgets.QLabel(self.widget)
        self.m_label_dumped.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.m_label_dumped.setObjectName("m_label_dumped")
        self.gridLayout_2.addWidget(self.m_label_dumped, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(402, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 9, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.widget)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 0, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.widget)
        self.label_31.setEnabled(True)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 1, 2, 1, 1)
        self.m_comboBox_channel_id = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_comboBox_channel_id.sizePolicy().hasHeightForWidth())
        self.m_comboBox_channel_id.setSizePolicy(sizePolicy)
        self.m_comboBox_channel_id.setObjectName("m_comboBox_channel_id")
        self.m_comboBox_channel_id.addItem("")
        self.m_comboBox_channel_id.addItem("")
        self.m_comboBox_channel_id.addItem("")
        self.m_comboBox_channel_id.addItem("")
        self.gridLayout_2.addWidget(self.m_comboBox_channel_id, 0, 2, 1, 1)
        self.m_spin_repeat_waves = QtWidgets.QSpinBox(self.widget)
        self.m_spin_repeat_waves.setEnabled(False)
        self.m_spin_repeat_waves.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.m_spin_repeat_waves.setMinimum(1)
        self.m_spin_repeat_waves.setMaximum(100000)
        self.m_spin_repeat_waves.setObjectName("m_spin_repeat_waves")
        self.gridLayout_2.addWidget(self.m_spin_repeat_waves, 1, 1, 1, 1)
        self.m_push_clear = QtWidgets.QPushButton(self.widget)
        self.m_push_clear.setObjectName("m_push_clear")
        self.gridLayout_2.addWidget(self.m_push_clear, 0, 7, 1, 1)
        self.m_checkBox_saveToFile = QtWidgets.QCheckBox(self.widget)
        self.m_checkBox_saveToFile.setObjectName("m_checkBox_saveToFile")
        self.gridLayout_2.addWidget(self.m_checkBox_saveToFile, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.retranslateUi(WaveformWidget)
        QtCore.QMetaObject.connectSlotsByName(WaveformWidget)

    def retranslateUi(self, WaveformWidget):
        _translate = QtCore.QCoreApplication.translate
        WaveformWidget.setWindowTitle(_translate("WaveformWidget", "Form"))
        self.m_check_wave_repeat.setText(_translate("WaveformWidget", "Repeat"))
        self.m_checkBox_autoClear.setText(_translate("WaveformWidget", "Auto Clear"))
        self.m_push_get_wave.setText(_translate("WaveformWidget", "Get Waveform"))
        self.m_label_dumped.setText(_translate("WaveformWidget", "Dumped: 0 "))
        self.label_30.setText(_translate("WaveformWidget", "Samples num"))
        self.label_31.setText(_translate("WaveformWidget", "times"))
        self.m_comboBox_channel_id.setItemText(0, _translate("WaveformWidget", "Channel 0"))
        self.m_comboBox_channel_id.setItemText(1, _translate("WaveformWidget", "Channel 1"))
        self.m_comboBox_channel_id.setItemText(2, _translate("WaveformWidget", "Channel 2"))
        self.m_comboBox_channel_id.setItemText(3, _translate("WaveformWidget", "Channel 3"))
        self.m_push_clear.setText(_translate("WaveformWidget", "Clear plot"))
        self.m_checkBox_saveToFile.setText(_translate("WaveformWidget", "Save to file"))
from pyqtgraph import PlotWidget
