class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


class CutSetEdge:
    def __init__(self, u=-1, v=-1):
        self.u = u
        self.v = v
        self.u2 = v
        self.v2 = u

    def Print(self):
        print('u=', self.u, 'v=', self.v, 'u2=', self.u2, 'v2=', self.v2)
