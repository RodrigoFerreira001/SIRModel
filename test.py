from SIRModel import SIRModel
from igraph import *

g = Graph.Full(10)
sirmodel = SIRModel(g, 0.1, 0.2)

# print sirmodel.beta
# print sirmodel.gamma
# print sirmodel.nodes_neighbours

print g

sirmodel.infect([0,1])