from SIRModel import SIRModel
from igraph import *

graph = Graph.Read_Ncol('moreno_highschool.txt', directed=False)
sirmodel = SIRModel(graph, 0.1, 0.2)

# print sirmodel.beta
# print sirmodel.gamma
# for n in sirmodel.nodes_neighbors:
#     print n
#
# print "\n########################\n"
# sirmodel.infect([0,1])
#
# for n in sirmodel.nodes_neighbors:
#     print n

# print graph.vs['name']
#
# print "S: ", sirmodel.susceptibles
# print "I: ", sirmodel.infecteds
# print "R: ", sirmodel.recovereds

for n in sirmodel.nodes_neighbors:
    print n

sirmodel.recover([1,0,68,69])
sirmodel.infect([0,1])


print "\n########################\n"

for n in sirmodel.nodes_neighbors:
    print n

# print "S: ", sirmodel.susceptibles
# print "I: ", sirmodel.infecteds
# print "R: ", sirmodel.recovereds