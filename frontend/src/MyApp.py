from PyQt5 import QtWidgets, QtCore
import sys
sys.path.append('/home/wyjang/IdeaProjects/cbnuh')
from MriWidget import MriWidget
from Component import Component
from frontend.src.docker.PatWidget import PatWidget
from frontend.src.docker.PathologyWidget import PathologyWidget
from frontend.src.docker.PatHxWidget import PatHxWidget
from frontend.src.home.HomeWidget import HomeWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        self.data = Component()
        self.home_wg = HomeWidget()
        self.pat_wg = PatWidget()
        self.patHx_wg = PatHxWidget()
        self.pathology_wg = PathologyWidget()
        self.bgcolor = self.palette().color(self.backgroundRole()).name()

        self.patDock = QtWidgets.QDockWidget()
        self.patHxDock = QtWidgets.QDockWidget()
        self.pathologyDock = QtWidgets.QDockWidget()

        self.central = QtWidgets.QTextEdit(self)
        self.central.setText('Welcome  prototype')
        self.setCentralWidget(self.home_wg)
        self.setDockOptions(self.AnimatedDocks)

        self.initui()
        self.initDock()
        self.wg = MriWidget()
        self.wg.data = self.data

    def initDock(self):
        self.patDock = QtWidgets.QDockWidget('Patient information', self)
        self.patDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.patDock.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable
                                 | QtWidgets.QDockWidget.DockWidgetFloatable
                                 | QtWidgets.QDockWidget.DockWidgetMovable)
        self.patDock.setStyleSheet('QDockWidget::title{text-align:left;background:'+self.bgcolor+';}')
        self.patDock.close()

        self.patHxDock = QtWidgets.QDockWidget('Patient History', self)
        self.patHxDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.patHxDock.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable
                                   | QtWidgets.QDockWidget.DockWidgetFloatable
                                   | QtWidgets.QDockWidget.DockWidgetMovable)
        self.patHxDock.setStyleSheet('QDockWidget::title{text-align:left;background:'+self.bgcolor+';}')
        self.patHxDock.close()

        self.pathologyDock = QtWidgets.QDockWidget('Pathology', self)
        self.pathologyDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.pathologyDock.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable
                                       | QtWidgets.QDockWidget.DockWidgetFloatable
                                       | QtWidgets.QDockWidget.DockWidgetMovable)
        self.pathologyDock.setStyleSheet('QDockWidget::title{text-align:left;background:'+self.bgcolor+';}')
        self.pathologyDock.close()

        patHxDockable = QtWidgets.QTextEdit(self.patHxDock)
        patHxDockable.setText('')

        pathologyDockable = QtWidgets.QTextEdit(self.pathologyDock)
        pathologyDockable.setText('')

        self.patDock.setWidget(self.pat_wg)
        self.patHxDock.setWidget(patHxDockable)
        self.pathologyDock.setWidget(pathologyDockable)

        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.patDock)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.patHxDock)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.pathologyDock)

    def initui(self):
        self.statusBar()
        self.initmenu()
        self.setWindowTitle('platform')
        self.statusBar().showMessage('Ready')

    def initmenu(self):
        menu_bar = self.menuBar()
        patient_menu = menu_bar.addMenu('&Patient')
        patient_new = QtWidgets.QAction('&New', self)
        patient_new.triggered.connect(self.runmenupatnew)
        patient_load = QtWidgets.QAction('&Load', self)
        patient_load.triggered.connect(self.runmenupatload)

        patient_menu.addAction(patient_new)
        patient_menu.addAction(patient_load)

        load_menu = menu_bar.addMenu('&Load')
        load_mri = QtWidgets.QAction('&MRI', self)
        load_ct = QtWidgets.QAction('&CT', self)
        load_menu.addAction(load_mri)
        load_menu.addAction(load_ct)
        load_mri.triggered.connect(self.runmenuloadmri)
        signal_menu = menu_bar.addMenu('MR-signal Enhancement')
        signal_dr = QtWidgets.QAction('&Deformable Registration', self)
        signal_uis = QtWidgets.QAction('&Unpaired Image Set', self)
        signal_stm = QtWidgets.QAction('&Select Train Model', self)
        signal_aoq = QtWidgets.QAction('&Analysis of Quality', self)
        signal_s = QtWidgets.QAction('&Statistics', self)
        signal_h = QtWidgets.QAction('&Help', self)
        signal_menu.addAction(signal_dr)
        signal_menu.addAction(signal_uis)
        signal_menu.addAction(signal_stm)
        signal_menu.addAction(signal_aoq)
        signal_menu.addAction(signal_s)
        signal_menu.addAction(signal_h)

        # segment_menu = menu_bar.addMenu('Auto-Segmentation')

        sct_menu = menu_bar.addMenu('sCT generation')
        sct_dfi = QtWidgets.QAction('&DICOM File Information', self)
        sct_isa = QtWidgets.QAction('&Image Slice Adjusting', self)
        sct_stm = QtWidgets.QAction('&Select Train Model', self)
        sct_aoq = QtWidgets.QAction('&Analysis of Quality', self)
        sct_s = QtWidgets.QAction('&Statistics', self)
        sct_h = QtWidgets.QAction('&Help', self)
        sct_menu.addAction(sct_dfi)
        sct_menu.addAction(sct_isa)
        sct_menu.addAction(sct_stm)
        sct_menu.addAction(sct_aoq)
        sct_menu.addAction(sct_s)
        sct_menu.addAction(sct_h)

    def runmenuloadmri(self):
        if self.data.patient == "":
            self.aboutmsg(msg_id='runmenuloadmri')
        else:
            self.wg.getdicomlist()
            self.setCentralWidget(self.wg)

    def runmenupatnew(self):
        self.aboutmsg(msg_id='runmenupatnew')
        pass

    def runmenupatload(self):
        self.setCentralWidget(self.central)

        self.data.patient = 'prostate0013_1'
        self.pathologyDock.show()
        # self.patDockable.setText(self.data.patient)

        self.patDock.showMinimized()
        self.data.pat_hx = 'case1'
        # self.patHxDockable.setText(self.data.pat_hx)

        self.data.pat_pt = 'case2'
        self.patHxDock.show()
        # self.pathologyDockable.setText(self.data.pat_pt)
        pass

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def aboutmsg(self, msg_id):
        if msg_id == 'runmenupatnew':
            QtWidgets.QMessageBox.about(self, 'Message', 'Now developing')

        elif msg_id == 'runmenuloadmri':
            QtWidgets.QMessageBox.about(self, 'Message', 'First, select a patient')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    m = MainWindow()
    m.showMaximized()
    sys.exit(app.exec_())
