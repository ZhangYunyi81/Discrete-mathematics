"""
@name:app.py.py
@author:ZHANG Yunyi
@date:2024/1/9
@description:自己用Qt搭建的UI界面
"""
import sys
import time
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from graph import *
from PyQt5.QtGui import QPixmap
import matplotlib
import matplotlib.pyplot as plt
import time
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500,400)
        self.container = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.flo = QFormLayout()
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText('请输入对称矩阵以设置无向图权重，例如：\n[[0,1],[1,0]]')
        self.flo.addWidget(self.text_edit)
        self.btn_set_graph = QPushButton('生成无向图',self)
        self.btn_set_graph.clicked.connect(self.set_graph)
        self.flo.addWidget(self.btn_set_graph)
        self.set_start_line = QTextEdit()
        self.set_start_line.setPlaceholderText('请输入最短路径树的根节点...')
        self.flo.addWidget(self.set_start_line)
        self.set_start_btn = QPushButton('设置根节点',self)
        self.set_start_btn.clicked.connect(self.set_start)
        self.flo.addWidget(self.set_start_btn)
        self.btn_ran_graph = QPushButton('随机生成图',self)
        self.btn_ran_graph.clicked.connect(self.random_grid_graph)
        self.btn_ran_start_end = QPushButton('随机生成起点终点', self)
        self.btn_ran_start_end.clicked.connect(self.random_start_end)
        self.btn_solve = QPushButton('求解起点到终点的最短路径',self)
        self.btn_solve.clicked.connect(self.solve_shortest_path)
        self.btn_tree = QPushButton('求解最短路径树')
        self.btn_tree.clicked.connect(self.draw_tree)
        # v_layout.addWidget(btn1)
        # v_layout.addWidget(btn2)
        # self.v_layout.addWidget(self.text_edit)
        # self.v_layout.addWidget(self.btn_ran_graph)
        # self.v_layout.addWidget(self.btn_ran_start_end)
        # self.v_layout.addWidget(self.btn_solve)
        # self.v_layout.addWidget(self.btn_tree)
        self.N2AnoPb_shadow = QGraphicsDropShadowEffect()  # 阴影类
        self.N2AnoPb_shadow.setOffset(0, 0)  # 设置阴影偏移坐标
        self.N2AnoPb_shadow.setBlurRadius(10)  # 设置阴影深度
        self.N2AnoPb_shadow.setColor(Qt.darkGreen)  # 设置阴影颜色
        self.btn_tree.setGraphicsEffect(self.N2AnoPb_shadow)  # 把阴影赋给控件


        self.flo.addWidget(self.btn_ran_graph)
        self.flo.addWidget(self.btn_ran_start_end)
        self.flo.addWidget(self.btn_solve)
        self.flo.addWidget(self.btn_tree)
        # self.setLayout(self.v_layout)
        self.setLayout(self.flo)

        self.setWindowTitle('最短路径树APP(作者：张云奕)')

    def set_graph(self):
        try:
            graph_info = self.text_edit.toPlainText()
            weight_matrix = np.array(eval(graph_info))
            # print(weight_matrix.shape)
            self.G = MyGraph()
            self.G.generate_map_from_matrix(weight_matrix)
            plt.close()
            self.G.draw_raw()
            # print('已设置无向图')
        except:
            msg_box = QMessageBox(QMessageBox.Critical, '输入错误', '请输入正确的矩阵！')
            msg_box.exec_()

    def set_start(self):
        try:
            start_info = self.set_start_line.toPlainText()
            self.G.start = eval(start_info)
            # print('已设置根节点')
            plt.close()
            self.G.draw_start()
        except:
            msg_box = QMessageBox(QMessageBox.Critical, '输入错误', '图中没有这个结点')
            msg_box.exec_()

    def random_graph(self):
        self.G = MyGraph()
        self.G.generate_random_map()
        plt.close()
        self.G.draw_raw()
        print('随机图已生成')

    def random_grid_graph(self):
        # os.remove('./fig/random_graph_raw.png')
        self.G = MyGraph()
        self.G.generate_grid_map()
        plt.close()
        self.G.draw_raw()
        plt.savefig('./fig/random_graph_raw.png')
        print('图已生成')
        # pix = QPixmap('./fig/random_graph_raw.png')
        # label = QLabel(self)
        # label.setPixmap(pix)
        # label.setScaledContents(True)

    def random_start_end(self):
        print('已生成起点和终点，分别为：')
        self.G.generate_random_start_and_end()
        plt.close()
        self.G.draw_start_end()
        # print(G.start)

    def solve_shortest_path(self):
        print('已生成最短路径：')
        self.G.generate_shortest_path()
        plt.close()
        self.G.draw_cal_path()

    def draw_tree(self):
        self.G.solve_tree()
        plt.close()
        self.G.draw_tree()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()