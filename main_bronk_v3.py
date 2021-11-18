import bron_kerbosch
from test import draw_graph
from utils import *
import random

""" Esta version intenta arrancar a armar el washing set usando el clique más grande por tiempo, 
    sin importar si es eficiente. Si el clique más grande es el de ropa que tarda 1, arranca por ahí
    y sigue por el siguiente que encuentre compatible con ese sin importar el tiempo, y así hasta terminar.
    Es incluso más lento, y dio resultados siempre superiores a 700.
"""

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

def get_clothes_by_time(times_dict):
    clothes_by_time = dict()

    times_dict_copy = dict(times_dict)
    while times_dict_copy:
        slowest_time = max(times_dict_copy.values())
        clothes_by_time[slowest_time] = [k for k,v in times_dict_copy.items() if v == slowest_time]
        for k in clothes_by_time[slowest_time]:
            del times_dict_copy[k]
    return clothes_by_time

def find_washing_sets(incompatibility_graph, times_dict):
    # Invert the incompatibility graph into a compatibility graph
    compatibility_graph = {}
    for k in incompatibility_graph.keys():
        compatibility_graph[k] = {v for v in incompatibility_graph.keys() if (k != v and v not in incompatibility_graph[k])}

    clothes_by_time = get_clothes_by_time(times_dict)

    washing_sets = set()
    while len(compatibility_graph) > 0:
        new_washing_set = find_washing_set(compatibility_graph, clothes_by_time)
        for k in new_washing_set:
            del compatibility_graph[k]
        washing_sets.add(new_washing_set)

    return washing_sets
    

def find_washing_set(compatibility_graph, clothes_by_time):
    washing_set = set()
    for i in range(20):
        largest_maximal_cliques_by_time = {}
        for i in range(1,21):
            # Subgrafo de compatibilidad para prendas de duracion 'i', y que son compatibles con todas las ya elegidas para lavar
            comp_subgraph = {k : v for k,v in compatibility_graph.items() if (k in clothes_by_time[i] and all(k in compatibility_graph[comp] for comp in washing_set))}
            if not comp_subgraph:
                continue
            maximal_cliques = list(bron_kerbosch.bron_kerbosch(compatibility_graph, comp_subgraph.keys(), R=washing_set))
            largest_clique_size = max(len(clique) for clique in maximal_cliques)
            largest_maximal_cliques = [clique for clique in maximal_cliques if len(clique) == largest_clique_size]
            largest_maximal_cliques_by_time[i] = random.choice(largest_maximal_cliques)
            #print(largest_maximal_cliques_by_time[i])
        if not largest_maximal_cliques_by_time: continue
        largest_clique_size = max(len(clique) for time,clique in largest_maximal_cliques_by_time.items())
        largest_maximal_cliques = [clique for time,clique in largest_maximal_cliques_by_time.items() if len(clique) == largest_clique_size]
        largest_maximal_clique_chosen = random.choice(largest_maximal_cliques)
        washing_set = frozenset(largest_maximal_clique_chosen)
        
    
    return washing_set


main()