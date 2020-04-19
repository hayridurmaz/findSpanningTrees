from findCutSets import WHITE


class CutSetVertex:
    def __init__(self, v):
        self.v = v
        self.parent = -1  # When parent equal to -1, it means that vertex v have no parent. Only root vertex have no parent
        self.previsit = -1
        self.postvisit = -1
        self.pre = -1
        self.alpha = -1
        self.color = WHITE
        self.descendants = [v]  # the descendants in the spanning tree T

    def Print(self):
        print('v=', self.v, 'parent=', self.parent, 'pre=', self.pre, 'alpha=', self.alpha, 'previsit=',
              self.previsit, 'postvisit=', self.postvisit)
        print('descendants=', self.descendants)
