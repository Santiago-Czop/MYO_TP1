import bron_kerbosch
from utils import *

def main():
    incompatibility_graph, times_dict = load_incompatibility_graph_and_times_dict()
    clothes_by_time = get_clothes_by_time(times_dict)
    print(clothes_by_time[20])
    inc_subgraph = {k : v for k,v in incompatibility_graph.items() if k in clothes_by_time[20]}
    # Invert the incompatibility graph into a compatibility graph
    compatibility_graph = {}
    for k in incompatibility_graph.keys():
        compatibility_graph[k] = {v for v in incompatibility_graph.keys() if (k != v and v not in incompatibility_graph[k])}
    comp_subgraph = {k : v for k,v in compatibility_graph.items() if k in clothes_by_time[20]}
    
    time_start = time.process_time()
    print(list(bron_kerbosch.bron_kerbosch(comp_subgraph)))
    print(time.process_time() - time_start)

    pass

def get_clothes_by_time(times_dict):
    clothes_by_time = dict()

    times_dict_copy = dict(times_dict)
    while times_dict_copy:
        slowest_time = max(times_dict_copy.values())
        clothes_by_time[slowest_time] = [k for k,v in times_dict_copy.items() if v == slowest_time]
        for k in clothes_by_time[slowest_time]:
            del times_dict_copy[k]
    return clothes_by_time

main()