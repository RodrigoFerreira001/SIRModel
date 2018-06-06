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

        self.susceptibles = range(graph.vcount())
        self.infecteds = []
        self.recovereds = []

        self.nodes_neighbors = []
        for i in xrange(graph.vcount()):
            self.nodes_neighbors.append({'infected_neighbors': 0, 'susceptible_neighbors': self.graph.neighbors(i)})

    def reset(self):
        pass

    def iterate(self):
        pass

    def infect(self, infecteds):
        for node in infecteds:
            self.infecteds.append(node)

            if node in self.recovereds:
                self.recovereds.remove(node)

                for neighbor in self.graph.neighbors(node):
                    self.nodes_neighbors[neighbor]['infected_neighbors'] += 1
            else:
                self.susceptibles.remove(node)

                for neighbor in self.graph.neighbors(node):
                    self.nodes_neighbors[neighbor]['susceptible_neighbors'].remove(node)
                    self.nodes_neighbors[neighbor]['infected_neighbors'] += 1

    def recover(self, recovereds):
        for node in recovereds:
            self.recovereds.append(node)

            if node in self.infecteds:
                self.infecteds.remove(node)

                for neighbor in self.graph.neighbors(node):
                    self.nodes_neighbors[neighbor]['infected_neighbors'] -= 1
            else:
                self.susceptibles.remove(node)

                for neighbor in self.graph.neighbors(node):
                    self.nodes_neighbors[neighbor]['susceptible_neighbors'].remove(node)


