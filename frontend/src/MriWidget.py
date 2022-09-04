from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QPushButton, QListWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import os
from Component import Component


class MriWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.path = ""
        self.left_top_img = QPixmap(self.path)
        self.layout = QHBoxLayout()
        self.data = Component()
        self.pat_img_layout = QVBoxLayout()
        self.pat_img = QListWidget()
        self.pat_but = QPushButton('Refresh', self)
        self.pat_but.clicked.connect(self.showimg)
        self.pat_img.itemDoubleClicked.connect(self.showimg)
        self.pat_img_layout.addWidget(self.pat_img)
        self.pat_img_layout.addWidget(self.pat_but)

        self.left_layout = QVBoxLayout()
        self.left_top = QLabel()
        self.left_top.setAlignment(Qt.AlignCenter)
        self.left_top.setFrameShape(QFrame.StyledPanel)
        self.left_top_B = QPushButton('MRI', self)
        self.left_top_B.clicked.connect(self.backendapi_mri)

        self.left_down_img = QPixmap(self.path)
        self.left_down = QLabel()
        self.left_down.setAlignment(Qt.AlignCenter)
        self.left_down.setFrameShape(QFrame.StyledPanel)
        self.left_down_B = QPushButton('Enhancement MRI', self)
        self.left_down_B.clicked.connect(self.backendapi_eh)

        self.left_layout.addWidget(self.left_top)
        self.left_layout.addWidget(self.left_top_B)
        self.left_layout.addWidget(self.left_down)
        self.left_layout.addWidget(self.left_down_B)

        self.right_layout = QVBoxLayout()
        self.right_top_img = QPixmap(self.path)
        self.right_top = QLabel()
        self.right_top.setAlignment(Qt.AlignCenter)
        self.right_top.setFrameShape(QFrame.StyledPanel)
        self.right_top_B = QPushButton('Predict SCT', self)
        self.right_top_B.clicked.connect(self.backendapi_sct)

        self.right_down_img = QPixmap(self.path)
        self.right_down = QLabel()
        self.right_down.setAlignment(Qt.AlignCenter)
        self.right_down.setFrameShape(QFrame.StyledPanel)
        self.right_down_B = QPushButton('Predict eSCT', self)
        self.right_down_B.clicked.connect(self.backendapi_esct)

        self.right_layout.addWidget(self.right_top)
        self.right_layout.addWidget(self.right_top_B)
        self.right_layout.addWidget(self.right_down)
        self.right_layout.addWidget(self.right_down_B)

        self.layout.addLayout(self.pat_img_layout, 4)
        self.layout.addLayout(self.left_layout, 4)
        self.layout.addLayout(self.right_layout, 4)
        self.setLayout(self.layout)

        self.dic_list = list()

    def backendapi_mri(self):
        os.system('/home/wyjang/IdeaProjects/cbnuh/backend/bin/input.sh ' +
                  '/home/wyjang/IdeaProjects/cbnuh/data/' + self.data.patient + ' ' +
                  '/home/wyjang/IdeaProjects/cbnuh/backend/sct_tmp/raw/' + self.data.patient + ' ' +
                  '/home/wyjang/IdeaProjects/cbnuh/frontend/tmp/' + self.data.patient + '/mri')

    def backendapi_sct(self):
        os.system('/home/wyjang/IdeaProjects/cbnuh/backend/bin/sct_run.sh ' + self.data.patient)
        os.system('/home/wyjang/IdeaProjects/cbnuh/backend/bin/output.sh ' +
                  '/home/wyjang/IdeaProjects/cbnuh/backend/sct_tmp/test/' + self.data.patient + ' ' +
                  '/home/wyjang/IdeaProjects/cbnuh/frontend/tmp/' + self.data.patient + '/sct')

    def backendapi_eh(self):
        os.system('/home/wyjang/IdeaProjects/cbnuh/backend/bin/eh_run.sh ' + self.data.patient)
        os.system('/home/wyjang/IdeaProjects/cbnuh/backend/bin/output.sh ' +
                  '/home/wyjang/IdeaProjects/cbnuh/backend/eh_tmp/test/' + self.data.patient + ' ' +
                  '/home/wyjang/IdeaProjects/cbnuh/frontend/tmp/' + self.data.patient + '/emri')

    def backendapi_esct(self):
        os.system('/home/wyjang/IdeaProjects/cbnuh/backend/bin/input_esct.sh ' +
                  '/home/wyjang/IdeaProjects/cbnuh/frontend/tmp/' + self.data.patient + '/emri ' +
                  '/home/wyjang/IdeaProjects/cbnuh/backend/esct_tmp/raw/' + self.data.patient)
        os.system('/home/wyjang/IdeaProjects/cbnuh/backend/bin/esct_run.sh ' + self.data.patient)
        os.system('/home/wyjang/IdeaProjects/cbnuh/backend/bin/output.sh ' +
                  '/home/wyjang/IdeaProjects/cbnuh/backend/esct_tmp/test/' + self.data.patient + ' ' +
                  '/home/wyjang/IdeaProjects/cbnuh/frontend/tmp/' + self.data.patient + '/esct')

    def showimg(self):
        self.left_top.clear()
        self.left_down.clear()
        self.right_top.clear()
        self.right_down.clear()
        pat = self.data.patient
        img_text = self.pat_img.currentItem().text()
        self.data.mri_temp_path_frontend_jpg = self.data.try_path + '/' + pat + '/mri/' + img_text + '.jpg'
        self.data.sct_temp_path_frontend_jpg = self.data.try_path + '/' + pat + '/sct/' + img_text + '.jpg'
        self.data.eh_temp_path_frontend_jpg = self.data.try_path + '/' + pat + '/emri/' + img_text + '.jpg'
        self.data.esct_temp_path_frontend_jpg = self.data.try_path + '/' + pat + '/esct/' + img_text + '.jpg'

        self.left_top_img = QPixmap(self.data.mri_temp_path_frontend_jpg)
        w = self.left_top.width() - 10
        h = self.left_top.height() - 10
        left_top_img_resized = self.left_top_img.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.left_top.setPixmap(left_top_img_resized)

        self.right_top_img = QPixmap(self.data.sct_temp_path_frontend_jpg)
        w = self.right_top.width() - 10
        h = self.right_top.height() - 10
        right_top_img_resized = self.right_top_img.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.right_top.setPixmap(right_top_img_resized)

        self.left_down_img = QPixmap(self.data.eh_temp_path_frontend_jpg)
        w = self.left_down.width() - 10
        h = self.left_down.height() - 10
        left_down_img_resized = self.left_down_img.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.left_down.setPixmap(left_down_img_resized)

        self.right_down_img = QPixmap(self.data.esct_temp_path_frontend_jpg)
        w = self.right_down.width() - 10
        h = self.right_down.height() - 10
        right_down_img_resized = self.right_down_img.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.right_down.setPixmap(right_down_img_resized)

    def getdicomlist(self):
        self.dic_list = os.listdir('/home/wyjang/IdeaProjects/cbnuh/data/' + self.data.patient)
        self.pat_img.clear()
        for i in self.dic_list:
            self.pat_img.addItem(i)
