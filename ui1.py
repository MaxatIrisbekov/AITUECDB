# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 720)
        Form.setMinimumSize(QSize(500, 720))
        Form.setMaximumSize(QSize(500, 720))
        icon = QIcon()
        icon.addFile(u"database.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-color: rgb(1, 44, 55);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 0, -1, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setPixmap(QPixmap(u"AITU.jpg"))

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.add_or_change_btn = QPushButton(Form)
        self.add_or_change_btn.setObjectName(u"add_or_change_btn")
        self.add_or_change_btn.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.add_or_change_btn.setFont(font)
        self.add_or_change_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_or_change_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(58, 160, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(142, 157, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	\n"
"	background-color: rgb(0, 255, 255);\n"
"}")

        self.verticalLayout.addWidget(self.add_or_change_btn)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_line_edit = QLineEdit(Form)
        self.search_line_edit.setObjectName(u"search_line_edit")
        self.search_line_edit.setMinimumSize(QSize(0, 25))
        self.search_line_edit.setMaximumSize(QSize(400, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.search_line_edit.setFont(font1)
        self.search_line_edit.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(204, 204, 204);\n"
"}")
        self.search_line_edit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.search_line_edit)

        self.search_btn = QPushButton(Form)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(0, 25))
        font2 = QFont()
        font2.setPointSize(10)
        self.search_btn.setFont(font2)
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(58, 160, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(142, 157, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	\n"
"	background-color: rgb(0, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons8-search-more-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.search_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.info_text_edit = QTextEdit(Form)
        self.info_text_edit.setObjectName(u"info_text_edit")
        font3 = QFont()
        font3.setPointSize(16)
        self.info_text_edit.setFont(font3)
        self.info_text_edit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.info_text_edit.setStyleSheet(u"border: none;\n"
"color: white;\n"
"")

        self.verticalLayout.addWidget(self.info_text_edit)

        self.delete_btn = QPushButton(Form)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMinimumSize(QSize(0, 25))
        self.delete_btn.setFont(font1)
        self.delete_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(150, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons8-delete-trash-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn.setIcon(icon2)
        self.delete_btn.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.delete_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"English Course DB", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#b0c8e2;\">AITU</span></p><p align=\"center\"><span style=\" font-size:20pt; color:#b0c8e2;\">English Course</span></p><p align=\"center\"><span style=\" font-size:20pt; color:#b0c8e2;\">Database</span></p><p align=\"right\"><span style=\" font-size:10pt; font-weight:600; color:#939393;\">by Maxat Irisbekov</span></p></body></html>", None))
        self.add_or_change_btn.setText(QCoreApplication.translate("Form", u"  Add / Change", None))
        self.search_line_edit.setText("")
        self.search_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter full name to search", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.info_text_edit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_text_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Searching results:", None))
        self.delete_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

