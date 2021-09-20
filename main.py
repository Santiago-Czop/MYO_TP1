def main():
    incompatibility_graph = get_incompatibility_graph()
    washing_sets = find_washing_sets(incompatibility_graph)
    generate_output(washing_sets)

    
def load_incompatibility_graph():
    incompatibility_graph = {}
    with open("primer_problema.txt", "r") as my_file:
        for line in my_file:
            line = line.rstrip('\n').strip(' ')
            if line[0] == 'c': continue
            if line[0] == 'p': continue #No necesito esta info, la obtengo despues
            if line[0] == 'e': pass # TODO Codear esto
            if line[0] == 'n': pass # TODO Codear esto


def find_washing_sets(inc_graph):
    pass

def generate_output(washing_sets):
    pass

#Adds a new vertex with no edges to the graph
def add_vertex(graph, v):
    if v not in graph: graph[v] = set()

#Connects v to w in the graph
def add_edge(graph, v, w):
    graph[v].add(w)

main()