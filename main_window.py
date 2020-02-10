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
        self.status_bar = QtWidgets.QLabel("Please load the images")
        self.status_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.save_button = QtWidgets.QPushButton("Save")

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.status_bar)
        self.layout.addWidget(self.save_button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.SetInputDirectory)
        self.save_button.clicked.connect(self.SetPdfPath)

        self.OnImageDirSelected.connect(self.image_processor.ReadImages)
        self.OnPdfPathSelected.connect(self.image_processor.SaveToPdf)

    # signal
    OnImageDirSelected = QtCore.Signal(str)
    OnPdfPathSelected = QtCore.Signal(str)


    def SetInputDirectory(self):
        self.path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Images directory')
        self.OnImageDirSelected.emit(self.path)
        self.status_bar.setText('Images are loaded from ' + self.path)

    def SetPdfPath(self):
        self.out_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Pdf Location')
        self.OnPdfPathSelected.emit(self.out_path)
        self.status_bar.setText('Pdf file is saved under ' + self.out_path)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())