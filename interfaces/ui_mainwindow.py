# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowMXFCnu.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(952, 555)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icones/py.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_Sair = QAction(MainWindow)
        self.action_Sair.setObjectName(u"action_Sair")
        icon1 = QIcon()
        icon1.addFile(u":/icones/close.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Sair.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(11, 83, 931, 419))
        self.tabExemplos1 = QWidget()
        self.tabExemplos1.setObjectName(u"tabExemplos1")
        self.groupBox = QGroupBox(self.tabExemplos1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 16, 271, 360))
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 251, 321))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btnDialogInfo = QPushButton(self.gridLayoutWidget)
        self.btnDialogInfo.setObjectName(u"btnDialogInfo")

        self.gridLayout.addWidget(self.btnDialogInfo, 4, 1, 1, 1)

        self.btnInputText = QPushButton(self.gridLayoutWidget)
        self.btnInputText.setObjectName(u"btnInputText")

        self.gridLayout.addWidget(self.btnInputText, 8, 1, 1, 1)

        self.btnInputInt = QPushButton(self.gridLayoutWidget)
        self.btnInputInt.setObjectName(u"btnInputInt")

        self.gridLayout.addWidget(self.btnInputInt, 9, 1, 1, 1)

        self.btnInputDouble = QPushButton(self.gridLayoutWidget)
        self.btnInputDouble.setObjectName(u"btnInputDouble")

        self.gridLayout.addWidget(self.btnInputDouble, 10, 1, 1, 1)

        self.btnDialogCustom = QPushButton(self.gridLayoutWidget)
        self.btnDialogCustom.setObjectName(u"btnDialogCustom")

        self.gridLayout.addWidget(self.btnDialogCustom, 0, 1, 1, 2)

        self.btnAbrirArquivo = QPushButton(self.gridLayoutWidget)
        self.btnAbrirArquivo.setObjectName(u"btnAbrirArquivo")

        self.gridLayout.addWidget(self.btnAbrirArquivo, 3, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)

        self.btnDialogSobreQt = QPushButton(self.gridLayoutWidget)
        self.btnDialogSobreQt.setObjectName(u"btnDialogSobreQt")

        self.gridLayout.addWidget(self.btnDialogSobreQt, 3, 1, 1, 1)

        self.btnDialogAlerta = QPushButton(self.gridLayoutWidget)
        self.btnDialogAlerta.setObjectName(u"btnDialogAlerta")

        self.gridLayout.addWidget(self.btnDialogAlerta, 6, 1, 1, 1)

        self.btnDialogQuestao = QPushButton(self.gridLayoutWidget)
        self.btnDialogQuestao.setObjectName(u"btnDialogQuestao")

        self.gridLayout.addWidget(self.btnDialogQuestao, 7, 1, 1, 1)

        self.btnDialogErro = QPushButton(self.gridLayoutWidget)
        self.btnDialogErro.setObjectName(u"btnDialogErro")

        self.gridLayout.addWidget(self.btnDialogErro, 5, 1, 1, 1)

        self.btnDialogSobre = QPushButton(self.gridLayoutWidget)
        self.btnDialogSobre.setObjectName(u"btnDialogSobre")

        self.gridLayout.addWidget(self.btnDialogSobre, 2, 1, 1, 1)

        self.btnSalvarArquivo = QPushButton(self.gridLayoutWidget)
        self.btnSalvarArquivo.setObjectName(u"btnSalvarArquivo")

        self.gridLayout.addWidget(self.btnSalvarArquivo, 4, 2, 1, 1)

        self.btnInputItem = QPushButton(self.gridLayoutWidget)
        self.btnInputItem.setObjectName(u"btnInputItem")

        self.gridLayout.addWidget(self.btnInputItem, 2, 2, 1, 1)

        self.lblFontesCores = QLabel(self.gridLayoutWidget)
        self.lblFontesCores.setObjectName(u"lblFontesCores")

        self.gridLayout.addWidget(self.lblFontesCores, 8, 2, 3, 1)

        self.btnDialogColors = QPushButton(self.gridLayoutWidget)
        self.btnDialogColors.setObjectName(u"btnDialogColors")

        self.gridLayout.addWidget(self.btnDialogColors, 7, 2, 1, 1)

        self.btnDialogFonts = QPushButton(self.gridLayoutWidget)
        self.btnDialogFonts.setObjectName(u"btnDialogFonts")

        self.gridLayout.addWidget(self.btnDialogFonts, 6, 2, 1, 1)

        self.btnEscolherPasta = QPushButton(self.gridLayoutWidget)
        self.btnEscolherPasta.setObjectName(u"btnEscolherPasta")

        self.gridLayout.addWidget(self.btnEscolherPasta, 5, 2, 1, 1)

        self.groupBox_2 = QGroupBox(self.tabExemplos1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(290, 16, 221, 361))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 201, 316))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnGravarArquivo = QPushButton(self.layoutWidget)
        self.btnGravarArquivo.setObjectName(u"btnGravarArquivo")

        self.verticalLayout.addWidget(self.btnGravarArquivo)

        self.btnLerArquivo = QPushButton(self.layoutWidget)
        self.btnLerArquivo.setObjectName(u"btnLerArquivo")

        self.verticalLayout.addWidget(self.btnLerArquivo)

        self.btnExcluirArquivo = QPushButton(self.layoutWidget)
        self.btnExcluirArquivo.setObjectName(u"btnExcluirArquivo")

        self.verticalLayout.addWidget(self.btnExcluirArquivo)

        self.btnRenomearAP = QPushButton(self.layoutWidget)
        self.btnRenomearAP.setObjectName(u"btnRenomearAP")

        self.verticalLayout.addWidget(self.btnRenomearAP)

        self.btnPastaHome = QPushButton(self.layoutWidget)
        self.btnPastaHome.setObjectName(u"btnPastaHome")

        self.verticalLayout.addWidget(self.btnPastaHome)

        self.btnPastaDocuments = QPushButton(self.layoutWidget)
        self.btnPastaDocuments.setObjectName(u"btnPastaDocuments")

        self.verticalLayout.addWidget(self.btnPastaDocuments)

        self.btnPastaAtual = QPushButton(self.layoutWidget)
        self.btnPastaAtual.setObjectName(u"btnPastaAtual")

        self.verticalLayout.addWidget(self.btnPastaAtual)

        self.btnCriarPasta = QPushButton(self.layoutWidget)
        self.btnCriarPasta.setObjectName(u"btnCriarPasta")

        self.verticalLayout.addWidget(self.btnCriarPasta)

        self.btnCriarPastas = QPushButton(self.layoutWidget)
        self.btnCriarPastas.setObjectName(u"btnCriarPastas")

        self.verticalLayout.addWidget(self.btnCriarPastas)

        self.btnExcluirPasta = QPushButton(self.layoutWidget)
        self.btnExcluirPasta.setObjectName(u"btnExcluirPasta")

        self.verticalLayout.addWidget(self.btnExcluirPasta)

        self.btnListDir = QPushButton(self.layoutWidget)
        self.btnListDir.setObjectName(u"btnListDir")

        self.verticalLayout.addWidget(self.btnListDir)

        self.groupBox_3 = QGroupBox(self.tabExemplos1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(520, 16, 171, 211))
        self.layoutWidget1 = QWidget(self.groupBox_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 151, 171))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnRandUniform = QPushButton(self.layoutWidget1)
        self.btnRandUniform.setObjectName(u"btnRandUniform")
        self.btnRandUniform.setFocusPolicy(Qt.WheelFocus)

        self.verticalLayout_2.addWidget(self.btnRandUniform)

        self.btnRandInt = QPushButton(self.layoutWidget1)
        self.btnRandInt.setObjectName(u"btnRandInt")

        self.verticalLayout_2.addWidget(self.btnRandInt)

        self.btnRandChoices = QPushButton(self.layoutWidget1)
        self.btnRandChoices.setObjectName(u"btnRandChoices")

        self.verticalLayout_2.addWidget(self.btnRandChoices)

        self.btnRandChoices2 = QPushButton(self.layoutWidget1)
        self.btnRandChoices2.setObjectName(u"btnRandChoices2")

        self.verticalLayout_2.addWidget(self.btnRandChoices2)

        self.btnRandShuffle = QPushButton(self.layoutWidget1)
        self.btnRandShuffle.setObjectName(u"btnRandShuffle")

        self.verticalLayout_2.addWidget(self.btnRandShuffle)

        self.btnRandSample = QPushButton(self.layoutWidget1)
        self.btnRandSample.setObjectName(u"btnRandSample")

        self.verticalLayout_2.addWidget(self.btnRandSample)

        self.groupBox_4 = QGroupBox(self.tabExemplos1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(520, 236, 171, 141))
        self.groupBox_5 = QGroupBox(self.tabExemplos1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(696, 16, 220, 361))
        self.layoutWidget2 = QWidget(self.groupBox_5)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 30, 200, 142))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnLoterias = QPushButton(self.layoutWidget2)
        self.btnLoterias.setObjectName(u"btnLoterias")

        self.verticalLayout_3.addWidget(self.btnLoterias)

        self.btnSistemaOperacional = QPushButton(self.layoutWidget2)
        self.btnSistemaOperacional.setObjectName(u"btnSistemaOperacional")

        self.verticalLayout_3.addWidget(self.btnSistemaOperacional)

        self.btnDataHoraSistema = QPushButton(self.layoutWidget2)
        self.btnDataHoraSistema.setObjectName(u"btnDataHoraSistema")

        self.verticalLayout_3.addWidget(self.btnDataHoraSistema)

        self.btnAbrirSegundoForm = QPushButton(self.layoutWidget2)
        self.btnAbrirSegundoForm.setObjectName(u"btnAbrirSegundoForm")

        self.verticalLayout_3.addWidget(self.btnAbrirSegundoForm)

        self.btnParaTestes = QPushButton(self.layoutWidget2)
        self.btnParaTestes.setObjectName(u"btnParaTestes")

        self.verticalLayout_3.addWidget(self.btnParaTestes)

        self.tabWidget.addTab(self.tabExemplos1, "")
        self.tabExemplos2 = QWidget()
        self.tabExemplos2.setObjectName(u"tabExemplos2")
        self.tabWidget.addTab(self.tabExemplos2, "")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 961, 71))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(112, 7, 311, 51))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 11, 50, 50))
        self.label_2.setPixmap(QPixmap(u":/imagens/python_50px.png"))
        self.label_2.setScaledContents(False)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(77, 30, 24, 24))
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255,0.9);")
        self.label_4.setPixmap(QPixmap(u":/icones/qt_32px.png"))
        self.label_4.setScaledContents(True)
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 952, 22))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menuArquivo.addAction(self.action_Sair)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Python Examples", None))
        self.action_Sair.setText(QCoreApplication.translate("MainWindow", u"&Sair", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Caixas de Di\u00e1logo", None))
#if QT_CONFIG(statustip)
        self.btnDialogInfo.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de di\u00e1logo de \"Informa\u00e7\u00e3o\"", None))
