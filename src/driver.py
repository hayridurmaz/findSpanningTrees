########################################################################################################################
# File name: driver.py
# @Author: Hayri Durmaz
# @Input: graphInput.txt -> Graph Information
# @Output:
# 1) All spanning trees of a given connected graph,
# 2) All cut sets depending on these spanning trees
# References:
# [1]: Saxena, S. (2010). On finding fundamental cut sets. Information Processing Letters, 110(4), 168-170
# [2]: Sörensen, K., Janssens, G. K. (2005). An algorithm to generate all spanning trees of a graph in order of
#      increasing cost
########################################################################################################################

import bcolors as bcolors

from src.Graph import Graph
from src.findCutSets import calculateFundamentalCutsets


def parseGraphFromFile(filename):
    g = Graph()
    graphInputFile = open(filename, "r")
    allLines = graphInputFile.readlines()

    for i in range(len(allLines)):
        if i == 0:
            try:
                verticeCount = int(allLines[i])
                g = Graph(verticeCount)
                g.initAdjMatris()
            except:
                print(bcolors.ERR + "ERROR: First line as to be 1 integer representing vertice count!" + bcolors.ENDC)
                exit(1)
        else:
            try:
                attributes = allLines[i].split(",")
                g.addEdge(int(attributes[0]), int(attributes[1]), int(attributes[2]))
                # g.addEdge(int(attributes[1]), int(attributes[0]), int(attributes[2]))
            except:
                print(bcolors.ERR + "ERROR: After first line, lines should be on this format: INTEGER, INTEGER, "
                                    "INTEGER\nRepresenting: From,To,Weight" + bcolors.ENDC)
    return g


def clearText(file="OUT_ALL_CUT_SETS.txt"):
    f = open(file, "w+")
    print("")
    f.close()


if __name__ == '__main__':
    clearText("OUT_ALL_CUT_SETS.txt")
    clearText("OUT_ALL_SPANNING_TREES.txt")
    graph = parseGraphFromFile("graphInput.txt")
    graph.printGraph()
    if not graph.isConnected():
        print(bcolors.ERR + "ERROR: Given input graph is not connected graph" + bcolors.ENDC)
    graph.printAllST()

    for i in range(graph.numVertices):
        temp_graph = Graph(graph.numVertices)
        temp_graph.initializeGraph(graph)
        temp_graph.initAdjMatris()
        temp_graph.root_vertex = i
        calculateFundamentalCutsets(temp_graph)
    print(
        bcolors.OK + "OUT: All spanning trees of given graph are shown in: " + bcolors.BLUE + "OUT_ALL_SPANNING_TREES"
                                                                                              ".txt")
    print(bcolors.OK + "OUT: All cut sets of given graph are shown in: " + bcolors.BLUE + "OUT_ALL_CUT_SETS.txt")
    print(bcolors.OK + "As You can see, each connected graph of all cut sets includes at least one edge from each and "
                       "every spanning tree")
