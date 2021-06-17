from pyqtgraph.Qt import QtWidgets
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys
from main import Ui_MainWindow


class Run:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.start_window, self.start_window_instance = self.opening_a_window(Ui_MainWindow(), type_of_window='main window')

    def opening_a_window(self, class_name, type_of_window='dialog'):  # a function that creates a new window
        if type_of_window == 'dialog':
            dialog = QtWidgets.QDialog()
        else:
            dialog = QtWidgets.QMainWindow()
        dialog_instance = class_name
        dialog_instance.setupUi(dialog)
        return dialog, dialog_instance

    def browsing(self):
        file = QtWidgets.QFileDialog.getOpenFileName(None, 'Choose an STL file',
                                                     r'C:\Users\ziaMh\Documents\Stl_file_read_and_store\\',
                                                     'STL files(*.stl)')
        self.file_address = file[0]
        self.stl_file = open(self.file_address)

        points = []
        x = []
        y = []
        z = []
        w = gl.GLViewWidget()
        w.showMaximized()
        w.setWindowTitle('STL file view in 3D')
        w.setCameraPosition(distance=200)

        for line in self.stl_file:
            if 'vertex' in line:
                splitted_line = line.split('vertex ')
                splitted_line = splitted_line[1]
                splitted_line = splitted_line.split(' ')  # separates the nodes
                if '' in splitted_line:
                    for a in range(splitted_line.count('')):
                        splitted_line.remove('')
                points.append((float(splitted_line[0]), float(splitted_line[1]), float(splitted_line[2])))

            elif 'endloop' in line:
                x.append(points[0][0])
                x.append(points[1][0])
                x.append(points[2][0])
                x.append(points[0][0])

                y.append(points[0][1])
                y.append(points[1][1])
                y.append(points[2][1])
                y.append(points[0][1])

                z.append(points[0][2])
                z.append(points[1][2])
                z.append(points[2][2])
                z.append(points[0][2])
                points = []

                pts_for_a_triangle = np.vstack([x, y, z]).transpose()
                line = gl.GLLinePlotItem(
                    pos=pts_for_a_triangle,
                    color=pg.glColor(19),
                    width=1,
                    antialias=True)
                w.addItem(line)
                x = []
                y = []
                z = []

        w.show()
        self.app.exec()

    def main(self):
        self.start_window_instance.actionOpen.triggered.connect(self.browsing)
        self.start_window.show()
        sys.exit(self.app.exec_())


run = Run()
run.main()