import torch
from torch import linalg

# 创建标量
x = torch.tensor(3.0)
y = torch.tensor(2.0)

print(x + y, x - y, x * y, x / y, x ** y)

# 创建向量
x = torch.arange(4, dtype=torch.float32)

# 访问向量中的元素
print(x[2])

# 向量的维数/长度
print(len(x))

"""向量可以看作只有一个轴的张量，可以使用shape访问向量的长度，对于张量，shape返回的是每个轴的长度"""
print(x.shape)

# 矩阵，即有两个轴的张量
A = torch.arange(20).reshape(5, 4)
print(A)

# 矩阵的转置
B = A.T
print(B)

# 张量，即可以有n个轴的多维数组
C = torch.arange(16).reshape(2, 2, 4)
print(C)

# 两个矩阵按元素相乘即对应位置相乘，称为hadamard积
A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.clone()

print(A * B)

# 张量与标量的乘法和加法是每个元素都与标量运算
print(A * 2)
print(A + 2)

# 调用sum对张量求和
print(A.sum())

# 求和是按 0 ：行， 1 ：列方向将张量降维成标量，指定求和所有行时，行的维数在输出形状中消失了：
A_sum_axis0 = A.sum(axis=0)
print(A)
print(A.shape)
print(A_sum_axis0)
print(A_sum_axis0.shape)

# 当指定求和所有列时，列的维数在输出形状中消失了
A_sum_axis1 = A.sum(axis=1)
print(A_sum_axis1)
print(A_sum_axis1.shape)

# 沿着行列同时求和，等价于对所有元素求和
A_sum = A.sum(axis=[0, 1])
print(A_sum)

# 求行、列的平均值
print(A.mean())
print(A.sum() / A.numel())
print(A.mean(axis=0))
print(A.sum(axis=0) / A.shape[0])

# 如果不想降维求和，可以使用 keepdims 实现
sum_A = A.sum(axis=1, keepdims=True)
print(A / sum_A)
"""这里sum_A是5*1的矩阵，根据广播机制，会先复制成为5*4的，然后A的各个元素对应相除"""

# 可以用cumsum实现对某个轴的积累和
print(A)
print(A.cumsum(axis=0))

# 向量的点积即对应元素相乘再相加
print(x)
y = torch.ones(4, dtype=torch.float32)
print(y)
print(torch.dot(x, y))

# 等价写法
print(torch.sum(x * y))

# 矩阵-向量积，即Ax，调用mv函数，要求A的列数等于x的长度，
print(A.shape, x.shape)
print(torch.mv(A, x))

# 矩阵乘法，常规意义上到一行乘以一列，调用mm实现
B = torch.ones(4, 3)
print(torch.mm(A, B))

# L2范数，即向量中元素的平方和的平方根，调用norm计算
u = torch.tensor([3.0, -4.0])
print(torch.norm(u))

# L1范数，即向量中元素的绝对值之和
print(torch.abs(u).sum())

# 矩阵的L2范数与向量类似，矩阵的每个元素的平方和再开方
v = torch.ones(4, 9)
print(torch.norm(v))

t = torch.ones(2, 3, 4)
print(t)
print(t.sum(axis=0).shape)
print(t.sum(axis=1).shape)
print(t.sum(axis=2).shape)
print(linalg.norm(t))
print(torch.norm(t))
