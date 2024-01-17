"""
@name:ran_matrix.py
@author:ZHANG Yunyi
@date:2024/1/16
@description:随机生成一个对称矩阵
"""
import numpy as np

# 生成一个3x3的随机对称矩阵，对角线上的元素为0
def ran_matrix(N):
    # 生成一个3x3的随机对称矩阵
    sym_matrix = np.random.rand(N, N)
    sym_matrix = (sym_matrix + sym_matrix.T) / 2  # 确保矩阵对称
    for n in range(N):
        sym_matrix[n][n] = 0
    print(list(sym_matrix))


if __name__ == '__main__':
    ran_matrix(6)