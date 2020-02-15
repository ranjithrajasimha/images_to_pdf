#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 23:05:08 2020

@author: ranjith
"""


import sys
from PySide2 import QtCore, QtWidgets, QtGui
from image_to_pdf import Image2Pdf

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.image_processor = Image2Pdf()
        self.button = QtWidgets.QPushButton("Load Images")
        self.rotate_left_button = QtWidgets.QPushButton("<-")
        self.rotate_right_button = QtWidgets.QPushButton("/")
        self.save_button = QtWidgets.QPushButton("Save as Pdf")

        self.contrast = QtWidgets.QSlider(QtCore.Qt.Horizontal)

        self.status_bar = QtWidgets.QLabel("Please load the image")
        
        self.image_widget = QtWidgets.QLabel()
        self.image_widget.setFixedSize(300,300)
        # self.status_bar.setAlignment(QtCore.Qt.AlignCenter)

        self.vlayout = QtWidgets.QVBoxLayout()
        self.grid_layout = QtWidgets.QGridLayout()
        self.main_layout = QtWidgets.QHBoxLayout()

        self.grid_layout.addWidget(self.rotate_left_button, 1, 0)
        self.grid_layout.addWidget(self.rotate_right_button, 1, 1)

        self.vlayout.addWidget(self.button)
        self.vlayout.addLayout(self.grid_layout)
        self.vlayout.addWidget(self.contrast)
        self.vlayout.addWidget(self.save_button)
        # self.vlayout.addWidget(self.status_bar)

        self.main_layout.addWidget(self.image_widget)
        self.main_layout.addLayout(self.vlayout)

        self.setLayout(self.main_layout)

        self.button.clicked.connect(self.SetInputDirectory)
        self.save_button.clicked.connect(self.SetPdfPath)

        self.OnImageDirSelected.connect(self.image_processor.ReadImages)
        self.OnPdfPathSelected.connect(self.image_processor.SaveToPdf)

    # signal
    OnImageDirSelected = QtCore.Signal(str)
    OnPdfPathSelected = QtCore.Signal(str)


    def SetInputDirectory(self):
        # self.path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Images directory')
        self.path = QtWidgets.QFileDialog.getOpenFileName(self, caption='Select Image', dir="/home/ranjith/Documents", filter='Image Files ( *.png *.jpg )')
        self.OnImageDirSelected.emit(self.path[0])
        self.image_widget.setPixmap(QtGui.QPixmap.fromImage(self.image_processor.GetImages()))
        self.status_bar.setText('Image: ' + self.path[0])

    def SetPdfPath(self):
        file_extension = ".pdf"
        self.out_path = self.path[0].replace(".jpg", "").replace(".png", "") + file_extension
        self.OnPdfPathSelected.emit(self.out_path)
        self.status_bar.setText('Pdf file is saved under ' + self.out_path)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec_())