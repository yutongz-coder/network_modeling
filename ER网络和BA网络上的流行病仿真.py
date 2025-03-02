import networkx as nx
import matplotlib.pyplot as plt
import EoN

N = 10**4
# M 的值被设定为 4*N（也就是 40000），在 nx.gnm_random_graph 函数中，M 参数用于指定网络中边的数量
M = 4*N
# t 代表模拟的时间序列（是一个包含多个时间点的列表或者数组，对应从模拟开始到 tmax 这段时间内的各个时间步长）
ER = nx.gnm_random_graph(N, M)

# SIS
tau = 0.5          # transmission rate
gamma = 0.2     # recovery rate per node
t, S, I = EoN.fast_SIS(ER, tau=tau, gamma=gamma, tmax = 10)
plt.plot(t, S, color='r', label='S')
plt.plot(t, I, color='b', label='I')
plt.legend(loc=0)
plt.xlabel("$T$")
plt.ylabel("individuals")
plt.show()

tau = 0.5           # transmission rate
gamma = 1.0    # recovery rate
rho = 0.05      # random fraction initially infected

# SIR
t, S, I, R = EoN.fast_SIR(ER, tau, gamma, rho=rho, tmax = 20)
plt.plot(t, S, color = 'r', label='S')
plt.plot(t, I, color = 'b', label='I')
plt.plot(t, R, color = 'g', label='R')
plt.legend(loc=0)
plt.xlabel("$T$")
plt.ylabel("individuals")
plt.show()
