import networkx as nx
import matplotlib.pyplot as plt

ba=nx.barabasi_albert_graph(100,5)
nx.draw(ba)
nx.draw_random(ba)
nx.draw_circular(ba)
nx.draw_spectral(ba)

plt.show()
plt.clf()

# nx.draw(G)
# plt.savefig("path.png")