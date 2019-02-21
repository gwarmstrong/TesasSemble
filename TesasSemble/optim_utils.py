import copy
import random
import graph 

# TODO implement graph sampling techniques

def i_sample_edges(Graph, i):
	edge_list = [edge for edge in Graph.edges if edge.data['color'] == 'red']
	random.shuffle(edge_list)
	sampled_edges = edge_list[:i]
	H = graph.RedBlueDiGraph()
	H.add_edges_from(sampled_edges)
	return H
