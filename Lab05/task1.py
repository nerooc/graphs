from lab05 import *

NUMBER_OF_LAYERS=2

pos,vertices_in_layers=rand_vertices(NUMBER_OF_LAYERS)
#list of all vertices' values
vertices=list(pos.keys())


#edges generated from minimal number of edges needed to connect all nodes to sink and source 
edges_part_1=add_random_minimal_edges_from_source_to_sink(vertices_in_layers)
#edges generated as 2*N random edges
edges_part_2=add_2N_random_edges(edges_part_1, vertices,NUMBER_OF_LAYERS)

G = nx.DiGraph()

for i in pos:
    G.add_node(i)

for (i,j) in edges_part_1:
    G.add_edge(i,j, weight= random.randint(1,10))

for (i,j) in edges_part_2:
    G.add_edge(i,j, weight =random.randint(1,10))

edges_with_weights=G.edges(data=True)
for i in edges_with_weights:
    print(i)

#adjacency matrix will be generated in a way that it will be compatibile with lab04.py functions (graph drawing and printing adjacency list/incidence matrix)
adj_matrix=generate_zeroed_adjacency_matrix(len(vertices))
adj_matrix=fill_adjacency_matrix(adj_matrix,edges_with_weights)
print("----ADJACENCY MATRIX OF YOUR FLOW NET:----\n")
pretty_print(adj_matrix)

"""
x=[(u, v) for (u, v, d) in G.edges(data=True)]
x2=x[0:2]
nx.draw_networkx_nodes(G, pos, node_size = 300, node_color = 'blue')

nx.draw_networkx_labels(G,pos,font_size=10)
nx.draw_networkx_edges(
    G,pos, edgelist=x2,
    connectionstyle="arc3,rad=0.4"
)
nx.draw_networkx_edges(
    G,pos, edgelist=x[2:],
)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

"""
nx.draw_networkx_nodes(G, pos, node_size = 300, node_color = 'blue')

nx.draw_networkx_labels(G,pos,font_size=10)
nx.draw_networkx_edges(
    G,pos#,connectionstyle="arc3,rad=0.1" #zakrzywiamy lekko dla czytelności 
)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.axis('square')

plt.show()


#PROBLEMY: 
#Jak linia jest prosta to jak edge przechodzi przez inny edge to waga sie nie pokazuje
#Jak linia jest zakrzywiona to jak np dwie długie się przecinają to też waga się nie pokazuje xDDD