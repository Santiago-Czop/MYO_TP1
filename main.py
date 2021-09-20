def main():
    incompatibility_graph, times_dict = load_incompatibility_graph_and_times_dict()
    washing_sets = find_washing_sets(incompatibility_graph)
    generate_output(washing_sets)

# Loads the file with the washing data.
# Returns the graph of incompatibilities and the dict with the washing times    
def load_incompatibility_graph_and_times_dict():
    incompatibility_graph = {}
    times_dict = {}
    with open("primer_problema.txt", "r") as my_file:
        for line in my_file:
            line = line.rstrip('\n').strip(' ')
            if line[0] == 'c': continue # A comment
            if line[0] == 'p': continue # Unnecessary info
            if line[0] == 'e': load_edge(incompatibility_graph, line)
            if line[0] == 'n': load_time(times_dict, line)
    return incompatibility_graph, times_dict

def find_washing_sets(inc_graph, times_dict):
    washing_sets = set()
    to_be_washed_set = set()
    for v in get_vertexes(inc_graph):
        to_be_washed_set.add(v)
    
    while len(to_be_washed_set) > 0:
        washing_set, to_be_washed_set = find_washing_set(to_be_washed_set, inc_graph, times_dict)
        washing_sets.add(washing_set) 

    return washing_sets
    
def find_washing_set(clothes_set, inc_graph, times_dict):
    washing_set = set()
    incompatible_clothes = set()
    while len(clothes_set) > 0:
        slowest_cloth = max(clothes_set, key=lambda v: times_dict[v])
        for v in get_adyacents(inc_graph, slowest_cloth):
            if v in clothes_set:
                clothes_set.remove(v)
                incompatible_clothes.add(v)
        clothes_set.remove(slowest_cloth)
        washing_set.add(slowest_cloth)      
    return washing_set, incompatible_clothes  

def generate_output(washing_sets):
    pass

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

def load_edge(graph, line):
    _, cloth_1, cloth_2 = line.split(' ')
    add_vertex(graph, cloth_1)
    add_vertex(graph, cloth_2)
    add_edge(graph, cloth_1, cloth_2)
    add_edge(graph, cloth_2, cloth_1)

def load_time(times, line):
    _, cloth, time = line.split(' ')
    times[cloth] = int(time)

main()