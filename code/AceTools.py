import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from PyQt5.QtChart import *
# from PyQt5 import QtWidgets
#定义主窗口

class MainWin(QWidget):
    #创建构造函数
    def __init__(self):
        super(MainWin,self).__init__()
        self.setGeometry(300,200,1280,720)
        self.setWindowTitle('Ace Tools')
        #创建状态栏
        self.statusbar = QStatusBar()
        #创建左侧列表菜单
        self.listmenu = QListWidget(self)
        #创建列表项目
        self.listmenu.insertItem(0,"辅助功能")
        self.listmenu.insertItem(1,"主要工具")
        self.listmenu.insertItem(2,"关于我的")
        #列表宽度设置
        self.listmenu.setFixedWidth(125)
        #列表项目间距设置
        self.listmenu.setSpacing(10)
        #创建堆叠
        self.stack_Assistant = QWidget()
        self.stack_Tools= QWidget()
        self.stack_About = QWidget()
        #创建页面
        self.Assistant()
        self.Tools()
        self.About()
        #将堆叠填入
        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.stack_Assistant)
        self.stack.addWidget(self.stack_Tools)
        self.stack.addWidget(self.stack_About)
        #截图部分
        pixmap = QPixmap("/home/otoya/Codehub/Python/AceToolBox/PyQtToolBox/img/desk.png")
        pixmap = pixmap.scaled(150, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label_screen = QLabel()
        label_screen.setPixmap(pixmap)
        #大体分为左右两部分
        hbox = QHBoxLayout()
        #左侧填入菜单与手机截屏
        #菜单与截屏上下两分
        vbox = QVBoxLayout()
        vbox.addWidget(label_screen)
        vbox.addWidget(self.listmenu)
        #右侧填入堆叠布局页
        hbox.addLayout(vbox)
        hbox.addWidget(self.stack)
        #显示布局
        self.setLayout(hbox)
        #绑定列表项与页面
        self.listmenu.currentRowChanged.connect(self.display)


    #定义辅助页面左侧内容
    #应用列表



    #辅助页面
    def Assistant(self):
        layout = QFormLayout()
        layout.addRow('fuck', QLineEdit())
        self.stack_Assistant.setLayout(layout)
    #工具页面
    def Tools(self):
        layout = QFormLayout()
        layout.addRow('fuck', QLineEdit())
        self.stack_Tools.setLayout(layout)
    #关于页面
    def About(self):
        layout = QFormLayout()
        layout.addRow('gfdgs', QLineEdit())
        self.stack_About.setLayout(layout)



    #创建显示页面函数
    def display(self, x):
        self.stack.setCurrentIndex(x)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())