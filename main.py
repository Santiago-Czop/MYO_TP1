from os import rename
from os import remove
import time


def main():
    start_time = time.perf_counter()
    incompatibility_graph, times_dict = load_incompatibility_graph_and_times_dict()
    top_result = evaluate_result(times_dict, "best_time.txt")
    washing_sets = find_washing_sets(incompatibility_graph, times_dict)
    generate_output(washing_sets)
    result = evaluate_result(times_dict)
    if result < top_result:
        keep_best_result()
        top_result = result
    print(f"Best Time: {top_result}")
    end_time = time.perf_counter()
    log_time(end_time - start_time)     
    print_avg_time()  

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
        washing_sets.add(frozenset(washing_set)) 

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
    with open("output.txt", "w") as output_file:
        wash = 1
        for washing_set in washing_sets:
            for cloth in washing_set:
                output_file.write(f"{cloth} {wash}\n")
            wash += 1

def evaluate_result(times_dict, result_file="output.txt"):
    washes = {}

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

    #print(f"Total Time: {tot_time}")
    return tot_time

def keep_best_result():
    try:
        rename("output.txt", "best_time.txt")
    except FileExistsError:
        remove("best_time.txt")
        rename("output.txt", "best_time.txt")

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

def log_time(time):
    with open("time_logs.txt", "a") as my_file:
        my_file.write(f"{time}\n")

def print_avg_time():
    time_sum = 0
    time_count = 0
    with open("time_logs.txt", "r") as my_file:
        for line in my_file:
            time_sum += float(line.rstrip("\n"))
            time_count += 1
    print(f"Avg Time: {time_sum / time_count}")

main()