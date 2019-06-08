import sys
import mainwindow
from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__=='__main__':
    # 创建QApplication类实例
    app = QApplication(sys.argv)
    mainWindow =QMainWindow()
    ui = mainwindow.Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
