import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# ba=nx.barabasi_albert_graph(100,5)
# nx.draw(ba)
# nx.draw_random(ba)
# nx.draw_circular(ba)
# nx.draw_spectral(ba)
#
# plt.show()
# plt.clf()

# nx.draw(G)
# plt.savefig("path.png")

nodes_df = pd.read_csv("/media/vasy/Data/Doksik/Learn/thesis/fault_pred/tidy_data/nodes.csv", parse_dates=True)
edges_df = pd.read_csv("/media/vasy/Data/Doksik/Learn/thesis/fault_pred/tidy_data/edges/1503        _edges.csv", parse_dates=True)

nodes_df = nodes_df[["node_name","node_type_e_or_f"]]

G = nx.DiGraph()


for index, row in nodes_df.iterrows():
    G.add_node(row["node_name"],node_type=row["node_type_e_or_f"])

edges_df["from_node"] = edges_df['to_go_node'].shift()

#Temp solution
#TODO initial phase for forklifts

edges_df["from_node"] = edges_df['to_go_node'][0]

G = nx.from_pandas_dataframe(edges_df, source= "from_node",target='to_go_node', edge_attr=['timestamp', 'vehicle_serialnumber','fail_in','fail_out'])

plt.clf()
pos = nx.random_layout(G)
#TODO edit drawing board size
nx.draw(G,pos,nodes_size = 1,alpha = 0.1,node_color='b',node_shape = ".")
