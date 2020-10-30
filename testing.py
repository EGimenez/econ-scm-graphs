

graph = [('1', '2'), ('2', '3'),('3', '4'), ('5', '1'), ('5', '3')]



def get_adj_edges(n):
	adj_edges = []
	for t in graph:
		if t[0] == n or t[1] == n:
			adj_edges.append(t)

	return adj_edges



def get_paths(p, nf):
	edges = get_adj_edges(p[-1])

	for e in edges:
		if p[-1] == e[0]:
			n = e[1]
		else:
			n = e[0]

		if n not in p:
			if e[0] == n:
				p += '<-'+n
			else:
				p += '->'+n

			get_paths(p, nf)

	return p


	print('hola')

get_paths('1', '4')

1->2->3->4
1<-5->3->4
1<-5->6<-4
