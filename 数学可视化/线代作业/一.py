import numpy as np

# 定义矩阵A
A = np.array([[2, 2, 3],
              [1, -1, 0],
              [-1, 2, 1]])

# 使用np.linalg.inv()函数求逆矩阵
try:
    A_inv = np.linalg.inv(A)
    print(A_inv)
except np.linalg.LinAlgError:
    print("该矩阵不可逆")