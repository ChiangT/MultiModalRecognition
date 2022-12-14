# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignRecognition_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1202, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1152, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1534, 900))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/result.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow{border-image: url(:/newPrefix/images_test/back.png);}\n"
"\n"
"#QInputDialog{border-image: url(:/newPrefix/images_test/light.png);}\n"
"\n"
"QLabel{border:5px;}\n"
"QLabel::hover {\n"
"border:0px;}\n"
"\n"
"QMenuBar{border-color:transparent;}\n"
"QToolButton[objectName=pushButton_doIt]{\n"
"border:5px;}\n"
"\n"
"QToolButton[objectName=pushButton_doIt]:hover {\n"
"image:url(:/newPrefix/images_test/run_hover.png);}\n"
"\n"
"QToolButton[objectName=pushButton_doIt]:pressed {\n"
"image:url(:/newPrefix/images_test/run_pressed.png);}\n"
"\n"
"QScrollBar:vertical{\n"
"background:transparent;\n"
"padding:2px;\n"
"border-radius:4px;\n"
"max-width:8px;}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background:#9acd32;\n"
"min-height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background:#9eb764;}\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"background:#9eb764;\n"
"}\n"
"QScrollBar::add-page:vertical{\n"
"background:none;\n"
"}\n"
"                               \n"
"QScrollBar::sub-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"background:none;}\n"
"                                 \n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"QScrollArea{\n"
"border:0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"background:transparent;\n"
"padding:0px;\n"
"border-radius:4px;\n"
"max-height:6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"background:#9acd32;\n"
"min-width:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"background:#9eb764;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"background:#9eb764;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal{\n"
"background:none;\n"
"}\n"
"QScrollBar::add-line:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"background:none;\n"
"}\n"
"QToolButton::hover{\n"
"border:0px;\n"
"} ")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(280, 160, 111, 39))
        self.label_author.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_author.setFont(font)
        self.label_author.setStyleSheet("color: rgb(255, 85, 0);\n"
"font: 22pt \"Comic Sans MS\";")
        self.label_author.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_author.setObjectName("label_author")
        self.label_display = QtWidgets.QLabel(self.centralwidget)
        self.label_display.setGeometry(QtCore.QRect(6, 335, 881, 561))
        self.label_display.setMinimumSize(QtCore.QSize(0, 0))
        self.label_display.setMaximumSize(QtCore.QSize(1152, 648))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_display.setFont(font)
        self.label_display.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_display.setStyleSheet("border-image: url(:/newPrefix/images_test/human.png);")
        self.label_display.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display.setObjectName("label_display")
        self.textEdit_camera = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_camera.setGeometry(QtCore.QRect(664, 262, 400, 37))
        self.textEdit_camera.setMinimumSize(QtCore.QSize(240, 37))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_camera.setFont(font)
        self.textEdit_camera.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(0, 170, 255);\n"
"color:rgb(0, 0, 255)")
        self.textEdit_camera.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_camera.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_camera.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_camera.setReadOnly(True)
        self.textEdit_camera.setObjectName("textEdit_camera")
        self.toolButton_camera = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_camera.setGeometry(QtCore.QRect(610, 260, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_camera.sizePolicy().hasHeightForWidth())
        self.toolButton_camera.setSizePolicy(sizePolicy)
        self.toolButton_camera.setMaximumSize(QtCore.QSize(60, 60))
        self.toolButton_camera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_camera.setAutoFillBackground(False)
        self.toolButton_camera.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(0, 170, 255);\n"
"color:rgb(0, 170, 255);")
        self.toolButton_camera.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images_test/shexiangtou.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_camera.setIcon(icon1)
        self.toolButton_camera.setIconSize(QtCore.QSize(60, 60))
        self.toolButton_camera.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_camera.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_camera.setAutoRaise(False)
        self.toolButton_camera.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_camera.setObjectName("toolButton_camera")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(280, 70, 671, 51))
        self.label_title.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(170, 0, 255);\n"
