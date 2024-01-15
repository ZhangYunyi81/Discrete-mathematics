"""
@name:graph.py
@author:ZHANG Yunyi
@date:2024/1/9
@description:涉及图论的类和函数
"""
import networkx as nx
import numpy as np
import itertools
from math import *
import matplotlib as mpl
import matplotlib.pyplot as plt
from dijkstra import *


class MyGraph(nx.Graph):
    def __init__(self, size=8):
        super().__init__()
        self.start = 0
        self.end = 0
        self.size = size
        self.path = []
        self.shortest_length = 0

    def generate_map_from_matrix(self, weight_matrix):
        node_amount = weight_matrix.shape[0]
        for node_1 in range(node_amount):
            self.add_node(node_1, pos=(np.random.random(1), np.random.random(1)))
            for node_2 in range(node_amount):
                if node_1 < node_2:
                    if weight_matrix[node_1][node_2] != 0:
                        self.add_edge(node_1, node_2, weight=weight_matrix[node_1][node_2])

    # 随机生成网格化地图
    def generate_grid_map(self):
        # 网格的行列数
        # size = np.random.randint(low=5, high=10)
        size = self.size
        # 分辨率
        res = 1
        # 生成随机矩阵，代表各边权重
        for i in range(size*size):
            # 行列数
            column = int(i / size)
            row = i % size
            self.add_node(i, pos=(row, column))
        for node_s in range(size*size):
            for node_p in range(size*size):
                if node_s != node_p:
                    x_s = self.nodes[node_s]['pos']
                    x_p = self.nodes[node_p]['pos']
                    distance = sqrt((x_s[0]-x_p[0])**2+(x_s[1]-x_p[1])**2)
                    if distance <= 1.5:
                        if not self.has_edge(node_s, node_p):
                            self.add_edge(node_s, node_p, weight=np.random.randint(1, 20))

    def generate_random_start_and_end(self):
        node_amount = self.number_of_nodes()
        while True:
            self.start = np.random.randint(low=0, high=node_amount)
            if self.has_node(self.start):
                break
        while True:
            self.end = np.random.randint(low=0, high=node_amount)
            if self.start != self.end and self.has_node(self.end):
                print(self.start, self.end)
                break

    def generate_shortest_path(self):
        self.shortest_length, self.path = dijkstra(self, self.start, self.end)
        print(self.path)

    def draw_raw(self):
        # 各节点位置
        fig = plt.figure()
        position ={}
        for i in range(self.number_of_nodes()):
            position[i] = self.nodes[i]['pos']
        weights_dic = nx.get_edge_attributes(self, 'weight')
        weights_list = []
        for idx, weight in weights_dic.items():
            weights_list.append(weight)
        # options = {"node_color": "#65abd0", "edge_color": '#dbebf4', "width": 1, "with_labels": True}
        cmap = plt.cm.get_cmap('Blues')
        options = {"node_color": "#65abd0", "edge_color": weights_list, 'edge_cmap': cmap, "width": 1, "with_labels": True}
        # nx.draw(self, pos=position, **options)
        nx.draw(self, with_labels=True)
        # nx.draw_networkx_edges(self, position, edgelist=[(0,1)], edge_color='m', width=4)
        # nx.draw_networkx(self, position, with_labels=True)
        # nx.draw_networkx_edge_labels(self, position, edge_labels=weights)
        # print(weights_dic)
        plt.show()

    def draw_start_end(self):
        fig = plt.figure()
        position = {}
        for i in range(self.number_of_nodes()):
            position[i] = self.nodes[i]['pos']
        weights_dic = nx.get_edge_attributes(self, 'weight')
        weights_list = []
        for idx, weight in weights_dic.items():
            weights_list.append(weight)
        # options = {"node_color": "#65abd0", "edge_color": '#dbebf4', "width": 1, "with_labels": True}
        cmap = plt.cm.get_cmap('Blues')
        options = {"node_color": "#65abd0", "edge_color": weights_list, 'edge_cmap': cmap, "width": 1,
                   "with_labels": True}
        nx.draw(self, pos=position, **options)
        # nx.draw(self, with_labels=True)
        nx.draw_networkx_nodes(self, position, nodelist=[self.start, self.end], node_color='m')
        # print(weights_dic)
        plt.savefig('./fig/path.png')
        plt.show()

    def solve_tree(self):
        self.path_tree = {}
        path = []
        for node in range(self.number_of_nodes()):
            if node != self.start:
                _, path = dijkstra(self, self.start, node)
                self.path_tree[node] = path
        # print(self.path_tree)

    def draw_tree(self):
        fig = plt.figure()
        position = {}
        for i in range(self.number_of_nodes()):
            position[i] = self.nodes[i]['pos']
        weights_dic = nx.get_edge_attributes(self, 'weight')
        weights_list = []
        for idx, weight in weights_dic.items():
            weights_list.append(weight)
        # options = {"node_color": "#65abd0", "edge_color": '#dbebf4', "width": 1, "with_labels": True}
        cmap = plt.cm.get_cmap('Blues')
        options = {"node_color": "#65abd0", "edge_color": weights_list, 'edge_cmap': cmap, "width": 1,
                   "with_labels": True}
        nx.draw(self, pos=position, **options)
        for end, path in self.path_tree.items():
            path_list = []
            for node_idx in range(len(path) - 1):
                path_list.append((path[node_idx], path[node_idx + 1]))
            nx.draw_networkx_edges(self, position, edgelist=path_list, edge_color='m', width=4)
        nx.draw_networkx_nodes(self, position, nodelist=[self.start], node_color='m')
        # print(weights_dic)
        # plt.savefig('./fig/path.png')
        plt.show()


    def draw_cal_path(self):
        fig=plt.figure()
        position = {}
        for i in range(self.number_of_nodes()):
            position[i] = self.nodes[i]['pos']
        weights_dic = nx.get_edge_attributes(self, 'weight')
        weights_list = []
        for idx, weight in weights_dic.items():
            weights_list.append(weight)
        # options = {"node_color": "#65abd0", "edge_color": '#dbebf4', "width": 1, "with_labels": True}
        cmap = plt.cm.get_cmap('Blues')
        options = {"node_color": "#65abd0", "edge_color": weights_list, 'edge_cmap': cmap, "width": 1,
                   "with_labels": True}
        nx.draw(self, pos=position, **options)
        path_list = []
        for node_idx in range(len(self.path)-1):
            path_list.append((self.path[node_idx], self.path[node_idx+1]))
        nx.draw_networkx_edges(self, position, edgelist=path_list, edge_color='m', width=4)
        nx.draw_networkx_nodes(self, position, nodelist=[self.start, self.end], node_color='m')
        # print(weights_dic)
        plt.savefig('./fig/path.png')
        plt.show()



if __name__ == '__main__':
    G = MyGraph()
    G.generate_grid_map()
    G.draw_raw()
