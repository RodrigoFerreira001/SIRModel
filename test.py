from SIRModel import SIRModel
from igraph import *

graph = Graph.Read_Ncol('moreno_highschool.txt', directed=False)
#print graph.vs[0].neighbors()[6]['name']
#print graph.neighbors(0)


#new_range  = [i * i          for i in range(5)   if i % 2 == 0]
# neighbors = [int(v['name']) for v in graph.vs[0].neighbors()]
# print neighbors

# for v in graph.neighbors(graph.vs.find('19')):
#     print graph.vs[v]['name']

beta = 0.2857
gamma = 0.1428

sirmodel = SIRModel(graph, beta, gamma)

#print graph

# print sirmodel.beta
# print sirmodel.gamma
# for n in sirmodel.nodes_neighbors:
#     print n
#
# print "\n########################\n"
sirmodel.infect([0, 1])
#
# for n in sirmodel.nodes_neighbors:
#     print n

# print graph.vs['name']
#
# print "S: ", sirmodel.susceptibles
# print "I: ", sirmodel.infecteds
# print "R: ", sirmodel.recovereds

# for n in sirmodel.nodes_neighbors:
#     print n

#sirmodel.recover([1,0,68,69])
#sirmodel.infect([0])
print sirmodel.iterate()


# print "\n########################\n"
#
# for n in sirmodel.nodes_neighbors:
#     print n

print "S: ", sirmodel.susceptibles
print "I: ", sirmodel.infecteds
print "R: ", sirmodel.recovereds