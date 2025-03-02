import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# 设置初始参数
N, K = 1000, 10
samples = 10
# logspace 函数用于创建一个等比数列
# logspace 函数接收三个参数，分别是 0、4 和 10。
# 第一个参数 0 表示数列起始值的以 10 为底的对数（也就是起始值为 10^0 = 1）；第二个参数 4 表示数列结束值的以 10 为底的对数（即结束值为 10^4 = 10000）；第三个参数 10 表示要生成的数列中元素的个数
p_rew = np.logspace(0, 4, 10)/10000
print(p_rew)

# 平均距离与平均集聚系数
C = []
CT = []  # 理论近似值：{[3(K-2)]/[4(K-1)]}*(1-p)^3
L = []
for p in p_rew:
    s1 = 0
    s2 = 0
    for i in range(samples):
        # 为了防止在计算平均距离时报错：最好改用生成连通WS小世界网络函数connected_watts_strogatz_graph()
        G = nx.connected_watts_strogatz_graph(N, K, p)
        s1 += nx.average_clustering(G)
        s2 += nx.average_shortest_path_length(G)

    # 理论值
    ct = (3 * (K - 2) / (4 * (K - 1))) * ((1 - p) ** 3)
    CT.append(ct)
    C.append(s1 / samples)
    L.append(s2 / samples)

plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.plot(p_rew, C, 'ro', label='$C(p)$')
plt.plot(p_rew, CT, 'r-', label='$CT(p)$')
plt.legend(loc=0, fontsize=14)
plt.xlabel("$p$")
plt.xscale("log")

plt.subplot(122)
plt.plot(p_rew, L, 'bs', label='$L(p)$')
plt.legend(loc=0, fontsize=14)
plt.xlabel("$p$")
# plt.xscale("log")
# plt.yscale("log")
plt.show()
# plt.savefig("C_L.png", dpi=600)


