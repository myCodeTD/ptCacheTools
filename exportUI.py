# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'O:\systemTool\python\ptCacheTools\exportUI.ui'
#
# Created: Wed Jun 11 10:52:18 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ExportCacheWindow(object):
    def setupUi(self, ExportCacheWindow):
        ExportCacheWindow.setObjectName(_fromUtf8("ExportCacheWindow"))
        ExportCacheWindow.resize(601, 829)
        self.centralwidget = QtGui.QWidget(ExportCacheWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 281, 101))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 46, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 51, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 61, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.project_label = QtGui.QLabel(self.frame)
        self.project_label.setGeometry(QtCore.QRect(90, 10, 171, 16))
        self.project_label.setObjectName(_fromUtf8("project_label"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 46, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.episode_label = QtGui.QLabel(self.frame)
        self.episode_label.setGeometry(QtCore.QRect(90, 30, 171, 16))
        self.episode_label.setObjectName(_fromUtf8("episode_label"))
        self.sequence_label = QtGui.QLabel(self.frame)
        self.sequence_label.setGeometry(QtCore.QRect(90, 50, 141, 16))
        self.sequence_label.setObjectName(_fromUtf8("sequence_label"))
        self.shot_label = QtGui.QLabel(self.frame)
        self.shot_label.setGeometry(QtCore.QRect(90, 70, 151, 16))
        self.shot_label.setObjectName(_fromUtf8("shot_label"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(310, 20, 281, 771))
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 101, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.asset_listWidget = QtGui.QListWidget(self.frame_2)
        self.asset_listWidget.setGeometry(QtCore.QRect(10, 30, 261, 191))
        self.asset_listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.asset_listWidget.setObjectName(_fromUtf8("asset_listWidget"))
        self.cache_pushButton = QtGui.QPushButton(self.frame_2)
        self.cache_pushButton.setGeometry(QtCore.QRect(10, 340, 261, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.cache_pushButton.setPalette(palette)
        self.cache_pushButton.setObjectName(_fromUtf8("cache_pushButton"))
        self.cacheSelected_pushButton = QtGui.QPushButton(self.frame_2)
        self.cacheSelected_pushButton.setGeometry(QtCore.QRect(10, 305, 261, 31))
        self.cacheSelected_pushButton.setObjectName(_fromUtf8("cacheSelected_pushButton"))
        self.publishHero_pushButton = QtGui.QPushButton(self.frame_2)
        self.publishHero_pushButton.setGeometry(QtCore.QRect(10, 560, 261, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.publishHero_pushButton.setPalette(palette)
        self.publishHero_pushButton.setObjectName(_fromUtf8("publishHero_pushButton"))
        self.backupHero_checkBox = QtGui.QCheckBox(self.frame_2)
        self.backupHero_checkBox.setGeometry(QtCore.QRect(10, 490, 91, 17))
        self.backupHero_checkBox.setChecked(True)
        self.backupHero_checkBox.setObjectName(_fromUtf8("backupHero_checkBox"))
        self.output_lineEdit = QtGui.QLineEdit(self.frame_2)
        self.output_lineEdit.setGeometry(QtCore.QRect(10, 440, 261, 20))
        self.output_lineEdit.setText(_fromUtf8(""))
        self.output_lineEdit.setObjectName(_fromUtf8("output_lineEdit"))
        self.label_11 = QtGui.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(20, 420, 91, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.overrideOutput_checkBox = QtGui.QCheckBox(self.frame_2)
        self.overrideOutput_checkBox.setGeometry(QtCore.QRect(10, 470, 111, 17))
        self.overrideOutput_checkBox.setObjectName(_fromUtf8("overrideOutput_checkBox"))
        self.manual_checkBox = QtGui.QCheckBox(self.frame_2)
        self.manual_checkBox.setGeometry(QtCore.QRect(10, 400, 121, 17))
        self.manual_checkBox.setObjectName(_fromUtf8("manual_checkBox"))
        self.cache_label = QtGui.QLabel(self.frame_2)
        self.cache_label.setGeometry(QtCore.QRect(130, 490, 131, 20))
        self.cache_label.setObjectName(_fromUtf8("cache_label"))
        self.buildScene_pushButton = QtGui.QPushButton(self.frame_2)
        self.buildScene_pushButton.setGeometry(QtCore.QRect(10, 650, 261, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.buildScene_pushButton.setPalette(palette)
        self.buildScene_pushButton.setObjectName(_fromUtf8("buildScene_pushButton"))
        self.shotgun_checkBox = QtGui.QCheckBox(self.frame_2)
        self.shotgun_checkBox.setGeometry(QtCore.QRect(10, 530, 91, 17))
        self.shotgun_checkBox.setChecked(True)
        self.shotgun_checkBox.setObjectName(_fromUtf8("shotgun_checkBox"))
        self.line = QtGui.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(10, 520, 260, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(10, 615, 260, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.openScene_pushButton = QtGui.QPushButton(self.frame_2)
        self.openScene_pushButton.setGeometry(QtCore.QRect(10, 690, 161, 31))
        self.openScene_pushButton.setObjectName(_fromUtf8("openScene_pushButton"))
        self.oneTime_checkBox = QtGui.QCheckBox(self.frame_2)
        self.oneTime_checkBox.setGeometry(QtCore.QRect(10, 285, 91, 17))
        self.oneTime_checkBox.setWhatsThis(_fromUtf8(""))
        self.oneTime_checkBox.setChecked(False)
        self.oneTime_checkBox.setObjectName(_fromUtf8("oneTime_checkBox"))
        self.updateCacheList_pushButton = QtGui.QPushButton(self.frame_2)
        self.updateCacheList_pushButton.setGeometry(QtCore.QRect(10, 225, 261, 26))
        self.updateCacheList_pushButton.setObjectName(_fromUtf8("updateCacheList_pushButton"))
        self.playblast_pushButton = QtGui.QPushButton(self.frame_2)
        self.playblast_pushButton.setGeometry(QtCore.QRect(10, 730, 161, 31))
        self.playblast_pushButton.setObjectName(_fromUtf8("playblast_pushButton"))
        self.reportProblem_pushButton = QtGui.QPushButton(self.frame_2)
        self.reportProblem_pushButton.setGeometry(QtCore.QRect(180, 690, 91, 71))
        self.reportProblem_pushButton.setObjectName(_fromUtf8("reportProblem_pushButton"))
        self.addCache_pushButton = QtGui.QPushButton(self.frame_2)
        self.addCache_pushButton.setGeometry(QtCore.QRect(10, 255, 131, 26))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(207, 158, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 158, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 158, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.addCache_pushButton.setPalette(palette)
        self.addCache_pushButton.setObjectName(_fromUtf8("addCache_pushButton"))
        self.removeCache_pushButton = QtGui.QPushButton(self.frame_2)
        self.removeCache_pushButton.setGeometry(QtCore.QRect(140, 255, 131, 26))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(176, 97, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 97, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 97, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.removeCache_pushButton.setPalette(palette)
        self.removeCache_pushButton.setObjectName(_fromUtf8("removeCache_pushButton"))
        self.line_3 = QtGui.QFrame(self.frame_2)
        self.line_3.setGeometry(QtCore.QRect(10, 390, 260, 3))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 810, 46, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.status_label = QtGui.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(80, 810, 201, 16))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.status_label.setFont(font)
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 130, 281, 591))
        self.frame_3.setFrameShape(QtGui.QFrame.Box)
        self.frame_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_8 = QtGui.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 101, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.set_listWidget = QtGui.QListWidget(self.frame_3)
        self.set_listWidget.setGeometry(QtCore.QRect(10, 30, 261, 71))
        self.set_listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.set_listWidget.setObjectName(_fromUtf8("set_listWidget"))
        self.exportSet_pushButton = QtGui.QPushButton(self.frame_3)
        self.exportSet_pushButton.setGeometry(QtCore.QRect(10, 140, 261, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.exportSet_pushButton.setPalette(palette)
        self.exportSet_pushButton.setFlat(False)
        self.exportSet_pushButton.setObjectName(_fromUtf8("exportSet_pushButton"))
        self.updateSet_pushButton = QtGui.QPushButton(self.frame_3)
        self.updateSet_pushButton.setGeometry(QtCore.QRect(10, 110, 261, 26))
        self.updateSet_pushButton.setObjectName(_fromUtf8("updateSet_pushButton"))
        self.camera_listWidget = QtGui.QListWidget(self.frame_3)
        self.camera_listWidget.setGeometry(QtCore.QRect(10, 410, 261, 91))
        self.camera_listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.camera_listWidget.setObjectName(_fromUtf8("camera_listWidget"))
        self.exportCamera_pushButton = QtGui.QPushButton(self.frame_3)
        self.exportCamera_pushButton.setGeometry(QtCore.QRect(10, 540, 261, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 60, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.exportCamera_pushButton.setPalette(palette)
        self.exportCamera_pushButton.setObjectName(_fromUtf8("exportCamera_pushButton"))
        self.label_9 = QtGui.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(20, 390, 101, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.all_checkBox = QtGui.QCheckBox(self.frame_3)
        self.all_checkBox.setGeometry(QtCore.QRect(20, 510, 121, 17))
        self.all_checkBox.setChecked(False)
        self.all_checkBox.setObjectName(_fromUtf8("all_checkBox"))
        self.label_10 = QtGui.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(20, 190, 101, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.nonCache_listWidget = QtGui.QListWidget(self.frame_3)
        self.nonCache_listWidget.setGeometry(QtCore.QRect(10, 210, 261, 91))
        self.nonCache_listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.nonCache_listWidget.setObjectName(_fromUtf8("nonCache_listWidget"))
        self.add_pushButton = QtGui.QPushButton(self.frame_3)
        self.add_pushButton.setGeometry(QtCore.QRect(10, 310, 131, 26))
        self.add_pushButton.setObjectName(_fromUtf8("add_pushButton"))
        self.remove_pushButton = QtGui.QPushButton(self.frame_3)
        self.remove_pushButton.setGeometry(QtCore.QRect(140, 310, 131, 26))
        self.remove_pushButton.setObjectName(_fromUtf8("remove_pushButton"))
        self.exportNonCache_pushButton = QtGui.QPushButton(self.frame_3)
        self.exportNonCache_pushButton.setGeometry(QtCore.QRect(10, 340, 261, 41))
        self.exportNonCache_pushButton.setObjectName(_fromUtf8("exportNonCache_pushButton"))
        self.clearEdlData_pushButton = QtGui.QPushButton(self.centralwidget)
        self.clearEdlData_pushButton.setGeometry(QtCore.QRect(160, 725, 131, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(108, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.clearEdlData_pushButton.setPalette(palette)
        self.clearEdlData_pushButton.setObjectName(_fromUtf8("clearEdlData_pushButton"))
        self.clearAllCacheData_pushButton = QtGui.QPushButton(self.centralwidget)
        self.clearAllCacheData_pushButton.setGeometry(QtCore.QRect(30, 760, 261, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(108, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.clearAllCacheData_pushButton.setPalette(palette)
        self.clearAllCacheData_pushButton.setObjectName(_fromUtf8("clearAllCacheData_pushButton"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(20, 790, 571, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.deleteOldVersion_pushButton = QtGui.QPushButton(self.centralwidget)
        self.deleteOldVersion_pushButton.setGeometry(QtCore.QRect(30, 725, 131, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(108, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 29, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.deleteOldVersion_pushButton.setPalette(palette)
        self.deleteOldVersion_pushButton.setObjectName(_fromUtf8("deleteOldVersion_pushButton"))
        ExportCacheWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExportCacheWindow)
        QtCore.QMetaObject.connectSlotsByName(ExportCacheWindow)

    def retranslateUi(self, ExportCacheWindow):
        ExportCacheWindow.setWindowTitle(QtGui.QApplication.translate("ExportCacheWindow", "PT Export Cache Tool v.1.2", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ExportCacheWindow", "Project : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ExportCacheWindow", "Episode : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ExportCacheWindow", "Sequence : ", None, QtGui.QApplication.UnicodeUTF8))
        self.project_label.setText(QtGui.QApplication.translate("ExportCacheWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ExportCacheWindow", "Shot : ", None, QtGui.QApplication.UnicodeUTF8))
        self.episode_label.setText(QtGui.QApplication.translate("ExportCacheWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.sequence_label.setText(QtGui.QApplication.translate("ExportCacheWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_label.setText(QtGui.QApplication.translate("ExportCacheWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ExportCacheWindow", "Cache Asset Lists", None, QtGui.QApplication.UnicodeUTF8))
        self.cache_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "3. Export Cache", None, QtGui.QApplication.UnicodeUTF8))
        self.cacheSelected_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "Cache Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.publishHero_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "4. Publish Hero Cache", None, QtGui.QApplication.UnicodeUTF8))
        self.backupHero_checkBox.setText(QtGui.QApplication.translate("ExportCacheWindow", "Backup Hero", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ExportCacheWindow", "Output Cache", None, QtGui.QApplication.UnicodeUTF8))
        self.overrideOutput_checkBox.setText(QtGui.QApplication.translate("ExportCacheWindow", "Override Output", None, QtGui.QApplication.UnicodeUTF8))
        self.manual_checkBox.setText(QtGui.QApplication.translate("ExportCacheWindow", "Manul Export Cache", None, QtGui.QApplication.UnicodeUTF8))
        self.cache_label.setText(QtGui.QApplication.translate("ExportCacheWindow", "cache : ", None, QtGui.QApplication.UnicodeUTF8))
        self.buildScene_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "5. Prepare Build Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_checkBox.setText(QtGui.QApplication.translate("ExportCacheWindow", "Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.openScene_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "6. Open Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.oneTime_checkBox.setText(QtGui.QApplication.translate("ExportCacheWindow", "One Process", None, QtGui.QApplication.UnicodeUTF8))
        self.updateCacheList_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.playblast_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "7. Open Playblast", None, QtGui.QApplication.UnicodeUTF8))
        self.reportProblem_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "Report Problem", None, QtGui.QApplication.UnicodeUTF8))
        self.addCache_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "Add Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.removeCache_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "Remove Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ExportCacheWindow", "Status : ", None, QtGui.QApplication.UnicodeUTF8))
        self.status_label.setText(QtGui.QApplication.translate("ExportCacheWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ExportCacheWindow", "Set Export", None, QtGui.QApplication.UnicodeUTF8))
        self.exportSet_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "1. Export Set", None, QtGui.QApplication.UnicodeUTF8))
        self.updateSet_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.exportCamera_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "2. Export Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ExportCacheWindow", "Export Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.all_checkBox.setText(QtGui.QApplication.translate("ExportCacheWindow", "Show All / Export All", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ExportCacheWindow", "Non Cache Export", None, QtGui.QApplication.UnicodeUTF8))
        self.add_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.exportNonCache_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "1. Export Non Cache (Optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.clearEdlData_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "Clear Edl Data", None, QtGui.QApplication.UnicodeUTF8))
        self.clearAllCacheData_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "Clear All Cache Data", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteOldVersion_pushButton.setText(QtGui.QApplication.translate("ExportCacheWindow", "Delete Old Version", None, QtGui.QApplication.UnicodeUTF8))

