# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui2.ui'
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
        Form.resize(375, 250)
        Form.setMinimumSize(QSize(375, 250))
        Form.setMaximumSize(QSize(375, 250))
        Form.setStyleSheet(u"background-color: rgb(0, 43, 54);")
        self.fullname_line_edit = QLineEdit(Form)
        self.fullname_line_edit.setObjectName(u"fullname_line_edit")
        self.fullname_line_edit.setGeometry(QRect(10, 10, 353, 31))
        self.fullname_line_edit.setMinimumSize(QSize(353, 0))
        font = QFont()
        font.setPointSize(12)
        self.fullname_line_edit.setFont(font)
        self.fullname_line_edit.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(0, 82, 102);\n"
"color: white;")
        self.fullname_line_edit.setClearButtonEnabled(True)
        self.date_line_edit = QLineEdit(Form)
        self.date_line_edit.setObjectName(u"date_line_edit")
        self.date_line_edit.setGeometry(QRect(10, 90, 141, 31))
        self.date_line_edit.setFont(font)
        self.date_line_edit.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(0, 82, 102);color:white;")
        self.date_line_edit.setClearButtonEnabled(True)
        self.date_came_btn = QPushButton(Form)
        self.date_came_btn.setObjectName(u"date_came_btn")
        self.date_came_btn.setGeometry(QRect(210, 90, 75, 31))
        self.date_came_btn.setFont(font)
        self.date_came_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_came_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 85, 255);\n"
"}")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 210, 101, 31))
        self.course_line_edit = QLineEdit(Form)
        self.course_line_edit.setObjectName(u"course_line_edit")
        self.course_line_edit.setGeometry(QRect(10, 50, 353, 31))
        self.course_line_edit.setMinimumSize(QSize(353, 0))
        self.course_line_edit.setFont(font)
        self.course_line_edit.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(0, 82, 102);\n"
"color: white;")
        self.course_line_edit.setClearButtonEnabled(True)
        self.lvl_line_edit = QLineEdit(Form)
        self.lvl_line_edit.setObjectName(u"lvl_line_edit")
        self.lvl_line_edit.setGeometry(QRect(10, 130, 141, 31))
        self.lvl_line_edit.setFont(font)
        self.lvl_line_edit.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(0, 82, 102);color:white;")
        self.lvl_line_edit.setClearButtonEnabled(True)
        self.current_lvl_line_edit = QLineEdit(Form)
        self.current_lvl_line_edit.setObjectName(u"current_lvl_line_edit")
        self.current_lvl_line_edit.setGeometry(QRect(10, 170, 353, 31))
        self.current_lvl_line_edit.setMinimumSize(QSize(353, 0))
        self.current_lvl_line_edit.setFont(font)
        self.current_lvl_line_edit.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(0, 82, 102);\n"
"color: white;")
        self.current_lvl_line_edit.setClearButtonEnabled(True)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 130, 41, 31))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 90, 41, 31))
        self.label_5.setFont(font)
        self.date_left_btn = QPushButton(Form)
        self.date_left_btn.setObjectName(u"date_left_btn")
        self.date_left_btn.setGeometry(QRect(290, 90, 75, 31))
        self.date_left_btn.setFont(font)
        self.date_left_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_left_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 85, 255);\n"
"}")
        self.lvl_came_btn = QPushButton(Form)
        self.lvl_came_btn.setObjectName(u"lvl_came_btn")
        self.lvl_came_btn.setGeometry(QRect(210, 130, 75, 31))
        self.lvl_came_btn.setFont(font)
        self.lvl_came_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.lvl_came_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 85, 255);\n"
"}")
        self.lvl_left_btn = QPushButton(Form)
        self.lvl_left_btn.setObjectName(u"lvl_left_btn")
        self.lvl_left_btn.setGeometry(QRect(290, 130, 75, 31))
        self.lvl_left_btn.setFont(font)
        self.lvl_left_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.lvl_left_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 85, 255);\n"
"}")
        self.on_studying_true_btn = QPushButton(Form)
        self.on_studying_true_btn.setObjectName(u"on_studying_true_btn")
        self.on_studying_true_btn.setGeometry(QRect(110, 210, 75, 31))
        self.on_studying_true_btn.setFont(font)
        self.on_studying_true_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.on_studying_true_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 85, 255);\n"
"}")
        self.on_studying_false_btn = QPushButton(Form)
        self.on_studying_false_btn.setObjectName(u"on_studying_false_btn")
        self.on_studying_false_btn.setGeometry(QRect(190, 210, 75, 31))
        self.on_studying_false_btn.setFont(font)
        self.on_studying_false_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.on_studying_false_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 85, 255);\n"
"}")
        self.add_or_change_btn = QPushButton(Form)
        self.add_or_change_btn.setObjectName(u"add_or_change_btn")
        self.add_or_change_btn.setGeometry(QRect(290, 210, 75, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.add_or_change_btn.setFont(font1)
        self.add_or_change_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_or_change_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 85, 255);\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.fullname_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter full name", None))
        self.date_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Date", None))
        self.date_came_btn.setText(QCoreApplication.translate("Form", u"Came", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">On studying:</span></p></body></html>", None))
        self.course_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter course", None))
        self.lvl_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Level", None))
        self.current_lvl_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Current level", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ffffff;\">when</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ffffff;\">when</span></p></body></html>", None))
        self.date_left_btn.setText(QCoreApplication.translate("Form", u"Left", None))
        self.lvl_came_btn.setText(QCoreApplication.translate("Form", u"Came", None))
        self.lvl_left_btn.setText(QCoreApplication.translate("Form", u"Left", None))
        self.on_studying_true_btn.setText(QCoreApplication.translate("Form", u"True", None))
        self.on_studying_false_btn.setText(QCoreApplication.translate("Form", u"False", None))
        self.add_or_change_btn.setText(QCoreApplication.translate("Form", u"Add/Change", None))
    # retranslateUi

