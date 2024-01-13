"""
@name:dijkstra.py
@author:ZHANG Yunyi
@date:2024/1/10
@description:自己写的Dijkstra算法
"""
import sys
import heapq
import networkx as nx

def dijkstra(graph, start, end):
    # 初始化距离字典和路径字典
    distances = {node: float('infinity') for node in graph.nodes()}
    paths = {node: [] for node in graph.nodes()}
    # 设置起点距离为0，并且路径为空
    distances[start] = 0
    paths[start] = [start]
    # 创建优先队列并将起点添加到队列中
    queue = [(0, start)]
    while queue:
        # 取出队列中的最小距离的节点
        current_distance, current_node = heapq.heappop(queue)
        # 如果当前节点已经在访问过，并且距离更大，那么跳过该节点
        if current_distance > distances[current_node]:
            continue
        # 遍历与当前节点相邻的节点
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']  # 获取边的权重
            distance = current_distance + weight  # 计算通过当前节点到达相邻节点的距离
            # 如果通过当前节点到达相邻节点的距离小于已知的距离，那么更新距离字典、路径字典和队列
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(queue, (distance, neighbor))
    return distances[end], paths[end]  # 返回终点和起点的最短路径及路径长度