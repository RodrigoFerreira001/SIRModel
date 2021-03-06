# -*- coding: utf-8 -*-

from SIRModel import SIRModel
from igraph import *
from matplotlib import pyplot as plt
import sys
import time

start = time.clock()

graph = Graph.Read_Ncol(sys.argv[1])
graph.to_undirected(mode="collapse", combine_edges=None)

beta = 0.2857
gamma = 0.1428

sirmodel = SIRModel(graph, beta, gamma)
sirmodel.infect([0,51])

S = []
I = []
R = []

for i in range(50):
    # print "Iteração: ", i

    iteration = sirmodel.iterate()

    S.append(iteration[0])
    I.append(iteration[1])
    R.append(iteration[2])

end = time.clock()

plt.plot(range(len(S)), S, 'g-')
plt.plot(range(len(I)), I, 'r-')
plt.plot(range(len(R)), R, 'b-')
plt.axis([0, 50, 0, graph.vcount()])

plt.xlabel('Geracoes')
plt.ylabel('Individuos Infectados')
plt.title('GASIR - Genetic Algorithm for SIR Model - Melhor Caso')

print str((end - start))

# plt.show()
plt.savefig(sys.argv[1].split(".")[0] + "_rlib.png")

with open(sys.argv[1].split(".")[0] + "_rlib_result", 'a') as file:
    file.write(str((end - start)) + '\n')