#endif // QT_CONFIG(statustip)
        self.btnDialogInfo.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00e3o", None))
#if QT_CONFIG(statustip)
        self.btnInputText.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de entrada de \"Texto\"", None))
#endif // QT_CONFIG(statustip)
        self.btnInputText.setText(QCoreApplication.translate("MainWindow", u"Input Text", None))
#if QT_CONFIG(statustip)
        self.btnInputInt.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de entrada de \"N\u00fameros Inteiros\"", None))
#endif // QT_CONFIG(statustip)
        self.btnInputInt.setText(QCoreApplication.translate("MainWindow", u"Input Int", None))
#if QT_CONFIG(statustip)
        self.btnInputDouble.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de entrada de \"N\u00fameros Decimais\"", None))
#endif // QT_CONFIG(statustip)
        self.btnInputDouble.setText(QCoreApplication.translate("MainWindow", u"Input Double", None))
#if QT_CONFIG(statustip)
        self.btnDialogCustom.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de di\u00e1logo personalizada", None))
#endif // QT_CONFIG(statustip)
        self.btnDialogCustom.setText(QCoreApplication.translate("MainWindow", u"Di\u00e1logo Personalizado", None))
#if QT_CONFIG(statustip)
        self.btnAbrirArquivo.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de di\u00e1logo de \"Abrir Arquivo\"", None))
