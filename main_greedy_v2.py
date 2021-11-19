import utils
import random
import collections
import itertools
import networkx as nx
import copy

def main():
    incompatibility_graph, times_dict = utils.load_incompatibility_graph_and_times_dict()
    top_result = utils.evaluate_result(times_dict, "best_time.txt")
    washing_sets = find_washing_sets(incompatibility_graph)
    utils.generate_output_coloring(washing_sets)
    result = utils.evaluate_result(times_dict)
    if result < top_result:
        utils.keep_best_result()
        top_result = result
    print(f"Time: {result}")
    print(f"Best Time: {top_result}")

def find_washing_sets(incompatibility_graph):
    G = nx.Graph()

    for k, vs in incompatibility_graph.items():
        for v in vs:
            if v in incompatibility_graph.keys(): G.add_edge(k,v)

    clothes = list(incompatibility_graph.keys())
    clothes = my_strategy_smallest_last(incompatibility_graph)

    result = {}
    for cloth in clothes:
        used_colors = {result[vertex] for vertex in utils.get_adyacents(incompatibility_graph, cloth) if vertex in result}
        result[cloth] = first_available(used_colors)

    print(max(result.values()))
    return result

def my_strategy_smallest_last(graph):
    G = copy.deepcopy(graph)
    result = []

    # Construyo la lista de menor a mayor y la invierto al devolverla
    for _ in graph.keys():
        candidate = min(G.keys(), key=lambda x: len(G[x]))
        candidates = [k for k,v in G.items() if len(v) == len(G[candidate])]
        u = random.choice(candidates)
        result.append(u)
        for v in utils.get_adyacents(G, u):
            G[v].remove(u)
        del G[u]
    
    return reversed(result)


def first_available(used_colors):
    count = 1
    while True:
        if count not in used_colors:
            return count
        count += 1

main()