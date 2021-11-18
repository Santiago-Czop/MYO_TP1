import networkx
from networkx.drawing.nx_pylab import draw
import bron_kerbosch
import matplotlib.pyplot as plt

def draw_graph(graph):
    g = networkx.Graph()

    for k, vs in graph.items():
        for v in vs:
            if v in graph.keys(): g.add_edge(k,v)

    pos = networkx.shell_layout(g)
    networkx.draw_networkx_nodes(g, pos, cmap=plt.get_cmap('jet'), node_size=20)
    networkx.draw_networkx_edges(g, pos)
    networkx.draw_networkx_labels(g, pos)
    plt.show()


#my_graph = {6: {4}, 5: {4, 2, 1}, 4: {6,5,3}, 3: {4,2}, 2: {3,5,1}, 1: {5,2}}
#print(list(bron_kerbosch.bron_kerbosch(my_graph, my_graph[4], R={4})))
#draw_graph(my_graph)
