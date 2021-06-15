from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(882, 683)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openGL = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGL.setGeometry(QtCore.QRect(0, 0, 881, 641))
        self.openGL.setObjectName("openGL")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuDefine_Cutting_Plane = QtWidgets.QMenu(self.menuView)
        self.menuDefine_Cutting_Plane.setObjectName("menuDefine_Cutting_Plane")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFlip = QtWidgets.QAction(MainWindow)
        self.actionFlip.setObjectName("actionFlip")
        self.actionRotate = QtWidgets.QAction(MainWindow)
        self.actionRotate.setObjectName("actionRotate")
        self.actionTransform = QtWidgets.QAction(MainWindow)
        self.actionTransform.setObjectName("actionTransform")
        self.actionTop_Plane = QtWidgets.QAction(MainWindow)
        self.actionTop_Plane.setObjectName("actionTop_Plane")
        self.actionRight_Plane = QtWidgets.QAction(MainWindow)
        self.actionRight_Plane.setObjectName("actionRight_Plane")
        self.actionFront_Plane = QtWidgets.QAction(MainWindow)
        self.actionFront_Plane.setObjectName("actionFront_Plane")
        self.actionCut_Plane = QtWidgets.QAction(MainWindow)
        self.actionCut_Plane.setObjectName("actionCut_Plane")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuDefine_Cutting_Plane.addAction(self.actionFlip)
        self.menuDefine_Cutting_Plane.addAction(self.actionRotate)
        self.menuDefine_Cutting_Plane.addAction(self.actionCut_Plane)
        self.menuView.addAction(self.actionTop_Plane)
        self.menuView.addAction(self.actionRight_Plane)
        self.menuView.addAction(self.actionFront_Plane)
        self.menuView.addAction(self.menuDefine_Cutting_Plane.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Healing STL Files"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuDefine_Cutting_Plane.setTitle(_translate("MainWindow", "Define Cutting Plane"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionFlip.setText(_translate("MainWindow", "Flip"))
        self.actionRotate.setText(_translate("MainWindow", "Rotate"))
        self.actionTransform.setText(_translate("MainWindow", "Transform "))
        self.actionTop_Plane.setText(_translate("MainWindow", "Top Plane"))
        self.actionRight_Plane.setText(_translate("MainWindow", "Right Plane"))
        self.actionFront_Plane.setText(_translate("MainWindow", "Front Plane"))
        self.actionCut_Plane.setText(_translate("MainWindow", "Cut Plane"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())