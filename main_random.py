from utils import *
import random

def main():
    incompatibility_graph, times_dict = load_incompatibility_graph_and_times_dict()
    top_result = evaluate_result(times_dict, "best_time.txt")
    washing_sets = find_washing_sets(incompatibility_graph, times_dict)
    generate_output(washing_sets)
    result = evaluate_result(times_dict)
    if result < top_result:
        keep_best_result()
        top_result = result
    print(f"Time: {result}")
    #print(f"Best Time: {top_result}")

def find_washing_sets(inc_graph, times_dict):
    clothes_by_time = get_clothes_by_time(times_dict)

    washing_sets = set()
    to_be_washed_set = set()
    for v in get_vertexes(inc_graph):
        to_be_washed_set.add(v)
    
    while to_be_washed_set:
        washing_set, to_be_washed_set = find_washing_set(to_be_washed_set, inc_graph, times_dict, clothes_by_time)
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

def find_washing_set(clothes_set, inc_graph, times_dict, clothes_by_time):
    washing_set = set()
    incompatible_clothes = set()
    while len(clothes_set) > 0:
        slowest_time = times_dict[max(clothes_set, key=lambda v: times_dict[v])]
        print(slowest_time)
        slowest_clothes = [k for k in clothes_set if times_dict[k] == slowest_time]
        slowest_cloth = slowest_clothes[random.randint(0, len(slowest_clothes) - 1)]
        for v in get_adyacents(inc_graph, slowest_cloth):
            if v in clothes_set:
                clothes_set.remove(v)
                incompatible_clothes.add(v)
        clothes_set.remove(slowest_cloth)
        washing_set.add(slowest_cloth)      
    print("SET")
    return washing_set, incompatible_clothes  

def _find_washing_set(): 
    pass

main()