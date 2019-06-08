import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__=='__main__':
    # 创建QApplication类实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口尺寸
    w.resize(400,200)
    # 移动窗口
    w.move(300,300)

    # 设置窗口标题
    w.setWindowTitle('百度文库免费下载—by CW')
    # 显示窗口
    w.show()
    # 进入程序的主循环，并通过exit和你熟确保主循环安全结束
    sys.exit(app.exec_())