"font: 28pt \"Times New Roman\";")
        self.label_title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_title.setObjectName("label_title")
        self.label_numer_result = QtWidgets.QLabel(self.centralwidget)
        self.label_numer_result.setGeometry(QtCore.QRect(1148, 400, 83, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_numer_result.setFont(font)
        self.label_numer_result.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_numer_result.setObjectName("label_numer_result")
        self.label_ymin = QtWidgets.QLabel(self.centralwidget)
        self.label_ymin.setGeometry(QtCore.QRect(1082, 816, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_ymin.setFont(font)
        self.label_ymin.setStyleSheet("font: italic 14pt \"Consolas\";")
        self.label_ymin.setObjectName("label_ymin")
        self.label_class_result = QtWidgets.QLabel(self.centralwidget)
        self.label_class_result.setGeometry(QtCore.QRect(1094, 680, 111, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_class_result.setFont(font)
        self.label_class_result.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_class_result.setObjectName("label_class_result")
        self.label_picLocation = QtWidgets.QLabel(self.centralwidget)
        self.label_picLocation.setGeometry(QtCore.QRect(894, 744, 37, 43))
        self.label_picLocation.setStyleSheet("border-image: url(:/newPrefix/images_test/Ordinateur.png);")
        self.label_picLocation.setText("")
        self.label_picLocation.setObjectName("label_picLocation")
        self.label_ymax = QtWidgets.QLabel(self.centralwidget)
        self.label_ymax.setGeometry(QtCore.QRect(1082, 850, 89, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_ymax.setFont(font)
        self.label_ymax.setStyleSheet("font: italic 14pt \"Consolas\";")
        self.label_ymax.setObjectName("label_ymax")
        self.label_location = QtWidgets.QLabel(self.centralwidget)
        self.label_location.setGeometry(QtCore.QRect(970, 780, 131, 31))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_location.setFont(font)
        self.label_location.setObjectName("label_location")
        self.label_useTime = QtWidgets.QLabel(self.centralwidget)
        self.label_useTime.setGeometry(QtCore.QRect(966, 350, 111, 51))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_useTime.setFont(font)
        self.label_useTime.setObjectName("label_useTime")
        self.label_ymin_result = QtWidgets.QLabel(self.centralwidget)
        self.label_ymin_result.setGeometry(QtCore.QRect(1168, 818, 73, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.label_ymin_result.setFont(font)
        self.label_ymin_result.setObjectName("label_ymin_result")
        self.label_picTime = QtWidgets.QLabel(self.centralwidget)
        self.label_picTime.setGeometry(QtCore.QRect(900, 350, 41, 41))
        self.label_picTime.setStyleSheet("border-image: url(:/newPrefix/images_test/fps.png);")
        self.label_picTime.setText("")
        self.label_picTime.setObjectName("label_picTime")
        self.label_picSelect = QtWidgets.QLabel(self.centralwidget)
        self.label_picSelect.setGeometry(QtCore.QRect(900, 440, 41, 41))
        self.label_picSelect.setStyleSheet("border-image: url(:/newPrefix/images_test/target.png);")
        self.label_picSelect.setText("")
        self.label_picSelect.setObjectName("label_picSelect")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(890, 640, 301, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_xmax = QtWidgets.QLabel(self.centralwidget)
        self.label_xmax.setGeometry(QtCore.QRect(900, 850, 87, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_xmax.setFont(font)
        self.label_xmax.setStyleSheet("font: italic 14pt \"Consolas\";")
        self.label_xmax.setObjectName("label_xmax")
        self.label_picNumber = QtWidgets.QLabel(self.centralwidget)
        self.label_picNumber.setGeometry(QtCore.QRect(896, 390, 41, 41))
        self.label_picNumber.setStyleSheet("border-image: url(:/newPrefix/images_test/counter.png);")
        self.label_picNumber.setText("")
        self.label_picNumber.setObjectName("label_picNumber")
        self.label_picResult = QtWidgets.QLabel(self.centralwidget)
        self.label_picResult.setGeometry(QtCore.QRect(898, 678, 41, 39))
        self.label_picResult.setStyleSheet("border-image: url(:/newPrefix/images_test/query.png);")
        self.label_picResult.setText("")
        self.label_picResult.setObjectName("label_picResult")
        self.label_objNum = QtWidgets.QLabel(self.centralwidget)
        self.label_objNum.setGeometry(QtCore.QRect(962, 400, 165, 39))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_objNum.setFont(font)
        self.label_objNum.setObjectName("label_objNum")
        self.label_xmin = QtWidgets.QLabel(self.centralwidget)
        self.label_xmin.setGeometry(QtCore.QRect(900, 816, 85, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_xmin.setFont(font)
        self.label_xmin.setStyleSheet("font: italic 14pt \"Consolas\";")
        self.label_xmin.setObjectName("label_xmin")
        self.label_class = QtWidgets.QLabel(self.centralwidget)
        self.label_class.setGeometry(QtCore.QRect(968, 686, 111, 37))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_class.setFont(font)
        self.label_class.setObjectName("label_class")
        self.comboBox_select = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_select.setGeometry(QtCore.QRect(966, 450, 179, 35))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.comboBox_select.setFont(font)
        self.comboBox_select.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBox_select.setStyleSheet("color: rgb(43, 89, 124);\n"
"font: italic 12pt \"Consolas\";")
        self.comboBox_select.setIconSize(QtCore.QSize(36, 36))
        self.comboBox_select.setObjectName("comboBox_select")
        self.comboBox_select.addItem("")
        self.label_ymax_result = QtWidgets.QLabel(self.centralwidget)
        self.label_ymax_result.setGeometry(QtCore.QRect(1168, 852, 75, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.label_ymax_result.setFont(font)
        self.label_ymax_result.setObjectName("label_ymax_result")
        self.label_xmax_result = QtWidgets.QLabel(self.centralwidget)
        self.label_xmax_result.setGeometry(QtCore.QRect(988, 852, 75, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.label_xmax_result.setFont(font)
        self.label_xmax_result.setObjectName("label_xmax_result")
        self.label_time_result = QtWidgets.QLabel(self.centralwidget)
        self.label_time_result.setGeometry(QtCore.QRect(1100, 350, 133, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_time_result.setFont(font)
        self.label_time_result.setObjectName("label_time_result")
        self.label_xmin_result = QtWidgets.QLabel(self.centralwidget)
        self.label_xmin_result.setGeometry(QtCore.QRect(988, 816, 77, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.label_xmin_result.setFont(font)
        self.label_xmin_result.setObjectName("label_xmin_result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(890, 330, 311, 571))
        self.label.setStyleSheet("background-color: rgb(233, 239, 251);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_picScore = QtWidgets.QLabel(self.centralwidget)
        self.label_picScore.setGeometry(QtCore.QRect(898, 726, 41, 41))
        self.label_picScore.setStyleSheet("border-image: url(:/newPrefix/images_test/finger.png);")
        self.label_picScore.setText("")
        self.label_picScore.setObjectName("label_picScore")
        self.label_numer_score = QtWidgets.QLabel(self.centralwidget)
        self.label_numer_score.setGeometry(QtCore.QRect(1092, 728, 83, 39))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_numer_score.setFont(font)
        self.label_numer_score.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_numer_score.setObjectName("label_numer_score")
        self.label_Score = QtWidgets.QLabel(self.centralwidget)
        self.label_Score.setGeometry(QtCore.QRect(964, 730, 165, 37))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_Score.setFont(font)
        self.label_Score.setObjectName("label_Score")
        self.label_display_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_display_2.setGeometry(QtCore.QRect(40, 140, 231, 71))
        self.label_display_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_display_2.setMaximumSize(QtCore.QSize(1152, 648))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_display_2.setFont(font)
        self.label_display_2.setMouseTracking(True)
        self.label_display_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_display_2.setStyleSheet("border-image: url(:/newPrefix/images_test/uni.png);\n"
"background-color: transparent;")
        self.label_display_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display_2.setObjectName("label_display_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(110, 260, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMaximumSize(QtCore.QSize(60, 60))
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setStyleSheet("background-color: transparent;")
        self.toolButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images_test/xiangji.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QtCore.QSize(60, 60))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 260, 361, 41))
        self.textEdit.setMinimumSize(QtCore.QSize(240, 37))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(0, 170, 255);\n"
"color:rgb(0, 0, 255)")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(890, 490, 311, 41))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_picResult_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_picResult_3.setGeometry(QtCore.QRect(910, 530, 41, 41))
        self.label_picResult_3.setStyleSheet("border-image: url(:/newPrefix/images_test/user.png);")
        self.label_picResult_3.setText("")
        self.label_picResult_3.setObjectName("label_picResult_3")
        self.label_class_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_class_3.setGeometry(QtCore.QRect(1010, 540, 111, 37))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_class_3.setFont(font)
        self.label_class_3.setObjectName("label_class_3")
        self.label_class_result_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_class_result_3.setGeometry(QtCore.QRect(1030, 600, 111, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_class_result_3.setFont(font)
        self.label_class_result_3.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_class_result_3.setObjectName("label_class_result_3")
        self.label_picLocation_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_picLocation_2.setGeometry(QtCore.QRect(898, 776, 41, 41))
        self.label_picLocation_2.setStyleSheet("border-image: url(:/newPrefix/images_test/location.png);")
        self.label_picLocation_2.setText("")
        self.label_picLocation_2.setObjectName("label_picLocation_2")
        self.label.raise_()
        self.label_author.raise_()
        self.label_display.raise_()
        self.textEdit_camera.raise_()
        self.toolButton_camera.raise_()
        self.label_title.raise_()
        self.label_numer_result.raise_()
        self.label_ymin.raise_()
        self.label_class_result.raise_()
        self.label_picLocation.raise_()
        self.label_ymax.raise_()
        self.label_location.raise_()
        self.label_useTime.raise_()
        self.label_ymin_result.raise_()
        self.label_picTime.raise_()
        self.label_picSelect.raise_()
        self.line_4.raise_()
        self.label_xmax.raise_()
        self.label_picNumber.raise_()
        self.label_picResult.raise_()
        self.label_objNum.raise_()
        self.label_xmin.raise_()
        self.label_class.raise_()
        self.comboBox_select.raise_()
        self.label_ymax_result.raise_()
        self.label_xmax_result.raise_()
        self.label_time_result.raise_()
        self.label_xmin_result.raise_()
        self.label_picScore.raise_()
        self.label_numer_score.raise_()
        self.label_Score.raise_()
        self.label_display_2.raise_()
        self.toolButton.raise_()
        self.textEdit.raise_()
        self.line_5.raise_()
        self.label_picResult_3.raise_()
        self.label_class_3.raise_()
        self.label_class_result_3.raise_()
        self.label_picLocation_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGoogle_Translate = QtWidgets.QAction(MainWindow)
        self.actionGoogle_Translate.setObjectName("actionGoogle_Translate")
        self.actionHTML_type = QtWidgets.QAction(MainWindow)
        self.actionHTML_type.setObjectName("actionHTML_type")
        self.actionsoftware_version = QtWidgets.QAction(MainWindow)
        self.actionsoftware_version.setObjectName("actionsoftware_version")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MultiModal AI Recognition v1.0"))
        self.label_author.setToolTip(_translate("MainWindow", "<html><head/><body><p>思绪无限（邮箱：sixuwuxian@aliyun.com）</p></body></html>"))
        self.label_author.setText(_translate("MainWindow", "5GCers"))
        self.label_display.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.textEdit_camera.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\'; font-size:18pt;\">点击图标开启实时摄像</span></p></body></html>"))
        self.label_title.setToolTip(_translate("MainWindow", "<html><head/><body><p>version: v1.0</p><p>author: 思绪无限</p></body></html>"))
        self.label_title.setText(_translate("MainWindow", "多模态AI识别系统 v1.0"))
        self.label_numer_result.setText(_translate("MainWindow", "0"))
        self.label_ymin.setText(_translate("MainWindow", "ymin: "))
        self.label_class_result.setText(_translate("MainWindow", "None"))
        self.label_ymax.setText(_translate("MainWindow", "ymax: "))
        self.label_location.setText(_translate("MainWindow", "<html><head/><body><p>位 置：<br/></p></body></html>"))
        self.label_useTime.setText(_translate("MainWindow", "<html><head/><body><p>FPS：</p></body></html>"))
        self.label_ymin_result.setText(_translate("MainWindow", "0"))
        self.label_xmax.setText(_translate("MainWindow", "xmax: "))
        self.label_objNum.setText(_translate("MainWindow", "<html><head/><body><p>手势数目：<br/></p></body></html>"))
        self.label_xmin.setText(_translate("MainWindow", "xmin: "))
        self.label_class.setText(_translate("MainWindow", "<html><head/><body><p>手势结果：<br/></p></body></html>"))
        self.comboBox_select.setCurrentText(_translate("MainWindow", "所有手势"))
        self.comboBox_select.setItemText(0, _translate("MainWindow", "所有手势"))
        self.label_ymax_result.setText(_translate("MainWindow", "0"))
        self.label_xmax_result.setText(_translate("MainWindow", "0"))
        self.label_time_result.setText(_translate("MainWindow", "0"))
        self.label_xmin_result.setText(_translate("MainWindow", "0"))
        self.label_numer_score.setText(_translate("MainWindow", "0"))
        self.label_Score.setText(_translate("MainWindow", "<html><head/><body><p>手指数：<br/></p></body></html>"))
        self.label_display_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\'; font-size:18pt;\">点击图标录入人脸</span></p></body></html>"))
        self.label_class_3.setText(_translate("MainWindow", "<html><head/><body><p>当前用户为：<br/></p></body></html>"))
        self.label_class_result_3.setText(_translate("MainWindow", "Unknown"))
        self.actionGoogle_Translate.setText(_translate("MainWindow", "Google Translate"))
        self.actionHTML_type.setText(_translate("MainWindow", "HTML type"))
        self.actionsoftware_version.setText(_translate("MainWindow", "software version"))
import image1_rc
