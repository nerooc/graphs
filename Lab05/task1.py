from lab05 import *
import argparse

def parserFunction():
	parser = argparse.ArgumentParser(description='')
	parser.add_argument('-l', '--layers', type=int, help=u'''Number of layers''',
		required=True)
	parser.add_argument('-vn', '--vertices_numbers', nargs='+', type=int, 
		help=u'''Number of vertices in each layer''', )

	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = parserFunction()

	try:
		if args.vertices_numbers:
			G, pos = generate_flow_net(args.layers, args.vertices_numbers) 
		else:
			G, pos = generate_flow_net(args.layers) 
		adj_matrix = get_adjacency_matrix_of_flow_net(G, save_to_file=True)
		print("\n----ADJACENCY MATRIX OF YOUR FLOW NET:----\n")
		pretty_print(adj_matrix)
		display_flow_net(G, pos)
	except Exception as e:
		print(e)
		exit(-1)
