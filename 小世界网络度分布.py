import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# 定义求度分布的函数
def get_pdf(G, K):
    N = len(G.nodes())

    Pk = []
    for ki in K:
        c = 0
        for i in G.nodes():
            if G.degree(i) == ki:
                c += 1
        Pk.append((c/N))

    return Pk


# 以N=1000，K=6的WS模型的数值模拟结果为例
N = 100
K = 6
samples = 1000  # 统计平均次数
p_rew = [0.1, 0.2, 0.4, 0.6, 1.0]

plt.figure(figsize=(8, 6))
symbols = ["ro-", "bs-", "g*-", "yv-", "k^-"]
# 为了便于求统计平均，指定区间[1, 16]
kmin, kmax = 1, 16
x = list(range(kmin, kmax+1))
c = 0
for p in p_rew:
    s = np.zeros(kmax-kmin+1)
    for i in range(samples):
        G = nx.watts_strogatz_graph(N, K, p)  # K 参数：表示每个节点的初始邻居数量。p 参数：用于控制网络中的 “随机重连” 概率。
        y = get_pdf(G, x)
        s += np.array(y)

    s = list(s)
    # 剔除概率为0的点
    new_x = []
    new_y = []
    for i in range(len(x)):
        if s[i] != 0:
            new_x.append(x[i])
            new_y.append(s[i])

    plt.plot(new_x, np.array(new_y)/samples, symbols[c], label='$p_{rew}=$'+str(p))
    c += 1

plt.legend(loc=0, fontsize=14)
plt.xlabel("$k$")
plt.ylabel("$p_k$")
plt.yscale("log")
plt.xlim([kmin, kmax])
plt.show()


