import igraph as ig
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def cal_by_igraph(samples, N):
    avl, clu = [], []
    t_avl, t_clu = [], []
    for n in N:
        m = 5*n
        avl0 = 0
        clu0 = 0
        t_avl0 = 0
        t_clu0 = 0
        for i in range(samples):
            Ger = ig.Graph.Erdos_Renyi(n=n, m=m)
            avk = sum(Ger.degree()) / n
            # 理论近似值
            t_avl0 += np.log(n) / np.log(avk)
            t_clu0 += avk / n

            # 模拟值
            avl0 += Ger.average_path_length()
            clu0 += Ger.transitivity_avglocal_undirected(mode='zero')

        avl.append(avl0 / samples)
        clu.append(clu0 / samples)
        t_avl.append(t_avl0 / samples)
        t_clu.append(t_clu0/samples)
    return avl, clu, t_avl, t_clu

# 耐心等待，计算这些指标比较耗时
samples = 10  # 为了使结果更加精确，通常需要将samples设置为较大的值.这里为了快速得到结果，可以取为1个样本
N = [100,200,300,500,700,1000,2000,5000]
# avl_0, clu_0, t_avl0, t_clu0 = cal_by_networkx(samples, N) # 速度较慢
avl_0, clu_0, t_avl0, t_clu0 = cal_by_igraph(samples, N)

plt.figure(figsize=(10,4))
plt.subplot(121)
plt.plot(N, avl_0, 'ro', label='simulation')
plt.plot(N, t_avl0, 'r--', label='theory predicts')
plt.title("average path length")
plt.legend(loc=0)
plt.xlabel("$N$")
plt.ylabel("$<l>$")
plt.xscale("log")

plt.subplot(122)
plt.plot(N, clu_0, 'ro', label='simulation')
plt.plot(N, t_clu0, 'r--', label='theory predicts')
plt.title("average clustering")
plt.legend(loc=0)
plt.xlabel("$N$")
plt.ylabel("$<C>$")
plt.xscale("log")
plt.yscale("log")
plt.show()
