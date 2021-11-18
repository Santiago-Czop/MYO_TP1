import utils
import networkx as nx

def main():
    incompatibility_graph, times_dict = utils.load_incompatibility_graph_and_times_dict()
    top_result = utils.evaluate_result(times_dict, "best_time.txt")
    washing_sets = find_washing_sets(incompatibility_graph, times_dict)
    generate_output(washing_sets)
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

    result = nx.coloring.greedy_color(G)

    print(result)
    distinct_values = {v for v in result.values()}
    print(len(distinct_values))

    return result
    
def generate_output(washing_sets):
    with open("output.txt", "w") as output_file:
        for k,v in washing_sets.items():
            output_file.write(f"{k} {v+1}\n")

main()