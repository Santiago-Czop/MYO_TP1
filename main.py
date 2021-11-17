from utils import *


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
    print(f"Best Time: {top_result}")

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

main()