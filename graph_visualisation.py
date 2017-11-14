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
edges_df = pd.read_csv("/media/vasy/Data/Doksik/Learn/thesis/fault_pred/tidy_data/edges/510148C00180      _edges.csv",
                       parse_dates=True)

nodes_df = nodes_df[["node_name", "node_type_e_or_f"]]
#TODO solve time type problem
#TODO solve empty to_go_node_problem
edges_df['timestamp'] = pd.to_datetime(edges_df['timestamp'], format='%d.%m.%Y')
#edges_df['timestamp'] = pd.to_datetime(edges_df['timestamp'], format='%d/%m/%Y %H:%M:%S')

edges_df = edges_df.sort_values(by='timestamp')

G = nx.DiGraph()

for index, row in nodes_df.iterrows():
    G.add_node(row["node_name"], node_type=row["node_type_e_or_f"])

# G.add_path([edges_df[["to_go_node"]]])

# ,[edges_df[['timestamp']],edges_df[['vehicle_serialnumber']],edges_df[['fail_in']],edges_df[['fail_out']]]



# Temp solution
# TODO initial phase for forklifts

edges_df["from_node"] = edges_df['to_go_node'].shift()
edges_df.from_node[0] = edges_df['to_go_node'][0]


# TODO ends
G = nx.from_pandas_edgelist(edges_df, source="from_node", target='to_go_node',
                            edge_attr=['timestamp', 'vehicle_serialnumber', 'fail_in', 'fail_out'],
                            create_using=nx.DiGraph()
                            )

plt.clf()
# pos = nx.circular_layout(G)
shell_df = edges_df.drop_duplicates("to_go_node",keep='first')
shell = [[rows.to_go_node for index, rows in shell_df.iterrows() if rows.fail_in],
         [rows.to_go_node for index, rows in shell_df.iterrows() if not rows.fail_in]]
pos = nx.shell_layout(G,shell)
# pos = nx.spring_layout(G)
# pos = nx.random_layout(G)
# TODO edit drawing board size
nx.draw_networkx_nodes(G, pos, nodes_size=1, alpha=1, node_color='b', node_shape=".", arrows=True)
nx.draw_networkx_edges(G, pos, alpha=1, edge_color='r', arrows=True)
plt.show()

####################################################################################################
