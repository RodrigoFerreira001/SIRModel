# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics.SIRModel as sir
import sys
import time

start = time.clock()

graph = nx.read_edgelist(sys.argv[1], nodetype = int)

beta = 0.2857
gamma = 0.1428


model = sir.SIRModel(graph)

# Model Configuration
cfg = mc.Configuration()
cfg.add_model_parameter('beta', beta)
cfg.add_model_parameter('gamma', gamma)

# cfg.add_model_parameter("percentage_infected", percentage_infected)
cfg.add_model_initial_configuration("Infected", [0,51])
# set initial status for the model
model.set_initial_status(cfg)

S = []
I = []
R = []

for i in range(50):
    print "Iteração: ", i

    iteration = model.iteration()

    S.append(iteration['node_count'][0])
    I.append(iteration['node_count'][1])
    R.append(iteration['node_count'][2])

end = time.clock()

plt.plot(range(len(S)), S, 'g-')
plt.plot(range(len(I)), I, 'r-')
plt.plot(range(len(R)), R, 'b-')
plt.axis([0, 50, 0, graph.number_of_nodes()])
plt.xlabel('Geracoes')
plt.ylabel('Individuos Infectados')
plt.title('GASIR - Genetic Algorithm for SIR Model - Melhor Caso')

print "Tempo decorrido: ", (end - start)

#plt.show()
plt.savefig(sys.argv[1].split(".")[0] + "_ndlib.png")