#endif // QT_CONFIG(statustip)
        self.btnAbrirArquivo.setText(QCoreApplication.translate("MainWindow", u"Abrir Arquivo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#0277bd;\">Pr\u00e9-definidos</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.btnDialogSobreQt.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de di\u00e1logo \"Sobre Qt\"", None))
#endif // QT_CONFIG(statustip)
        self.btnDialogSobreQt.setText(QCoreApplication.translate("MainWindow", u"Sobre Qt", None))
#if QT_CONFIG(statustip)
        self.btnDialogAlerta.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de di\u00e1logo de \"Alerta\"", None))
#endif // QT_CONFIG(statustip)
        self.btnDialogAlerta.setText(QCoreApplication.translate("MainWindow", u"Alerta", None))
#if QT_CONFIG(statustip)
        self.btnDialogQuestao.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de di\u00e1logo de \"Pergunta\"", None))
#endif // QT_CONFIG(statustip)
        self.btnDialogQuestao.setText(QCoreApplication.translate("MainWindow", u"Quest\u00e3o", None))
#if QT_CONFIG(statustip)
        self.btnDialogErro.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de di\u00e1logo de \"Erro\"", None))
#endif // QT_CONFIG(statustip)
        self.btnDialogErro.setText(QCoreApplication.translate("MainWindow", u"Erro", None))
