from os import rename
from os import remove
from os import path
import time

# Loads the file with the washing data.
# Returns the graph of incompatibilities and the dict with the washing times    

def load_incompatibility_graph_and_times_dict():
    incompatibility_graph = {}
    times_dict = {}
    with open("tercer_problema.txt", "r") as my_file:
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

# Generates output for the format of a set of washing sets
def generate_output(washing_sets):
    with open("output.txt", "w") as output_file:
        wash = 1
        for washing_set in washing_sets:
            for cloth in washing_set:
                output_file.write(f"{cloth} {wash}\n")
            wash += 1

# Generates output for the format of a colored graph
def generate_output_coloring(washing_sets):
    with open("output.txt", "w") as output_file:
        for k,v in washing_sets.items():
            output_file.write(f"{k} {v+1}\n")

def generate_output_cplex(washing_sets):
    washing_list = []
    with open("lavados_entrega_3_97.txt", "r") as input_file:
        for line in input_file:
            washing_list.append(tuple(line.rstrip('\n').split(" ")))
            washing_list.sort(key=lambda t: t[0])
        with open("output_for_cplex.txt", "w") as output_file:
            for t in washing_list:
                output_file.write(f"coloreoValido[{t[0]}] = {t[1]};\n")

# Calculates the time spent
def evaluate_result(times_dict, result_file="output.txt"):
    washes = {}

    if not path.isfile(result_file):
        return float("inf")
    
    with open(result_file, "r") as output_file:
        for line in output_file:
            cloth, wash = line.rstrip('\n').split(' ')
            if wash not in washes.keys():
                washes[wash] = times_dict[cloth]
            else:
                if times_dict[cloth] > washes[wash]:
                    washes[wash] = times_dict[cloth]

    tot_time = 0
    for k,v in washes.items():
        tot_time += v

    return tot_time


# Prints the time of each washing set
def print_washes_times(times_dict):
    washes = {}

    if not path.isfile("output.txt"):
        return float("inf")
    
    with open("output.txt", "r") as output_file:
        for line in output_file:
            cloth, wash = line.rstrip('\n').split(' ')
            if wash not in washes.keys():
                washes[wash] = times_dict[cloth]
            else:
                if times_dict[cloth] > washes[wash]:
                    washes[wash] = times_dict[cloth]
    
    for k,v in washes.items():
        print(f"{v} - {k}")

# Replaces best_time.txt with output.txt
def keep_best_result():
    try:
        rename("output.txt", "best_time.txt")
    except FileExistsError:
        remove("best_time.txt")
        rename("output.txt", "best_time.txt")
