from utils import *

def main():
    incompatibility_graph, times_dict = load_incompatibility_graph_and_times_dict()
    washing_sets = find_washing_sets(incompatibility_graph, times_dict)

def find_washing_sets(inc_graph, times_dict):
    # I'll try to optimize the code by doing as much work as possible only once
    clothes_by_time = get_clothes_by_time(times_dict)

    washing_sets = set()
    top_time = float("inf")
    to_be_washed_set = set()
    for v in get_vertexes(inc_graph):
        to_be_washed_set.add(v)
    
    while to_be_washed_set:
        washing_set, to_be_washed_set = find_washing_set(to_be_washed_set, inc_graph, times_dict)
        washing_sets.add(frozenset(washing_set)) 

    return washing_sets


def get_clothes_by_time(times_dict):
    clothes_by_time = dict()

    times_dict_copy = dict(times_dict)
    while times_dict_copy:
        slowest_time = max(times_dict_copy.values())
        clothes_by_time[slowest_time] = [k for k,v in times_dict_copy.items() if v == slowest_time]
        for k in clothes_by_time[slowest_time]:
            del times_dict_copy[k]
    return clothes_by_time

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

def _find_washing_set(): 
    pass

main()