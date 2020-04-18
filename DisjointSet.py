class DisjointSet:
    def __init__(self, n):
        self.parent = []
        self.rnk = []
        self.n = n
        for i in range(n + 1):
            self.rnk.append(0)
            self.parent.append(i)

    def Find(self, u):
        if self.parent[u] == u:
            return self.parent[u]
        else:
            return self.Find(self.parent[u])

    def Union(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if x != y:
            if self.rnk[x] < self.rnk[y]:
                self.rnk[y] = self.rnk[y] + self.rnk[x]
                self.parent[x] = y
            else:
                self.rnk[x] = self.rnk[x] + self.rnk[y]
                self.parent[y] = x
