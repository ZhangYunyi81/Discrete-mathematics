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

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500,300)
        # 最外层的布局，采用水平布局，包含两部分，左边为输入的图信息，
        # 右边为输出的最短路径图
        self.container = QHBoxLayout()
        # 第一组控件，设定图的信息
        self.input_box = QGroupBox('输入信息')
        # 输入信息是垂直摆放
        self.v_layout = QVBoxLayout()
        # btn1 = QPushButton('定义节点', self)
        # btn2 = QPushButton('定义边', self)
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
        self.v_layout.addWidget(self.btn_ran_graph)
        self.v_layout.addWidget(self.btn_ran_start_end)
        self.v_layout.addWidget(self.btn_solve)
        self.v_layout.addWidget(self.btn_tree)
        self.input_box.setLayout(self.v_layout)
        # 创建第二个组
        # self.output_box = QGroupBox('图可视化')
        # self.v_layout = QVBoxLayout()
        # self.output_box.setLayout(self.v_layout)
        self.container.addWidget(self.input_box)
        # self.container.addWidget(self.output_box)

        self.setLayout(self.container)
        self.setWindowTitle('计算无向图最短路径')

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