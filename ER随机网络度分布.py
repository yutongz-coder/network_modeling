import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats

# 随机网络的度分布的精确形式是二项分布。当节点个数N远大于平均度分布<k>时，二项分布可以很好地近似为泊松分布
# 大部分真实网络是稀疏的，意味着这些网络的平均度远小于网络大小
# 定义求度分布的函数
def get_pdf(G, kmin, kmax):
    k = list(range(kmin, kmax+1))  # 获取所有可能的度值
    N = len(G.nodes())

    Pk = []
    for ki in k:
        c = 0
        for i in G.nodes():
            if G.degree(i) == ki:
                c += 1
        Pk.append(c/N)

    return k, Pk


samples = 100   # 统计平均
# N是一个列表，第一个元素为100，第二个元素为1000
N = [100, 1000]
# 为了便于求统计平均，指定区间[20, 80]
kmin, kmax, avk = 20, 80, 50
# np.zeros(kmax - kmin + 1) 就会创建一个长度为 kmax - kmin + 1 的数组，这个数组中的所有元素初始值都为 0。
# 最终创建好的全零数组被赋值给变量 s1
s1 = np.zeros(kmax - kmin + 1)
s2 = np.zeros(kmax - kmin + 1)
for i in range(samples):
    ER1 = nx.gnp_random_graph(N[0], avk/N[0])
    x1, y1 = get_pdf(ER1, kmin, kmax)
    ER2 = nx.gnp_random_graph(N[1], avk/N[1])
    x2, y2 = get_pdf(ER2, kmin, kmax)

    s1 += np.array(y1)
    s2 += np.array(y2)

# 计算二项分布理论值
n = 100
p = 0.5
# arange 函数接收两个参数，分别是 20 和 81。这表示创建的数组 k 的起始值是 20，结束值是 80（注意不包括结束值本身，这是 arange 函数的特点），元素之间的间隔是 1
k = np.arange(20, 81)
pk_b = stats.binom.pmf(k, n, p)

#  计算泊松分布理论值
# 通过 math.factorial(ki) 来获取 ki 的阶乘值
# λ 是泊松分布的参数（在代码中用变量 avk 表示）
# 最终列表 pk_p 就存储了泊松分布在从 kmin 到 kmax 这个取值范围内各个离散点上的理论概率值
pk_p = [np.exp(-avk)*(avk**ki)/math.factorial(ki) for ki in range(kmin, kmax+1)]

# 绘图度分布图
plt.figure(figsize=(6, 4))
plt.plot(x1, s1/samples, 'ro', label='$N = 100$')
plt.plot(x2, s2/samples, 'bs', label='$N = 1000$')
plt.plot(x2, pk_b, 'g-', label='binomial')
plt.plot(x2, pk_p, 'r-', label="poisson")
plt.legend(loc=0)
plt.xlabel("$k$")
plt.ylabel("$p_k$")
plt.xlim([20, 80])
# 100个节点的网络度分布近似于二项分布，1000个节点的网络度分布近似于泊松分布
plt.show()




