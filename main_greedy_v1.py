import utils
import networkx as nx

def main():
    incompatibility_graph, times_dict = utils.load_incompatibility_graph_and_times_dict()
    top_result = utils.evaluate_result(times_dict, "best_time.txt")
    washing_sets = find_washing_sets(incompatibility_graph, times_dict)
    utils.generate_output_coloring(washing_sets)
    result = utils.evaluate_result(times_dict)
    if result < top_result:
        utils.keep_best_result()
        top_result = result
    print(f"Time: {result}")
    print(f"Best Time: {top_result}")
    
    

def find_washing_sets(incompatibility_graph, times_dict):
    G = nx.Graph()

    for k, vs in incompatibility_graph.items():
        for v in vs:
            if v in incompatibility_graph.keys(): G.add_edge(k,v)

    result = nx.coloring.greedy_color(G, strategy="smallest_last", interchange=True)

    distinct_values = {v for v in result.values()}
    print(len(distinct_values))

    return result
    
main()