#if QT_CONFIG(statustip)
        self.btnDialogSobre.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de di\u00e1logo \"Sobre\"", None))
#endif // QT_CONFIG(statustip)
        self.btnDialogSobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
#if QT_CONFIG(statustip)
        self.btnSalvarArquivo.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de di\u00e1logo de \"Salvar Arquivo\"", None))
#endif // QT_CONFIG(statustip)
        self.btnSalvarArquivo.setText(QCoreApplication.translate("MainWindow", u"Salvar Arquivo", None))
#if QT_CONFIG(statustip)
        self.btnInputItem.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de escolha de um \"Item\"", None))
#endif // QT_CONFIG(statustip)
        self.btnInputItem.setText(QCoreApplication.translate("MainWindow", u"Input Item", None))
#if QT_CONFIG(statustip)
        self.lblFontesCores.setStatusTip(QCoreApplication.translate("MainWindow", u"Utilize os bot\u00f5es \"Fontes\" e \"C\u00f4res\" para me estilizar", None))
#endif // QT_CONFIG(statustip)
        self.lblFontesCores.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Eu sou<br>um simples<br>texto.</p></body></html>", None))
#if QT_CONFIG(statustip)
        self.btnDialogColors.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de di\u00e1logo de \"C\u00f4res\"", None))
#endif // QT_CONFIG(statustip)
        self.btnDialogColors.setText(QCoreApplication.translate("MainWindow", u"C\u00f4res", None))
#if QT_CONFIG(statustip)
        self.btnDialogFonts.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de caixa de di\u00e1logo de \"Fontes do Sistema\"", None))
#endif // QT_CONFIG(statustip)
        self.btnDialogFonts.setText(QCoreApplication.translate("MainWindow", u"Fontes", None))
#if QT_CONFIG(statustip)
        self.btnEscolherPasta.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de escolha de uma pasta do sistema", None))
