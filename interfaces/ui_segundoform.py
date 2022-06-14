# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'segundoformQejvtR.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
import resources_rc

class Ui_frmSegundoForm(object):
    def setupUi(self, frmSegundoForm):
        if not frmSegundoForm.objectName():
            frmSegundoForm.setObjectName(u"frmSegundoForm")
        frmSegundoForm.setWindowModality(Qt.WindowModal)
        frmSegundoForm.resize(390, 244)
        icon = QIcon()
        icon.addFile(u":/icones/py.ico", QSize(), QIcon.Normal, QIcon.Off)
        frmSegundoForm.setWindowIcon(icon)
        self.btnSegFormClose = QPushButton(frmSegundoForm)
        self.btnSegFormClose.setObjectName(u"btnSegFormClose")
        self.btnSegFormClose.setGeometry(QRect(284, 210, 91, 24))
        icon1 = QIcon()
        icon1.addFile(u":/icones/close.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSegFormClose.setIcon(icon1)
        self.label = QLabel(frmSegundoForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 341, 91))

        self.retranslateUi(frmSegundoForm)

        QMetaObject.connectSlotsByName(frmSegundoForm)
    # setupUi

    def retranslateUi(self, frmSegundoForm):
        frmSegundoForm.setWindowTitle(QCoreApplication.translate("frmSegundoForm", u"Form", None))
        self.btnSegFormClose.setText(QCoreApplication.translate("frmSegundoForm", u"Fechar", None))
        self.label.setText(QCoreApplication.translate("frmSegundoForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#55aaff;\">Segundo Form</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#55aaff;\">ApplicationModal</span></p></body></html>", None))
    # retranslateUi

