# -*- coding: UTF-8 -*-

import os
import sys
import json
import cv2
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from libs.toolbar import ToolBar
import math
import numpy as np
import pic_Widget


__appname__ = 'label_tool'
# __config__ = 'config.yaml'
CUR_LABEL = None
# sys.path[0] = "D:\label_Tool"
class MainWindow(QMainWindow):
    # 初始化
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # load config file
        # self.config = self.load_config(__config__) #载入配置文件
        # self.config = self.load_config()
        # file list
        self.file_list = []  # 当前文件列表
        self.curr_dir_path = None  # 当前文件夹路径
        self.curr_pro_path = None
        self.curr_img_idx = None  # 当前照片的id
        self.curr_label = None
        self.cur_img_path = None
        self.init_ui()  # 初始化UI界面

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # def load_config(self, config):  # 加载配置文件
    #     """load label from config file"""
    #     with open(config, 'r') as f:
    #        config = yaml.load(f)
    #     # config = {'label': {'standard':0, 'unstandard': 1, 'other':2}}
    #     return config

    def init_ui(self): # 初始化UI界面
        """init ui"""
        self.setWindowTitle(__appname__)
        self.setGeometry(300, 300, 1900, 800)
        # self.statusBar().showMessage('Close')
        self._init_toolbar()    # 左边的工具栏
        # self._init_label_button()   # 右边的标签栏
        self._init_file_list()   # 右边的文件栏

        self._init_img_viewer()  # 图片浏览器
        self.show()

    def _init_toolbar(self):    # 左边的工具栏
        open_dir_act = QAction('Open', self)
        open_dir_act.setShortcut('Ctrl+O')
        open_dir_act.triggered.connect(self.open_dir)

        prev_act = QAction('previous', self)
        prev_act.triggered.connect(self.open_prev_img)
        prev_act.setShortcuts(['A', Qt.Key_4])
        # prev_act.setShortcut(Qt.Key_4)

        next_act = QAction('next', self)
        next_act.triggered.connect(self.open_next_img)
        next_act.setShortcuts(['D', Qt.Key_6])

        skip_act = QAction('skip', self)
        skip_act.triggered.connect(self.open_skipnext_img)
        skip_act.setShortcuts(['W', Qt.Key_8])

        exit_act = QAction('exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)

        toolbar = ToolBar('toolbar')
        toolbar.addAction(open_dir_act)
        toolbar.addAction(prev_act)
        toolbar.addAction(next_act)
        toolbar.addAction(skip_act)
        toolbar.addSeparator()
        toolbar.addAction(exit_act)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)

    def _init_img_viewer(self):

        pic_Widget_mid = QWidget()
        pic_Widget_mid = pic_Widget.Ui_pic_Widget.setupUi(self, pic_Widget_mid)
        self.setCentralWidget(pic_Widget_mid)



    def on_change_func(self, slider):  # 7
        cur_yaw = 0

        if slider == self.horizontalSlider_yaw:
            cur_yaw = self.polarizationFive(self.horizontalSlider_yaw.value())
            self.lineEdit__HoriSlider_yaw.setText(str(cur_yaw))
            self.horizontalSlider_yaw.setSliderPosition(cur_yaw)
            self.curr_label["yaw"] = cur_yaw
            self._load_img_unlabel(self.cur_img_path, self.img_viewer, graphicsScene(self.lineEdit_yaw))
            # 代表图片
        elif slider == self.horizontalSlider_pitch:
            cur_pitch = self.polarizationFive(self.horizontalSlider_pitch.value())
            self.lineEdit__HoriSlider_pitch.setText(str(cur_pitch))
            self.horizontalSlider_pitch.setSliderPosition(cur_pitch)
            self.curr_label["pitch"] = cur_pitch
            self._load_img_unlabel(self.cur_img_path, self.img_viewer, graphicsScene(self.lineEdit_yaw))
        elif slider == self.horizontalSlider_roll:
            cur_roll = self.polarizationFive(self.horizontalSlider_roll.value())
            self.lineEdit__HoriSlider_roll.setText(str(cur_roll))
            self.horizontalSlider_roll.setSliderPosition(cur_roll)
            self.curr_label["roll"] = cur_roll
            self._load_img_unlabel(self.cur_img_path, self.img_viewer, graphicsScene(self.lineEdit_yaw))

        self._load_ref_img(self.curr_label)


    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # def _init_label_button(self):    # 右边的标签栏
    #     head_layer = QVBoxLayout()
    #     i = 0
    #     shortcuts = 'zxcvb'
    #     for label_name, label_idx in self.config['label'].items():
    #         button = 'button_{}'.format(label_idx)
    #         ## initialize the button
    #         setattr(self, button, QPushButton(label_name, self))
    #         getattr(self, button).setShortcut(shortcuts[i])
    #         i += 1
    #         ## call out function
    #         getattr(self, button).clicked.connect(self.rb_clicked)
    #         ## set button size
    #         getattr(self, button).setMinimumHeight(60)
    #         ## add the button to the layout
    #         head_layer.addWidget(getattr(self, button))
    #
    #     self.head_gbox = QGroupBox('status', self)
    #     self.head_gbox.setLayout(head_layer)
    #
    #     label_selector_layout = QVBoxLayout()
    #     label_selector_layout.addWidget(self.head_gbox)
    #
    #
    #     label_selector_widget = QWidget()
    #     label_selector_widget.setLayout(label_selector_layout)
    #     self.label_selector_dock = QDockWidget('Label Select', self)
    #     self.label_selector_dock.setObjectName('labels')
    #     self.label_selector_dock.setWidget(label_selector_widget)
    #     self.addDockWidget(Qt.RightDockWidgetArea, self.label_selector_dock)

    def rb_clicked(self,label):   # 规则检测
        if self.curr_img_idx == None:
            QMessageBox.information(self,
                                    "warning",
                                    "Please open the image folder",
                                    QMessageBox.Ok)

            return

        self.setWindowTitle(self.curr_dir_path + ' * ')

        # 保存标签文件内容
        # label_name = self.sender().text()
        # label = self.config['label'][label_name]
        # self.save_anno(label)
        self.save_anno(label)
        self.open_next_img()

    def _init_file_list(self):  # 初始化列表
        self.file_list_widget = QListWidget()
        self.file_list_widget.itemDoubleClicked.connect(self.file_item_double_clicked)
        self.file_list_dock = QDockWidget('File List', self)
        self.file_list_dock.setObjectName('files')
        self.file_list_dock.setWidget(self.file_list_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.file_list_dock)

    def file_item_double_clicked(self, item):  # 双击file_item
        file_name = item.text()
        img_idx = self.file_list.index(file_name)
        self._switch_img(img_idx)

    def open_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self, 'Open Folder', os.path.expanduser('~'))


        if dir_path:
            self._import_dir_images(dir_path)

    def _import_dir_images(self, dir_path):
        if self.open_dir == dir_path:
            return

        self.curr_dir_path = dir_path
        pro_path = os.path.dirname(dir_path)
        self.curr_pro_path = pro_path
        # print(pro_path)
        # self.curr_pro_path = dir_path.split
        self.file_list_widget.clear()
        self.file_list = sorted([name for name in os.listdir(dir_path) if self._is_img(name)])
        if not self.file_list:
            return
        for idx, file_path in enumerate(self.file_list):
            item = QListWidgetItem(file_path)
            item.setFlags(item.flags() ^ Qt.ItemIsUserCheckable)
            if self._has_label_file(idx):
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
            self.file_list_widget.addItem(item)
        init_idx = 0
        self._switch_img(init_idx)
        self.setWindowTitle(dir_path)
        self.horizontalSlider_roll.valueChanged.connect(lambda: self.on_change_func(self.horizontalSlider_roll))
        self.horizontalSlider_yaw.valueChanged.connect(lambda: self.on_change_func(self.horizontalSlider_yaw))
        self.horizontalSlider_pitch.valueChanged.connect(lambda: self.on_change_func(self.horizontalSlider_pitch))
    def _is_img(self, file_name):
        ext = file_name.split('.')[-1]
        return ext in ['jpg', 'jpeg', 'png', 'bmp']

    def save_anno(self, content):   # 保存label文件
        if self.curr_img_idx == None:
            self._warning_box(title="warning", message="Please open the image folder")
            return

        label_name = self._get_label_name(self.curr_img_idx)
        label_path = os.path.join(self.curr_dir_path, label_name)

        try:
            with open(label_path, 'w') as fout:
                json.dump(content, fout)
        except Exception as e:
            QMessageBox.warning(self, 'warning', str(e))
            return

        self.setWindowTitle(self.curr_dir_path)
        item = self.file_list_widget.item(self.curr_img_idx)
        item.setCheckState(Qt.Checked)

    def _get_label_name(self, img_idx):     # 获取标签文件名称.json
        img_name = self.file_list[img_idx]
        label_name = img_name.split('.')[0] + '.json'
        return label_name
    def open_skipnext_img(self):
        if self.curr_img_idx == None:
            self._warning_box(title="warning", message="Please open the image folder")
            return

        if self.curr_img_idx == len(self.file_list):
            self._warning_box(title="warning", message="Finished!!")
            return

        print("skip :" + str(self.curr_img_idx))

        # self.result_label = self.curr_label
        label = self.curr_label
        label["yaw"] = -1
        label["pitch"] = -1
        label["roll"] = -1
        # print(label)
        self.rb_clicked(label)
        pass
    def open_next_img(self):  # 打开下一张
        if self.curr_img_idx == None:
            self._warning_box(title="warning", message="Please open the image folder")
            return

        if self.curr_img_idx == len(self.file_list) - 1:
            self._warning_box(title="warning", message="Finished!!")
            return

        next_img_idx = self.curr_img_idx + 1
        self._switch_img(next_img_idx)

    def open_prev_img(self):  # 打开上一张
        if self.curr_img_idx == None:
            self._warning_box(title="warning", message="Please open the image folder")
            return

        if self.curr_img_idx == 0:
            self._warning_box(title="warning", message="No previous image. It's the first image.")
            return

        prev_img_idx = self.curr_img_idx - 1
        self._switch_img(prev_img_idx)

    def _switch_img(self, img_idx):  # 切换图片
        self._set_default_color()
        if img_idx == self.curr_img_idx:
            return

        img_name = self.file_list[img_idx]
        # print(img_name)
        img_path = os.path.join(self.curr_dir_path, img_name)
        self.cur_img_path = img_path
        self._get_json(img_name)

        if not self._load_img_unlabel(img_path, self.img_viewer,graphicsScene(self.lineEdit_yaw) ):
            return

        self._load_ref_img(True)

        self.setWindowTitle(self.curr_dir_path)
        self.curr_img_idx = img_idx
        file_widget_item = self.file_list_widget.item(img_idx)
        file_widget_item.setSelected(True)

        # 已经标注好的图片 显示
        if self._has_label_file(img_idx):
            label = self._load_label(img_idx)
            self._set_color_by_label(label)

    def _set_default_color(self):   # 设置标签按钮初始化颜色
        self.lineEdit_yaw.clear()
        self.lineEdit_pitch.clear()
        self.lineEdit_roll.clear()

    def _set_color_by_label(self, label):   # 设置标签按钮颜色
        self.lineEdit_yaw.setText(str(label["yaw"]))
        self.lineEdit_pitch.setText(str(label["pitch"]))
        self.lineEdit_roll.setText(str(label["roll"]))
        # for label_name, label_idx in self.config['label'].items():
        #     if label_idx == label:
        #         button = 'button_{}'.format(label_idx)
        #         ## set the button color to the default color
        #         getattr(self, button).setStyleSheet("background-color: red")

    def _get_json(self, img_name):
        # print(img_name)
        img_num = img_name.split('.')[0]
        label_path = os.path.join(self.curr_pro_path, 'unlabeled_images', img_num + '.json')

        if not (os.path.exists(label_path)):
            img_num = 'corse_' + img_num
            label_path = os.path.join(self.curr_pro_path, 'corse_labels', img_num + '.json')
        # label_path = sys.path[0]+'\corse_labels\\'+img_num+'.json'
        print('[load] label_path '+label_path)
        try:
            with open(label_path, 'r') as fin:
                # curr_label = json.load(fin)
                self.curr_label = json.load(fin)
            print('[load]', img_num, self.curr_label)
            return self.curr_label
        except Exception as e:
            QMessageBox.warning(self, 'Warning', str(e))
            return None
    def _load_ref_img(self,curr_label):
            self.horizontalSlider_yaw.setSliderPosition(self.curr_label["yaw"])
            self.lineEdit__HoriSlider_yaw.setText(str(self.horizontalSlider_yaw.value()))
            self.horizontalSlider_pitch.setSliderPosition(self.curr_label["pitch"])
            self.lineEdit__HoriSlider_pitch.setText(str(self.horizontalSlider_pitch.value()))
            self.horizontalSlider_roll.setSliderPosition(self.curr_label["roll"])
            self.lineEdit__HoriSlider_roll.setText(str(self.horizontalSlider_roll.value()))
            reference_images_Path = os.path.join(self.curr_pro_path,'reference_images')
            # reference_images_Path = r'D:\workspace\xmc\label\hello_world\reference_images'
            refStardand =os.path.join(reference_images_Path,
                                  'ref_yaw_'+str(self.curr_label["yaw"])+'_pitch_'+str(self.curr_label["pitch"])
                                    +'_roll_'+str(self.curr_label["roll"])+'.jpg')


            self._load_img(refStardand, self.refStardand, graphicsScene())

            img_x1 = os.path.join(reference_images_Path,
                                  'ref_yaw_'+str(self.curr_label["yaw"]-5)+'_pitch_'+str(self.curr_label["pitch"])
                                  +'_roll_'+str(self.curr_label["roll"])+'.jpg')

            self._load_img(img_x1, self.img_x1,graphicsScene_x1())

            img_x2 = os.path.join(reference_images_Path,
                                  'ref_yaw_' + str(self.curr_label["yaw"] + 5) + '_pitch_' + str(self.curr_label["pitch"])
                                  + '_roll_' + str(self.curr_label["roll"]) + '.jpg')

            self._load_img(img_x2, self.img_x2,graphicsScene_x2())

            img_y1 = os.path.join(reference_images_Path,
                                  'ref_yaw_' + str(self.curr_label["yaw"]) + '_pitch_' + str(self.curr_label["pitch"]-5)
                                  + '_roll_' + str(self.curr_label["roll"]) + '.jpg')

            self._load_img(img_y1, self.img_y1,graphicsScene_y1())

            img_y2 = os.path.join(reference_images_Path,
                                  'ref_yaw_' + str(self.curr_label["yaw"]) + '_pitch_' + str(self.curr_label["pitch"] + 5)
                                  + '_roll_' + str(self.curr_label["roll"]) + '.jpg')

            self._load_img(img_y2, self.img_y2, graphicsScene_y2())

            img_z1 = os.path.join(reference_images_Path,
                                  'ref_yaw_' + str(self.curr_label["yaw"]) + '_pitch_' + str(self.curr_label["pitch"])
                                  + '_roll_' + str(self.curr_label["roll"]-5) + '.jpg')

            self._load_img(img_z1, self.img_z1,graphicsScene_z1())

            img_z2 = os.path.join(reference_images_Path,
                                  'ref_yaw_' + str(self.curr_label["yaw"]) + '_pitch_' + str(self.curr_label["pitch"])
                                  + '_roll_' + str(self.curr_label["roll"] +5) + '.jpg')
            self._load_img(img_z2, self.img_z2,graphicsScene_z2())

            return

    def draw_axis(self, img, yaw, pitch, roll, tdx=None, tdy=None, size=25):
        # print(type(img))
        pitch = pitch * np.pi / 180
        yaw = -(yaw * np.pi / 180)
        roll = roll * np.pi / 180

        if tdx != None and tdy != None:
            tdx = tdx
            tdy = tdy
        else:
            height, width = img.shape[:2]
            tdx = width / 2
            tdy = height / 2

        # X-Axis pointing to right. drawn in red
        x1 = size * (math.cos(yaw) * math.cos(roll)) + tdx
        y1 = size * (math.cos(pitch) * math.sin(roll) + math.cos(roll) * math.sin(pitch) * math.sin(yaw)) + tdy

        # Y-Axis | drawn in green
        #        v
        x2 = size * (-math.cos(yaw) * math.sin(roll)) + tdx
        y2 = size * (math.cos(pitch) * math.cos(roll) - math.sin(pitch) * math.sin(yaw) * math.sin(roll)) + tdy

        # Z-Axis (out of the screen) drawn in blue
        x3 = size * (math.sin(yaw)) + tdx
        y3 = size * (-math.cos(yaw) * math.sin(pitch)) + tdy

        cv2.line(img, (int(tdx), int(tdy)), (int(x1), int(y1)), (0, 0, 255), 2)
        cv2.line(img, (int(tdx), int(tdy)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.line(img, (int(tdx), int(tdy)), (int(x3), int(y3)), (255, 0, 0), 1)

        return img

    def _load_img(self, img_path, img_viewer,scene ):  # 加载图片
        # print(img_path)
        try:
            with open(img_path, 'rb') as f:
                img_data = f.read()
        except Exception as e:
            QMessageBox.warning(self, 'Warning', str(e))
            return
        img = QImage.fromData(img_data)
        if img.isNull():
            QMessageBox.warning(self, 'Warning', 'Invalid Image')
            return False
        # if
        #     img = draw_axis(img,)

        item = QGraphicsPixmapItem(QPixmap(img))
        # scene = graphicsScene()
        scene.addItem(item)
        img_viewer.setScene(scene)
        img_viewer.fitInView(item)  # 参数类型为QGraphicsItem

        return True

    def _load_img_unlabel(self, img_path, img_viewer, scene ):  # 加载图片
        # print(img_path)
        try:
            with open(img_path, 'rb') as f:
                img = cv2.imread(img_path)
        except Exception as e:
            QMessageBox.warning(self, 'Warning', str(e))
            return
        img = self.draw_axis(img, self.curr_label['yaw'],self.curr_label['pitch'],self.curr_label['roll'])
        img = QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)
        if img.isNull():
            QMessageBox.warning(self, 'Warning', 'Invalid Image')
            return False


        item = QGraphicsPixmapItem(QPixmap(img))
        # scene = graphicsScene()
        scene.addItem(item)
        img_viewer.setScene(scene)
        img_viewer.fitInView(item)  # 参数类型为QGraphicsItem

        return True

    def _has_label_file(self, img_idx):  # 存在标签文件
        label_name = self._get_label_name(img_idx)
        label_path = os.path.join(self.curr_dir_path, label_name)
        return os.path.exists(label_path)

    def _load_label(self, img_idx): # 加载标签文件
        label_name = self._get_label_name(img_idx)
        label_path = os.path.join(self.curr_dir_path, label_name)

        try:
            with open(label_path, 'r') as fin:
                # curr_label = json.load(fin)
                curr_label = json.load(fin)
            # print('[load]', label_name, curr_label)
            # exit(0)
            return curr_label
        except Exception as e:
            QMessageBox.warning(self, 'Warning', str(e))
            return None

    def polarizationFive(self, val):
        if val % 5 == 0:
            return val
        else :
            return round(val,-1)
    def _warning_box(self, title, message): # 警告框
        return QMessageBox.information(self,
                                    title,
                                    message,
                                    QMessageBox.Ok)


    def closeEvent(self, event):  # 关闭事件
        event.accept()

    def getSignal_ref_stard(self):
        # self.result_label = self.curr_label
        self.showResultLabe(self.curr_label["yaw"], self.curr_label["pitch"],
                            self.curr_label["roll"])
    def getSignal_ref_x1(self):
        self.showResultLabe(self.curr_label["yaw"]-5, self.curr_label["pitch"],
                            self.curr_label["roll"])
    def getSignal_ref_x2(self):
        self.showResultLabe(self.curr_label["yaw"] + 5, self.curr_label["pitch"],
                            self.curr_label["roll"])
    def getSignal_ref_y1(self):
        self.showResultLabe(self.curr_label["yaw"], self.curr_label["pitch"] - 5,
                            self.curr_label["roll"])
    def getSignal_ref_y2(self):
        self.showResultLabe(self.curr_label["yaw"], self.curr_label["pitch"] + 5,
                            self.curr_label["roll"])
    def getSignal_ref_z1(self):
        self.showResultLabe(self.curr_label["yaw"], self.curr_label["pitch"],
                            self.curr_label["roll"]-5)
    def getSignal_ref_z2(self):
        self.showResultLabe(self.curr_label["yaw"], self.curr_label["pitch"],
                            self.curr_label["roll"]+5)
    def showResultLabe(self, yaw, pitch, roll):
        self.lineEdit_yaw.setText(str(yaw))
        self.lineEdit_pitch.setText(str(pitch))
        self.lineEdit_roll.setText(str(roll))


    def getSignal_save_stard(self):
        # self.result_label = self.curr_label
        self.rb_clicked(self.curr_label)
    def getSignal_save_x1(self):
        # self.result_label = self.curr_label
        label = self.curr_label
        label["yaw"] = label["yaw"] - 5
        print(label)
        self.rb_clicked(label)
    def getSignal_save_x2(self):
        # self.result_label = self.curr_label
        label = self.curr_label
        label["yaw"] = label["yaw"] + 5
        print(label)
        self.rb_clicked(label)
    def getSignal_save_y1(self):
        # self.result_label = self.curr_label
        label = self.curr_label
        label["pitch"] = label["pitch"] - 5
        print(label)
        self.rb_clicked(label)
    def getSignal_save_y2(self):
        # self.result_label = self.curr_label
        label = self.curr_label
        label["pitch"] = label["pitch"] + 5
        print(label)
        self.rb_clicked(label)
    def getSignal_save_z1(self):
        # self.result_label = self.curr_label
        label = self.curr_label
        label["roll"] = label["roll"] - 5
        print(label)
        self.rb_clicked(label)
    def getSignal_save_z2(self):
        # self.result_label = self.curr_label
        label = self.curr_label
        label["roll"] = label["roll"] + 5
        print(label)
        self.rb_clicked(label)






class graphicsScene(QGraphicsScene):
    speakword = pyqtSignal()
    saveword = pyqtSignal()
    def __init__(self, parent=None):
        super(graphicsScene, self).__init__(parent)
        self.speakword.connect(window.getSignal_ref_stard)
        self.saveword.connect(window.getSignal_save_stard)
    def mouseMoveEvent(self, event):
        self.speakword.emit()
    def mousePressEvent(self, event):
        self.saveword.emit()

class graphicsScene_x1(QGraphicsScene):
    speakword = pyqtSignal()
    saveword = pyqtSignal()
    def __init__(self, parent=None):
        super(graphicsScene_x1, self).__init__(parent)
        self.speakword.connect(window.getSignal_ref_x1)
        self.saveword.connect(window.getSignal_save_x1)
    def mouseMoveEvent(self, event):
        self.speakword.emit()
    def mousePressEvent(self, event):
        self.saveword.emit()

class graphicsScene_x2(QGraphicsScene):
    speakword = pyqtSignal()
    saveword = pyqtSignal()
    def __init__(self, parent=None):
        super(graphicsScene_x2, self).__init__(parent)
        self.speakword.connect(window.getSignal_ref_x2)
        self.saveword.connect(window.getSignal_save_x2)
    def mouseMoveEvent(self, event):
        self.speakword.emit()
    def mousePressEvent(self, event):
        self.saveword.emit()

class graphicsScene_y1(QGraphicsScene):
    speakword = pyqtSignal()
    saveword = pyqtSignal()
    def __init__(self, parent=None):
        super(graphicsScene_y1, self).__init__(parent)
        self.speakword.connect(window.getSignal_ref_y1)
        self.saveword.connect(window.getSignal_save_y1)
    def mouseMoveEvent(self, event):
        self.speakword.emit()
    def mousePressEvent(self, event):
        self.saveword.emit()

class graphicsScene_y2(QGraphicsScene):
    speakword = pyqtSignal()
    saveword = pyqtSignal()
    def __init__(self, parent=None):
        super(graphicsScene_y2, self).__init__(parent)
        self.speakword.connect(window.getSignal_ref_y2)
        self.saveword.connect(window.getSignal_save_y2)
    def mouseMoveEvent(self, event):
        self.speakword.emit()
    def mousePressEvent(self, event):
        self.saveword.emit()

class graphicsScene_z1(QGraphicsScene):
    speakword = pyqtSignal()
    saveword = pyqtSignal()
    def __init__(self, parent=None):
        super(graphicsScene_z1, self).__init__(parent)
        self.speakword.connect(window.getSignal_ref_z1)
        self.saveword.connect(window.getSignal_save_z1)
    def mouseMoveEvent(self, event):
        self.speakword.emit()
    def mousePressEvent(self, event):
        self.saveword.emit()
class graphicsScene_z2(QGraphicsScene):
    speakword = pyqtSignal()
    saveword = pyqtSignal()
    def __init__(self, parent=None):
        super(graphicsScene_z2, self).__init__(parent)
        self.speakword.connect(window.getSignal_ref_z2)
        self.saveword.connect(window.getSignal_save_z2)
    def mouseMoveEvent(self, event):
        self.speakword.emit()
    def mousePressEvent(self, event):
        self.saveword.emit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())



