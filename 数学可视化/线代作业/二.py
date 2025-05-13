import numpy as np

# 定义矩阵A
A = np.array([[1, -1, 0],
              [0, 1, -1],
              [-1, 0, 1]])

# 对矩阵方程AX = A + 2X进行变形得到(A - 2E)X = A，先构造A - 2E
E = np.eye(3)  # 3阶单位矩阵
A_minus_2E = A - 2 * E

# 构造增广矩阵[A - 2E | A]
augmented_matrix = np.hstack((A_minus_2E, A))

# 进行初等行变换，将增广矩阵化为行最简形
from sympy import Matrix
augmented_matrix_sympy = Matrix(augmented_matrix)
row_echelon_form = augmented_matrix_sympy.rref()[0]

# 提取行最简形中对应X的部分
X = np.array(row_echelon_form[:, 3:]).astype(float)
print(X)