# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pic_Widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QEvent

class Ui_pic_Widget(QtWidgets.QWidget):

    def setupUi(self, pic_Widget):
        sliderMin = -55
        sliderMax = 55
        pic_Widget.setObjectName("pic_Widget")
        pic_Widget.setEnabled(True)
        pic_Widget.resize(1243, 879)
        self.img_viewer = QtWidgets.QGraphicsView(pic_Widget)

        self.img_viewer.setGeometry(QtCore.QRect(50, 440, 240, 320))
        self.img_viewer.setBaseSize(QtCore.QSize(240, 320))
        self.img_viewer.setWhatsThis("")
        self.img_viewer.setAccessibleName("")
        self.img_viewer.setObjectName("img_viewer")

        self.refStardand = QtWidgets.QGraphicsView(pic_Widget)
        self.refStardand.setGeometry(QtCore.QRect(330, 440, 120, 160))
        self.refStardand.setBaseSize(QtCore.QSize(240, 320))
        self.refStardand.setMouseTracking(True)
        self.refStardand.setObjectName("refStardand")
        self.graphicsScene = QtWidgets.QGraphicsScene(pic_Widget)



        self.img_x1 = QtWidgets.QGraphicsView(pic_Widget)
        self.img_x1.setGeometry(QtCore.QRect(510, 250, 120, 160))
        self.img_x1.setBaseSize(QtCore.QSize(240, 320))
        self.img_x1.setMouseTracking(True)
        self.img_x1.setObjectName("img_x1")

        self.img_x2 = QtWidgets.QGraphicsView(pic_Widget)
        self.img_x2.setGeometry(QtCore.QRect(670, 250, 120, 160))
        self.img_x2.setBaseSize(QtCore.QSize(240, 320))
        self.img_x2.setMouseTracking(True)
        self.img_x2.setObjectName("img_x2")



        self.img_y1 = QtWidgets.QGraphicsView(pic_Widget)
        self.img_y1.setGeometry(QtCore.QRect(510, 440, 120, 160))
        self.img_y1.setBaseSize(QtCore.QSize(240, 320))
        self.img_y1.setMouseTracking(True)
        self.img_y1.setObjectName("img_y1")


        self.img_y2 = QtWidgets.QGraphicsView(pic_Widget)
        self.img_y2.setGeometry(QtCore.QRect(670, 440, 120, 160))
        self.img_y2.setBaseSize(QtCore.QSize(240, 320))
        self.img_y2.setMouseTracking(True)
        self.img_y2.setObjectName("img_y2")


        self.img_z1 = QtWidgets.QGraphicsView(pic_Widget)
        self.img_z1.setGeometry(QtCore.QRect(510, 630, 120, 160))
        self.img_z1.setBaseSize(QtCore.QSize(240, 320))
        self.img_z1.setMouseTracking(True)
        self.img_z1.setObjectName("img_z1")


        self.img_z2 = QtWidgets.QGraphicsView(pic_Widget)
        self.img_z2.setGeometry(QtCore.QRect(670, 630, 120, 160))
        self.img_z2.setBaseSize(QtCore.QSize(240, 320))
        self.img_z2.setMouseTracking(True)
        self.img_z2.setObjectName("img_z2")


        self.lineEdit_yaw = QtWidgets.QLineEdit(pic_Widget)
        self.lineEdit_yaw.setGeometry(QtCore.QRect(150, 350, 101, 21))
        self.lineEdit_yaw.setObjectName("lineEdit_yaw")
        self.lineEdit_yaw.setAlignment(QtCore.Qt.AlignCenter)
        # self.lineEdit_yaw.clear()


        self.lineEdit_pitch = QtWidgets.QLineEdit(pic_Widget)
        self.lineEdit_pitch.setGeometry(QtCore.QRect(150, 380, 101, 21))
        self.lineEdit_pitch.setObjectName("lineEdit_pitch")
        self.lineEdit_pitch.setAlignment(QtCore.Qt.AlignCenter)

        self.lineEdit_roll = QtWidgets.QLineEdit(pic_Widget)
        self.lineEdit_roll.setGeometry(QtCore.QRect(150, 410, 101, 21))
        self.lineEdit_roll.setObjectName("lineEdit_roll")
        self.lineEdit_roll.setAlignment(QtCore.Qt.AlignCenter)

        self.label_yaw = QtWidgets.QLabel(pic_Widget)
        self.label_yaw.setGeometry(QtCore.QRect(70, 350, 54, 21))
        self.label_yaw.setAlignment(QtCore.Qt.AlignCenter)
        self.label_yaw.setObjectName("label_yaw")


        self.label_roll = QtWidgets.QLabel(pic_Widget)
        self.label_roll.setGeometry(QtCore.QRect(70, 410, 54, 21))
        self.label_roll.setAlignment(QtCore.Qt.AlignCenter)
        self.label_roll.setObjectName("label_roll")


        self.label_pitch = QtWidgets.QLabel(pic_Widget)
        self.label_pitch.setGeometry(QtCore.QRect(70, 380, 54, 21))
        self.label_pitch.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pitch.setObjectName("label_pitch")


        self.horizontalSlider_yaw = QtWidgets.QSlider(pic_Widget)
        self.horizontalSlider_yaw.setGeometry(QtCore.QRect(850, 370, 331, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.horizontalSlider_yaw.setFont(font)
        self.horizontalSlider_yaw.setMouseTracking(True)
        self.horizontalSlider_yaw.setTabletTracking(False)
        self.horizontalSlider_yaw.setAutoFillBackground(False)
        self.horizontalSlider_yaw.setMinimum(sliderMin)
        self.horizontalSlider_yaw.setMaximum(sliderMax)
        self.horizontalSlider_yaw.setSingleStep(5)
        self.horizontalSlider_yaw.setPageStep(5)
        # self.horizontalSlider_yaw.setSliderPosition(0)
        self.horizontalSlider_yaw.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_yaw.setObjectName("horizontalSlider_yaw")
        # self.horizontalSlider_yaw.valueChanged.connect(lambda: self.on_change_func(self.horizontalSlider_yaw))

        # self.horizontalSlider_yaw.mouseMoveEvent(None)
        self.horizontalSlider_yaw.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSlider_yaw.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_yaw.setTickInterval(5)





        self.label_HoriSlider_yaw = QtWidgets.QLabel(pic_Widget)
        self.label_HoriSlider_yaw.setGeometry(QtCore.QRect(870, 330, 54, 21))
        self.label_HoriSlider_yaw.setAlignment(QtCore.Qt.AlignCenter)
        self.label_HoriSlider_yaw.setObjectName("label_HoriSlider_yaw")

        self.lineEdit__HoriSlider_yaw = QtWidgets.QLineEdit(pic_Widget)
        self.lineEdit__HoriSlider_yaw.setGeometry(QtCore.QRect(950, 330, 101, 21))
        self.lineEdit__HoriSlider_yaw.setObjectName("lineEdit__HoriSlider_yaw")


        self.label_HoriSlider_pitch = QtWidgets.QLabel(pic_Widget)
        self.label_HoriSlider_pitch.setGeometry(QtCore.QRect(870, 460, 54, 21))
        self.label_HoriSlider_pitch.setAlignment(QtCore.Qt.AlignCenter)
        self.label_HoriSlider_pitch.setObjectName("label_HoriSlider_pitch")

        self.lineEdit__HoriSlider_pitch = QtWidgets.QLineEdit(pic_Widget)
        self.lineEdit__HoriSlider_pitch.setGeometry(QtCore.QRect(950, 460, 101, 21))
        self.lineEdit__HoriSlider_pitch.setObjectName("lineEdit__HoriSlider_pitch")




        self.horizontalSlider_pitch = QtWidgets.QSlider(pic_Widget)
        self.horizontalSlider_pitch.setGeometry(QtCore.QRect(850, 500, 331, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.horizontalSlider_pitch.setFont(font)
        self.horizontalSlider_pitch.setMouseTracking(True)
        self.horizontalSlider_pitch.setTabletTracking(False)
        self.horizontalSlider_pitch.setAutoFillBackground(False)
        self.horizontalSlider_pitch.setMinimum(sliderMin)
        self.horizontalSlider_pitch.setMaximum(sliderMax)
        self.horizontalSlider_pitch.setSingleStep(5)
        self.horizontalSlider_pitch.setPageStep(5)
        self.horizontalSlider_pitch.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSlider_pitch.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_pitch.setTickInterval(5)



        # self.horizontalSlider_pitch.setSliderPosition(0)
        self.horizontalSlider_pitch.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_pitch.setObjectName("horizontalSlider_pitch")

        self.label_HoriSlider_roll = QtWidgets.QLabel(pic_Widget)
        self.label_HoriSlider_roll.setGeometry(QtCore.QRect(870, 600, 54, 21))
        self.label_HoriSlider_roll.setAlignment(QtCore.Qt.AlignCenter)
        self.label_HoriSlider_roll.setObjectName("label_HoriSlider_roll")
        # self.horizontalSlider_pitch.valueChanged.connect(lambda: self.on_change_func(self.horizontalSlider_pitch))
        self.lineEdit__HoriSlider_roll = QtWidgets.QLineEdit(pic_Widget)
        self.lineEdit__HoriSlider_roll.setGeometry(QtCore.QRect(950, 600, 101, 21))
        self.lineEdit__HoriSlider_roll.setObjectName("lineEdit__HoriSlider_roll")
        self.horizontalSlider_roll = QtWidgets.QSlider(pic_Widget)
        self.horizontalSlider_roll.setGeometry(QtCore.QRect(850, 640, 331, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.horizontalSlider_roll.setFont(font)
        self.horizontalSlider_roll.setMouseTracking(True)
        self.horizontalSlider_roll.setTabletTracking(False)
        self.horizontalSlider_roll.setAutoFillBackground(False)
        self.horizontalSlider_roll.setMinimum(sliderMin)
        self.horizontalSlider_roll.setMaximum(sliderMax)
        self.horizontalSlider_roll.setSingleStep(5)
        self.horizontalSlider_roll.setPageStep(5)
        # self.horizontalSlider_roll.setSliderPosition(0)
        self.horizontalSlider_roll.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_roll.setObjectName("horizontalSlider_roll")
        # self.horizontalSlider_roll.valueChanged.connect(lambda: self.on_change_func(self.horizontalSlider_roll))
        self.horizontalSlider_roll.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSlider_roll.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_roll.setTickInterval(5)


        self.label_yaw.setText('yaw')
        self.label_roll.setText("roll")
        self.label_pitch.setText("pitch")
        self.label_HoriSlider_yaw.setText("yaw")
        self.label_HoriSlider_pitch.setText("pitch")
        self.label_HoriSlider_roll.setText("roll")

        QtCore.QMetaObject.connectSlotsByName(pic_Widget)
        return pic_Widget


