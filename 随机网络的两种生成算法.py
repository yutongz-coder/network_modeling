# G(N,L)模型：N个节点通过L条随机放置的链接彼此相连，Erdos和Renyi在他们关于随机网络的系列论文中采用的是这种定义方式
# G(N,p)模型：N个节点中，每对节点之间以概率p彼此相连

import random
import itertools
import networkx as nx
import matplotlib.pyplot as plt

def gnl(N, L):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    nlist = list(G)
    edge_count = 0
    while edge_count < 1:
        # generate random edge u,v
        u = random.choice(nlist)
        v = random.choice(nlist)
        if u == v or G.has_edge(u, v):
            edge_count += 1
    return G


G = gnl(100, 200)


def gnp(N, p):
    edges = itertools.combinations(range(N), 2)
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for e in edges:
        if random.random() < p:
            G.add_edge(*e)
    return G


GNP = gnp(100, 0.6)

# 可以直接调用库函数来生成这两种网络
n, m, p = 20, 40, 0.2
g1 = nx.gnm_random_graph(n, m)
g2 = nx.gnp_random_graph(n, p)

plt.figure(figsize=(8, 4))

plt.subplot(121)
nx.draw(g1, pos=nx.circular_layout(g1), node_size=300, node_color="red", with_labels=True)
plt.title("G(N,L)")

plt.subplot(122)
nx.draw(g2, pos=nx.circular_layout(g2), node_size=300, node_color="red", with_labels=True)
plt.title("G(N,p)")

plt.show()



