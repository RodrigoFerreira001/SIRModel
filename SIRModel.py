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

        self.susceptibles = []
        self.infecteds = []
        self.recovered = []

        self.nodes_neighbours = []
        for i in xrange(graph.vcount()):
            self.nodes_neighbours.append({'infeted_neighbours' : 0, 'susceptible_neighbours' : []})

    def reset(self):
        pass

    def iterate(self):
        pass

    def infect(self, infecteds):
        for node in infecteds:
            print node

    def recover(self):
        pass
