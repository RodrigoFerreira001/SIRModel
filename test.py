from SIRModel import SIRModel
from igraph import *
from matplotlib import pyplot as plt
import networkx as nx
import numpy as np
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics.SIRModel as sir

graph = Graph.Read_Ncol('email_enron.txt', directed=False)
# graph = nx.read_edgelist('email_enron.txt', nodetype = int)
#print graph.vs[0].neighbors()[6]['name']
#print graph.neighbors(0)

print graph.summary()

beta = 0.2857
gamma = 0.1428


# model = sir.SIRModel(graph)
sirmodel = SIRModel(graph, beta, gamma)

# # Model Configuration
# cfg = mc.Configuration()
# cfg.add_model_parameter('beta', beta)
# cfg.add_model_parameter('gamma', gamma)
#
# # cfg.add_model_parameter("percentage_infected", percentage_infected)
# cfg.add_model_initial_configuration("Infected", [0,51, 100, 500, 4000, 131])
# # set initial status for the model
# model.set_initial_status(cfg)


#new_range  = [i * i          for i in range(5)   if i % 2 == 0]
# neighbors = [int(v['name']) for v in graph.vs[0].neighbors()]
# print neighbors

# for v in graph.neighbors(graph.vs.find('19')):
#     print graph.vs[v]['name']


# print graph

# print sirmodel.beta
# print sirmodel.gamma
# for n in sirmodel.nodes_neighbors:
#     print n
#
# print "\n########################\n"
#sirmodel.infect([0, 51])
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

# sirmodel.recover([1,0,68,69])
sirmodel.infect([0,51, 100, 500, 4000, 131])

S = []
I = []
R = []

for i in range(50):
    #iteration = model.iteration()
    iteration = sirmodel.iterate()

    print iteration

    # S.append(iteration['node_count'][0])
    # I.append(iteration['node_count'][1])
    # R.append(iteration['node_count'][2])
    S.append(iteration[0])
    I.append(iteration[1])
    R.append(iteration[2])


plt.plot(range(len(S)), S, 'g-')
plt.plot(range(len(I)), I, 'r-')
plt.plot(range(len(R)), R, 'b-')
plt.axis([0, 50, 0, 36692])
plt.xlabel('Geracoes')
plt.ylabel('Individuos Infectados')
plt.title('GASIR - Genetic Algorithm for SIR Model - Melhor Caso')
plt.show()

# print "\n########################\n"
#
# for n in sirmodel.nodes_neighbors:
#     print n

# print "S: ", sirmodel.susceptibles
# print "I: ", sirmodel.infecteds
# print "R: ", sirmodel.recovereds