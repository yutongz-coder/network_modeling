import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def C_vs_k(G):
    klist = [G.degree(i) for i in G.nodes()]
    # 计算每个节点的集聚系数
    all_C = {i: nx.clustering(G, i) for i in G.nodes()}
    all_k = list(set(klist))  # 所有可能的度值

    # 计算度值为k的节点的集聚系数的平均值
    C_k = {}
    for k in sorted(all_k):
        s = 0
        j = 0
        for i in G.nodes():
            if G.degree(i) == k:
                j = j + 1
                s = s + all_C[i]
        avc_k = s / j
        C_k[k] = avc_k

    return C_k


df = pd.read_csv("数据/citation.csv")
G = nx.from_pandas_edgelist(df, 'source', 'target', create_using=nx.Graph())
len(G.nodes())

C_k = C_vs_k(G)
avC = nx.average_clustering(G)
print(avC)
x = np.linspace(1, 10000, 10000)
y = [avC]*10000

plt.figure(figsize=(6,4))
plt.plot(C_k.keys(), C_k.values(), 'ro')
plt.plot(x, y, 'b-')
plt.xlabel("$k$")
plt.ylabel("$C(k)$")
plt.xscale("log")
plt.yscale("log")
plt.xlim([1,1e4])
# plt.savefig("C(k)_k_citation.png", dpi=600)
plt.show()
