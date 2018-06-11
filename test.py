from SIRModel2 import SIRModel
from igraph import *

beta = 0.2857
gamma = 0.1428

graph = Graph.Read_Ncol(sys.argv[1])
graph.to_undirected(mode="collapse", combine_edges=None)

sirmodel = SIRModel(graph, beta, gamma)
sirmodel.infect([0])
#sirmodel.recover([0])


for status in  sirmodel.nodes_status:
    print status

print "(S: ", sirmodel.scount , ") (I: ", sirmodel.icount, ") (R: ", sirmodel.rcount, ")"