#endif // QT_CONFIG(statustip)
        self.btnEscolherPasta.setText(QCoreApplication.translate("MainWindow", u"Escolher Pasta", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Pastas e Arquivos", None))
#if QT_CONFIG(statustip)
        self.btnGravarArquivo.setStatusTip(QCoreApplication.translate("MainWindow", u"Grava um arquivo de texto no diret\u00f3rio do programa", None))
#endif // QT_CONFIG(statustip)
        self.btnGravarArquivo.setText(QCoreApplication.translate("MainWindow", u"Gravar Arquivo", None))
#if QT_CONFIG(statustip)
        self.btnLerArquivo.setStatusTip(QCoreApplication.translate("MainWindow", u"L\u00ea um arquivo de texto no diret\u00f3rio do programa", None))
#endif // QT_CONFIG(statustip)
        self.btnLerArquivo.setText(QCoreApplication.translate("MainWindow", u"Ler Arquivo", None))
#if QT_CONFIG(statustip)
        self.btnExcluirArquivo.setStatusTip(QCoreApplication.translate("MainWindow", u"Exclui um arquivo de texto no diret\u00f3rio do programa", None))
#endif // QT_CONFIG(statustip)
        self.btnExcluirArquivo.setText(QCoreApplication.translate("MainWindow", u"Excluir Arquivo", None))
        self.btnRenomearAP.setText(QCoreApplication.translate("MainWindow", u"Renomear Arq/Pasta", None))
#if QT_CONFIG(statustip)
        self.btnPastaHome.setStatusTip(QCoreApplication.translate("MainWindow", u"Caminho da pasta \"home\" do sistema", None))
#endif // QT_CONFIG(statustip)
        self.btnPastaHome.setText(QCoreApplication.translate("MainWindow", u"Pasta \"Home\"", None))
#if QT_CONFIG(statustip)
        self.btnPastaDocuments.setStatusTip(QCoreApplication.translate("MainWindow", u"Caminho da pasta \"Documentos\" do sistema", None))
#endif // QT_CONFIG(statustip)
        self.btnPastaDocuments.setText(QCoreApplication.translate("MainWindow", u"Pasta \"Documents e Desktop\"", None))
#if QT_CONFIG(statustip)
        self.btnPastaAtual.setStatusTip(QCoreApplication.translate("MainWindow", u"Caminho da pasta de onde o programa est\u00e1 sendo executado", None))
#endif // QT_CONFIG(statustip)
        self.btnPastaAtual.setText(QCoreApplication.translate("MainWindow", u"Pasta Atual", None))
#if QT_CONFIG(statustip)
        self.btnCriarPasta.setStatusTip(QCoreApplication.translate("MainWindow", u"Cria uma pasta", None))
#endif // QT_CONFIG(statustip)
        self.btnCriarPasta.setText(QCoreApplication.translate("MainWindow", u"Criar Pasta", None))
#if QT_CONFIG(statustip)
        self.btnCriarPastas.setStatusTip(QCoreApplication.translate("MainWindow", u"Cria mais de uma pasta simultaneamente", None))
#endif // QT_CONFIG(statustip)
        self.btnCriarPastas.setText(QCoreApplication.translate("MainWindow", u"Criar Pastas", None))
#if QT_CONFIG(statustip)
        self.btnExcluirPasta.setStatusTip(QCoreApplication.translate("MainWindow", u"Exclui as pastas criadas atrav\u00e9s do dois bot\u00f5es acima, caso existam.", None))
#endif // QT_CONFIG(statustip)
        self.btnExcluirPasta.setText(QCoreApplication.translate("MainWindow", u"Excluir Pastas Criadas", None))
#if QT_CONFIG(statustip)
        self.btnListDir.setStatusTip(QCoreApplication.translate("MainWindow", u"Lista pastas e arquivos de um diret\u00f3rio", None))
#endif // QT_CONFIG(statustip)
        self.btnListDir.setText(QCoreApplication.translate("MainWindow", u"Listar Diret\u00f3rio", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Random", None))
#if QT_CONFIG(statustip)
        self.btnRandUniform.setStatusTip(QCoreApplication.translate("MainWindow", u"Gera um valor decimal do m\u00ednimo ao m\u00e1ximo", None))
#endif // QT_CONFIG(statustip)
        self.btnRandUniform.setText(QCoreApplication.translate("MainWindow", u"Random Uniform", None))
#if QT_CONFIG(statustip)
        self.btnRandInt.setStatusTip(QCoreApplication.translate("MainWindow", u"Gera um valor inteiro do m\u00ednimo ao m\u00e1ximo", None))
#endif // QT_CONFIG(statustip)
        self.btnRandInt.setText(QCoreApplication.translate("MainWindow", u"Random Int", None))
#if QT_CONFIG(statustip)
        self.btnRandChoices.setStatusTip(QCoreApplication.translate("MainWindow", u"Escolhe uma op\u00e7\u00e3o aleat\u00f3ria", None))
#endif // QT_CONFIG(statustip)
        self.btnRandChoices.setText(QCoreApplication.translate("MainWindow", u"Random Choices", None))
#if QT_CONFIG(statustip)
        self.btnRandChoices2.setStatusTip(QCoreApplication.translate("MainWindow", u"Escolhe duas op\u00e7\u00f5es aleat\u00f3rias", None))
#endif // QT_CONFIG(statustip)
        self.btnRandChoices2.setText(QCoreApplication.translate("MainWindow", u"Random Choices 2", None))
#if QT_CONFIG(statustip)
        self.btnRandShuffle.setStatusTip(QCoreApplication.translate("MainWindow", u"Embaralha uma lista de op\u00e7\u00f5es", None))
#endif // QT_CONFIG(statustip)
        self.btnRandShuffle.setText(QCoreApplication.translate("MainWindow", u"Random Shuffle", None))
#if QT_CONFIG(statustip)
        self.btnRandSample.setStatusTip(QCoreApplication.translate("MainWindow", u"Escolhe aleatoriamente mais de um elemento de uma lista sem repetir elementos.", None))
#endif // QT_CONFIG(statustip)
        self.btnRandSample.setText(QCoreApplication.translate("MainWindow", u"Random Sample", None))
        self.groupBox_4.setTitle("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Outros", None))
#if QT_CONFIG(statustip)
        self.btnLoterias.setStatusTip(QCoreApplication.translate("MainWindow", u"Obtenha palpites para v\u00e1rios jogos da loteria", None))
#endif // QT_CONFIG(statustip)
        self.btnLoterias.setText(QCoreApplication.translate("MainWindow", u"Loterias", None))
#if QT_CONFIG(statustip)
        self.btnSistemaOperacional.setStatusTip(QCoreApplication.translate("MainWindow", u"Mostra o sistema operacional atual", None))
#endif // QT_CONFIG(statustip)
        self.btnSistemaOperacional.setText(QCoreApplication.translate("MainWindow", u"Sistema Operacional", None))
#if QT_CONFIG(statustip)
        self.btnDataHoraSistema.setStatusTip(QCoreApplication.translate("MainWindow", u"Exibe data e hora do sistema no formato local", None))
#endif // QT_CONFIG(statustip)
        self.btnDataHoraSistema.setText(QCoreApplication.translate("MainWindow", u"Data e Hora do Sistema", None))
#if QT_CONFIG(statustip)
        self.btnAbrirSegundoForm.setStatusTip(QCoreApplication.translate("MainWindow", u"Exemplo de um segundo formul\u00e1rio", None))
#endif // QT_CONFIG(statustip)
        self.btnAbrirSegundoForm.setText(QCoreApplication.translate("MainWindow", u"Abrir Segundo Form", None))
#if QT_CONFIG(statustip)
        self.btnParaTestes.setStatusTip(QCoreApplication.translate("MainWindow", u"Bot\u00e3o sem fun\u00e7\u00e3o espec\u00edfica, apenas para testes diversos", None))
#endif // QT_CONFIG(statustip)
        self.btnParaTestes.setText(QCoreApplication.translate("MainWindow", u"Testes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExemplos1), QCoreApplication.translate("MainWindow", u"Exemplos 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExemplos2), QCoreApplication.translate("MainWindow", u"Exemplos 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:700; color:#0277bd;\">Python Examples</span></p></body></html>", None))
        self.label_2.setText("")
        self.label_4.setText("")
        self.menuArquivo.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
    # retranslateUi

