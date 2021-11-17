# Loads the file with the washing data.
# Returns the graph of incompatibilities and the dict with the washing times    

def load_incompatibility_graph_and_times_dict():
    incompatibility_graph = {}
    times_dict = {}
    with open("segundo_problema.txt", "r") as my_file:
        for line in my_file:
            line = line.rstrip('\n').strip(' ')
            if line[0] == 'c': continue # A comment
            if line[0] == 'p': continue # Unnecessary info
            if line[0] == 'e': load_edge(incompatibility_graph, line)
            if line[0] == 'n': load_time(times_dict, line)
    return incompatibility_graph, times_dict

def load_edge(graph, line):
    _, cloth_1, cloth_2 = line.split(' ')
    add_vertex(graph, cloth_1)
    add_vertex(graph, cloth_2)
    add_edge(graph, cloth_1, cloth_2)
    add_edge(graph, cloth_2, cloth_1)

def load_time(times, line):
    _, cloth, time = line.split(' ')
    times[cloth] = int(time)

#Adds a new vertex with no edges to the graph
def add_vertex(graph, v):
    if v not in graph: graph[v] = set()

#Connects v to w in the graph
def add_edge(graph, v, w):
    graph[v].add(w)

#Returns an iterator of the vertexes in graph
def get_vertexes(graph):
    return graph.keys()

#Returns a set of the vertexes connected to v
def get_adyacents(graph, v):
    return graph[v]