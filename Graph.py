import copy
from heapq import *

from CutSetVertex import CutSetVertex
from DisjointSet import DisjointSet
from Edge import Edge
from Matrix_G import Matrix_G
from findCutSets import COLOR

WHITE = COLOR.WHITE
GRAY = COLOR.GRAY
BLACK = COLOR.BLACK


class Graph:
    def __init__(self, V=0):
        self.numVertices = V
        self.edges = []
        self.adjMatrix = []
        self.original_edges = []
        self.MST = []
        self.MST_weight = 0
        self.root_vertex = 0  # default root is vertex 0
        self.matrix = [[] for i in range(V)]
        self.Matrix = Matrix_G()
        self.edge = [[] for i in range(V)]
        self.vertex = []  # append(Vertex(i))
        self.t1 = 0  # label for previsit postvisit in vertex
        self.t2 = 0  # label for pre in vertex

    def initializeGraph(self, graph):
        self.numVertices = 0
        self.edges = []
        self.original_edges = []
        self.MST = []
        self.MST_weight = 0
        self.numVertices = graph.numVertices
        self.edges[:] = graph.edges
        self.adjMatrix[:] = graph.adjMatrix
        self.original_edges[:] = graph.original_edges

    def initAdjMatris(self):
        for i in range(self.numVertices):
            self.adjMatrix.append([0 for i in range(self.numVertices)])

    def initializeGraphWithMatris(self, M=Matrix_G()):
        self.matrix = copy.deepcopy(M.Matrix)
        self.Matrix = copy.deepcopy(M)
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if self.matrix[i][j] != 0:
                    self.edge[i].append(j)
        for i in range(self.numVertices):
            self.vertex.append(CutSetVertex(i))

    def Print(self):
        print("adjacent matrix:")
        self.Matrix.Print()
        print('vertex:')
        for i in range(self.N):
            self.vertex[i].Print()
        print('edge:')
        for i in range(self.N):
            print(i, ":", self.edge[i])

    def printGraph(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val), end=" ")
            print("")

    # recursive callable, sub-program for preprocess
    def subpreprocess(self, F):
        # print('line145=',F)
        for i in range(len(F)):
            e = F[i]
            FF = []
            self.vertex[e].previsit = self.t1
            self.t1 = self.t1 + 1
            self.vertex[e].pre = self.t2
            self.t2 = self.t2 + 1
            self.vertex[e].color = BLACK
            for i in range(len(self.edge[e])):
                if self.vertex[self.edge[e][i]].color == WHITE and self.vertex[self.edge[e][i]].parent == -1:
                    FF.append(self.edge[e][i])
                    self.vertex[self.edge[e][i]].parent = e
            for i in range(len(FF)):
                self.vertex[e].descendants.append(FF[i])  # the descendants of vertex e
            self.subpreprocess(FF)  # the spanning tree is embedded in this function
            self.vertex[e].postvisit = self.t1
            self.t1 = self.t1 + 1

    # label every vertex in graph, previsit time and postvisit time for every vertex in tree T
    def preprocess(self):

        F = []
        # F.append(self.root_vertex)
        self.vertex[self.root_vertex].previsit = self.t1
        self.t1 = self.t1 + 1
        self.vertex[self.root_vertex].pre = self.t2
        self.t2 = self.t2 + 1
        self.vertex[self.root_vertex].color = BLACK
        for i in range(len(self.edge[self.root_vertex])):
            if self.vertex[self.edge[self.root_vertex][i]].color == WHITE:
                F.append(self.edge[self.root_vertex][i])
                self.vertex[self.edge[self.root_vertex][i]].parent = self.root_vertex
        for i in range(len(F)):
            self.vertex[self.root_vertex].descendants.append(F[i])  # the descendants of root vertex
        self.subpreprocess(F)
        self.vertex[self.root_vertex].postvisit = self.t1

    def alphaprocess(self):  # produce \alpha(v) in Refernece Saxena, S. (2010).
        for i in range(self.numVertices):
            self.vertex[i].alpha = int((self.vertex[i].postvisit - self.vertex[i].previsit - 1) / 2) + self.vertex[
                i].pre

    def __lt__(self, other):
        return self.MST_weight < other.MST_weight

    def addEdge(self, u, v, weight=1):
        self.edges.append(Edge(u, v, weight))
        self.original_edges.append(Edge(u, v, weight))
        self.adjMatrix[u][v] = 1
        self.adjMatrix[v][u] = 1

    def kruskalMST(self):
        self.MST_weight = 0
        sumOfWeights = 0
        self.edges.sort(key=lambda x: x.w, reverse=False)
        ds = DisjointSet(self.numVertices)
        for e in self.edges:
            u = e.u
            v = e.v
            set_of_u = ds.Find(u)
            set_of_v = ds.Find(v)
            if set_of_u != set_of_v:
                w = e.w
                self.MST.append(Edge(u, v, w))
                sumOfWeights += w
                ds.Union(set_of_u, set_of_v)

        for mst_edge in self.MST:
            for original_edge in self.original_edges:
                if original_edge.u == mst_edge.u and original_edge.v == mst_edge.v:
                    self.MST_weight = self.MST_weight + original_edge.w
                    # mst_edge.w = original_edge.w
                    break

        return sumOfWeights

    def containsCycle(self, visited_list):
        for e in self.edges:
            if visited_list[e.u] and visited_list[e.v]:
                return True
            visited_list[e.u] = True
            visited_list[e.v] = True
        return False

    def isConnected(self):
        visited_list = [False] * self.numVertices
        for e in self.edges:
            visited_list[e.u] = True
            visited_list[e.v] = True
        for i in range(self.numVertices):
            if not visited_list[i]:
                return False
        return True

    def printMST(self):
        for e in self.MST:
            print(str(e.u) + " -> " + str(e.v) + " (w:" + str(e.w) + ")")

    def modifyWeight(self, edge, weight):
        for e in self.edges:
            if e.u == edge.u and e.v == edge.v:
                e.w = weight
                break

    def printAllST(self):
        partitions = []
        counter = 0
        weight = self.kruskalMST()
        heappush(partitions, self)
        while len(partitions) > 0:
            smallest = heappop(partitions)
            print(counter)
            counter += 1
            smallest.printMST()
            print("Weight of MST is: " + str(smallest.MST_weight))
            print()
            i = 0
            for e in smallest.MST:
                if e.w == 0:
                    i = i + 1
                else:
                    break
            for j in range(0, smallest.numVertices - 1 - i):
                part = Graph()
                part.initializeGraph(smallest)

                for z in range(i, i + j):
                    for parts_edge in part.edges:
                        if smallest.MST[z].u == parts_edge.u and smallest.MST[z].v == parts_edge.v:
                            part.modifyWeight(parts_edge, 0)
                            break

                for z in range(0, len(part.edges)):
                    if smallest.MST[(i + j)].u == part.edges[z].u and smallest.MST[(i + j)].v == part.edges[z].v:
                        part.edges = remove(part.edges, z)
                        break

                if part.isConnected():
                    part.kruskalMST()
                    if len(part.MST) < part.numVertices - 1:
                        continue
                    heappush(partitions, part)
                else:
                    continue


def remove(arr, i):
    # slicing till ith character
    a = arr[: i]
    # slicing from i+1th index
    b = arr[i + 1:]
    return a + b
