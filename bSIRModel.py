from igraph import *
import numpy as np

__author__ = "Rodrigo Ferreira"
__license__ = "GPLv3"
__email__ = "rodrigoferreira001@hotmail.com"


class SIRModel:

    def __init__(self, graph, beta, gamma):
        """
            Model constructor
            :param graph: An igraph graph
            :param beta: The infection rate (float value in [0,1])
            :param gamma: The recovery rate (float value in [0,1])

        """
        self.iteration = 0
        self.graph = graph
        self.beta = beta
        self.gamma = gamma
        self.status = []

        self.susceptibles = range(graph.vcount())
        self.infecteds = []
        self.recovereds = []

        self.nodes_neighbors = []
        for i in range(graph.vcount()):
            self.nodes_neighbors.append(
                {'infected_neighbors': 0,
                 'susceptible_neighbors': [int(self.graph.vs[v]['name']) for v in self.graph.neighbors(self.graph.vs.find(str(i)))]})

        # for i, e in enumerate(self.nodes_neighbors):
        #     print i,": ",e

    def reset(self):
        pass

    def iterate(self):
        """
            Infection and recovery Process
        :return: status
        """
        #infection
        #print "Numero de infectados: ", len(self.infecteds)
        for i in range(len(self.infecteds)):
            #print "Infectados: ", self.infecteds
            #print "Eu deveria percorrer:"
            neighbors = self.nodes_neighbors[self.infecteds[i]]['susceptible_neighbors'][:]
            #print neighbors

            #for neighbor in self.nodes_neighbors[self.infecteds[i]]['susceptible_neighbors']:
            for neighbor in neighbors:
                event = np.random.random_sample()
                #print "No: ", self.infecteds[i]
                #print "Vizinho: ", neighbor
                #print "Event: ", event
                #print "Conta: ", self.beta * self.nodes_neighbors[neighbor]['infected_neighbors']
                #print "Vizinhos: ", self.nodes_neighbors[neighbor]['susceptible_neighbors']

                if event < (self.beta * self.nodes_neighbors[neighbor]['infected_neighbors']):
                    self.infecteds.append(neighbor)  # erro aqui
                    self.susceptibles.remove(neighbor)
                    #print neighbor, " foi infectado"

                    for n in [int(self.graph.vs[v]['name']) for v in self.graph.neighbors(self.graph.vs.find(str(neighbor)))]:
                        self.nodes_neighbors[n]['susceptible_neighbors'].remove(neighbor)
                        self.nodes_neighbors[n]['infected_neighbors'] += 1
                #print "--------------------------"

        #recovery
        # print "\n ------------------------\n Recovery:"
        # print "Devo percorrer: "
        # print self.infecteds
        for i in reversed(range(len(self.infecteds))):
            event = np.random.random_sample()
            # print "No: ", self.infecteds[i]
            if event < self.gamma:
                # print "No ", self.infecteds[i], " foi recuperado"
                # print "Event: ", event
                # print "Gamma: ", self.gamma
                # print "---------------------"
                self.recovereds.append(self.infecteds[i])
                self.infecteds.remove(self.infecteds[i])


        self.iteration += 1
        return (len(self.susceptibles), len(self.infecteds), len(self.recovereds))

    def infect(self, infecteds):
        for node in infecteds:
            self.infecteds.append(node)

            #print "Infectado: ", node

            if node in self.recovereds:
                self.recovereds.remove(node)

                for neighbor in [int(self.graph.vs[v]['name']) for v in self.graph.neighbors(self.graph.vs.find(str(node)))]:
                    self.nodes_neighbors[neighbor]['infected_neighbors'] += 1
            else:
                self.susceptibles.remove(node)

                #print "Vizinhos de ", node, ": ", [int(v['name']) for v in self.graph.vs[node].neighbors()]

                for neighbor in [int(self.graph.vs[v]['name']) for v in self.graph.neighbors(self.graph.vs.find(str(node)))]:
                    self.nodes_neighbors[neighbor]['susceptible_neighbors'].remove(node)
                    self.nodes_neighbors[neighbor]['infected_neighbors'] += 1

    def recover(self, recovereds):
        for node in recovereds:
            self.recovereds.append(node)

            if node in self.infecteds:
                self.infecteds.remove(node)

                for neighbor in [int(self.graph.vs[v]['name']) for v in self.graph.neighbors(self.graph.vs.find(str(node)))]:
                    self.nodes_neighbors[neighbor]['infected_neighbors'] -= 1
            else:
                self.susceptibles.remove(node)

                for neighbor in [int(self.graph.vs[v]['name']) for v in self.graph.neighbors(self.graph.vs.find(str(node)))]:
                    self.nodes_neighbors[neighbor]['susceptible_neighbors'].remove(node)


