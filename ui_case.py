# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'case.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSplitter, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(404, 231)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.case_2 = QLabel(self.splitter)
        self.case_2.setObjectName(u"case_2")
        self.case_2.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.case_2)
        self.textEdit = QTextEdit(self.splitter)
        self.textEdit.setObjectName(u"textEdit")
        self.splitter.addWidget(self.textEdit)
        self.sure = QPushButton(self.splitter)
        self.sure.setObjectName(u"sure")
        self.splitter.addWidget(self.sure)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.comboBox = QComboBox(self.splitter_2)
        self.comboBox.setObjectName(u"comboBox")
        self.splitter_2.addWidget(self.comboBox)
        self.result = QLabel(self.splitter_2)
        self.result.setObjectName(u"result")
        self.result.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.result)
        self.go_query = QPushButton(self.splitter_2)
        self.go_query.setObjectName(u"go_query")
        self.splitter_2.addWidget(self.go_query)

        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.case_2.setText(QCoreApplication.translate("Form", u"\u75c5\u4f8b\uff1a", None))
        self.sure.setText(QCoreApplication.translate("Form", u"\u5b8c\u6210", None))
        self.result.setText("")
        self.go_query.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
    # retranslateUi

