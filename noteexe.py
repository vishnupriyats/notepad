import sys
import datetime
from PySide import QtGui
# import qdarkstyle
from notepy import Ui_MainWindow

class mainwindow(Ui_MainWindow, QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(mainwindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.statusBar().showMessage('Ready')
        self.actionExit.triggered.connect(self.closewindow)
        self.actionStatus.triggered.connect(self.togglemenu)
        self.actionFont.triggered.connect(self.displayfont)
        self.actionOpen.triggered.connect(self.showopen)
        self.actionSave.triggered.connect(self.save)
        self.actionPrint.triggered.connect(self.printdialog)
        self.actionDate_time.triggered.connect(self.displaydate)
        self.actionCopy.triggered.connect(self.copyfun)
        self.actionPaste.triggered.connect(self.pastefun)
        self.actionCut.triggered.connect(self.cutfun)
        self.actionDelete.triggered.connect(self.clearfun)
        self.actionSelect_all.triggered.connect(self.selectall)
        self.actionNew.triggered.connect(self.newtext)
        self.show()
    def closewindow(self):
        msgBox =QtGui.QMessageBox()
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
        msgBox.setDefaultButton(QtGui.QMessageBox.Save)
        ret = msgBox.exec_()
        if ret == QtGui.QMessageBox.Save:
          # Save was clicked
            self.save()
            self.close() 
        elif ret == QtGui.QMessageBox.Discard:
            self.clearfun()
            self.close()
            # Don't save was clicked
        elif ret == QtGui.QMessageBox.Cancel:
            QtGui.QMessageBox.information(self,'',"Nothing Changed")
            # cancel was clicked
    def togglemenu(self):
        if self.actionStatus.isChecked():
            self.statusBar().show()
        else:
            self.statusBar().hide()    
    
    def displayfont(self):
        font,ok = QtGui.QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)
    
    def showopen(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(str(data))
        print fname
    def save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        try:
            file = open(name[0],'w')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close() 
        except:
            QtGui.QMessageBox.information(self,'',"Nothing Changed")

    def printdialog(self):
        printer=QtGui.QPrinter()        
        printDialog = QtGui.QPrintDialog(printer)
        if printDialog.exec_() == QtGui.QDialog.Accepted :
            print"check"
    def displaydate(self):
        x=datetime.datetime.now()
        self.textEdit.append(str(x))
    def copyfun(self):
        QtGui.QTextEdit.copy(self.textEdit) 
    def pastefun(self):
        QtGui.QTextEdit.paste(self.textEdit)
    def cutfun(self):
        QtGui.QTextEdit.cut(self.textEdit)
    def clearfun(self):
        QtGui.QTextEdit.clear(self.textEdit)  
    def clearfun(self):
        QtGui.QTextEdit.clear(self.textEdit)
    def selectall(self):
        QtGui.QTextEdit.selectAll(self.textEdit)   
    def newtext(self):
        msgBox =QtGui.QMessageBox()
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
        msgBox.setDefaultButton(QtGui.QMessageBox.Save)
        ret = msgBox.exec_()
        if ret == QtGui.QMessageBox.Save:
          # Save was clicked
            self.save()   
        elif ret == QtGui.QMessageBox.Discard:
            self.clearfun()
            # Don't save was clicked
        elif ret == QtGui.QMessageBox.Cancel:
            QtGui.QMessageBox.information(self,'',"Nothing Changed")
            # cancel was clicked
    def closeEvent(self, event):
        msgBox =QtGui.QMessageBox()
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
        msgBox.setDefaultButton(QtGui.QMessageBox.Save)
        ret = msgBox.exec_()
        if ret == QtGui.QMessageBox.Save:
          # Save was clicked
            self.save()
            self.close() 
        elif ret == QtGui.QMessageBox.Discard:
            self.clearfun()
            self.close()
            # Don't save was clicked
        elif ret == QtGui.QMessageBox.Cancel:
            QtGui.QMessageBox.information(self,'',"Nothing Changed")
            # cancel was clicked
            event.ignore()    






if __name__ == '__main__':
    app = QtGui.QApplication([])
    myapp = mainwindow()
    # dark_stylesheet = qdarkstyle.load_stylesheet_pyside()
    # app.setStyleSheet(dark_stylesheet)
    sys.exit(app.exec_())