library(igraph)

g <- make_ring(10)
rlt01 = all_simple_paths(g, 1, 5)

rlt02 = all_simple_paths(g, 1, c(3, 5))

print(rlt01)

print('')