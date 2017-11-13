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
edges_df = pd.read_csv("/media/vasy/Data/Doksik/Learn/thesis/fault_pred/tidy_data/edges/516210C00190_edges.csv", parse_dates=True)

nodes_df = nodes_df[["node_name","node_type_e_or_f"]]

G = nx.DiGraph()


for index, row in nodes_df.iterrows():
    G.add_node(row["node_name"],node_type=row["node_type_e_or_f"])

#G.add_path([edges_df[["to_go_node"]]])

#,[edges_df[['timestamp']],edges_df[['vehicle_serialnumber']],edges_df[['fail_in']],edges_df[['fail_out']]]

edges_df["from_node"] = edges_df['to_go_node'].shift()

#Temp solution
#TODO initial phase for forklifts

edges_df.from_node[0] = edges_df['to_go_node'][0]

G = nx.from_pandas_dataframe(edges_df, source= "from_node",target='to_go_node', edge_attr=['timestamp', 'vehicle_serialnumber','fail_in','fail_out'])

plt.clf()
#pos = nx.circular_layout(G)
pos = nx.shell_layout(G)
#pos = nx.spring_layout(G)
#TODO edit drawing board size
nx.draw_networkx_nodes(G,pos,nodes_size = 1,alpha = 1,node_color='b',node_shape = ".",arrows=True)
nx.draw_networkx_edges(G,pos,alpha = 1,edge_color='r',arrows=True)
plt.show()

####################################################################################################
G = nx.DiGraph()
G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
     ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])

val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'H': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here
red_edges = [('A', 'C'), ('E', 'C')]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()
####################################################################################################
