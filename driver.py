import bcolors as bcolors

from Graph import Graph
from findCutSets import calculateFundamentalCutsets


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


if __name__ == '__main__':
    graph = parseGraphFromFile("graphInput.txt")
    graph.printGraph()
    if not graph.isConnected():
        print(bcolors.ERR + "ERROR: Given input graph is not connected graph" + bcolors.ENDC)
    graph.printAllST()
    calculateFundamentalCutsets(graph)
