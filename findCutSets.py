# this program aims finding all fundamental cut sets,
# when the spanning tree T in undirected graph G is given
# Python 3.6
# rongjian liu <rongjliu@foxmail.com>
# Jun/16/2018
#
# Refernece: Saxena, S. (2010). On finding fundamental cut sets. Information Processing Letters, 110(4), 168-170.
import copy
from enum import Enum

from Edge import CutSetEdge
from Matrix_G import Matrix_G


class COLOR(Enum):
    WHITE = 1,
    GRAY = 2,
    BLACK = 3


WHITE = COLOR.WHITE
GRAY = COLOR.GRAY
BLACK = COLOR.BLACK
txtName = "G.txt"


# section Algorithm in Refernece Saxena, S. (2010).
def fundmentalcutsets(G):
    N = G.numVertices  # the vertex number of graph G
    vertex = G.vertex
    edge = G.edge
    S = [[] for i in range(N)]
    for v in range(N):
        if vertex[v].parent != -1:  # vertex[v].parent!=-1 means the vertex v has a parent
            Aprev = vertex[v].pre
            Aalphv = vertex[v].alpha
            descendants = vertex[v].descendants  # list A[i,j] in paper
            for subv in range(len(descendants)):
                for u in range(len(edge[descendants[subv]])):
                    if vertex[edge[descendants[subv]][u]].pre < Aprev or vertex[
                        edge[descendants[subv]][u]].pre > Aalphv:
                        S[v].append(CutSetEdge(vertex[edge[descendants[subv]][u]].v, descendants[subv]))
        # for w in range(Aprev, Aalphv+1):
        # for u in range(len(edge[w])):
        # if vertex[edge[w][u]].pre < Aprev or vertex[edge[w][u]].pre> Aalphv:
        # S[v].append(Edge(edge[w][u],v))
    return S


def calculateFundamentalCutsets(G):
    Gmatrix = Matrix_G(G.numVertices, G.adjMatrix)

    temp = Matrix_G(G.numVertices, G.adjMatrix)
    Gmatrix.Matrix = copy.deepcopy(temp.Matrix)
    Gmatrix.writetxt()

    G.initializeGraphWithMatris(Gmatrix)
    G.preprocess()
    G.alphaprocess()
    S = fundmentalcutsets(G)
    f = open(txtName, "a+")
    f.write("\nthe fundmental cut sets are: \nbegin \nthe root vertex is " + str(G.root_vertex) + '.\n')
    for i in range(len(S)):
        SI = S[i]
        # print(type(SI))
        # str1=str(i)
        if G.vertex[i].parent == -1:
            continue
        else:
            f.write('for edge (' + str(i) + ',' + str(G.vertex[i].parent) + '), there exist(s) ' + str(
                len(SI)) + ' edge(s) need to be removed\n')
        for jj in range(len(SI)):
            f.write('(' + str(SI[jj].u) + ',' + str(SI[jj].v) + ') ')
        if G.vertex[i].parent != -1:
            f.write('\n')
    f.write('end\n')
    f.close()
