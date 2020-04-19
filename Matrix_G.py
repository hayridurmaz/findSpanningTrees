class Matrix_G:
    def __init__(self, N=1, matrix=[]):
        self.N = N
        self.Matrix = matrix

    def Print(self):
        print('   ', [i for i in range(self.N)])
        for i in range(self.N):
            print(i, ':', self.Matrix[i])
        return 1

    def Print2(self):

        a = []
        for i in range(self.N):
            state = 0
            for j in range(self.N):
                if self.Matrix[j][i] > 0:
                    state = 1
                    break
            a.append(state)
        num = 0
        for i in range(len(a)):
            if a[i] > 0:
                num = num + 1
        print('num=', num, a)

    # def product(self):  # produce the random adjacent matrix for graph G
    #     for i in range(self.N):
    #         for j in range(i + 1, self.N):

    def writetxt(self, txtName="G.txt"):
        f = open(txtName, "a+")
        # localtime = str(time.time())
        # f.write(localtime)
        str11 = ''.join('%s' % self.N)
        f.write("\nadjacent matrix is " + str11 + "*" + str11 + "\nbegin:\n")
        for i in range(self.N):
            str1 = ",".join('%s' % id for id in self.Matrix[i])
            f.write(str1)
            f.write('\n')
        f.write('end\n')
        f.close()
        return 1

    def Ifconnected(self):
        label = [0 for i in range(self.N)]
        root = 0
        F = []
        label[root] = 1
        for i in range(self.N):
            if self.Matrix[root][i] == 1:
                label[i] = 1
                F.append(i)
        while (len(F) > 0):
            e = F.pop(0)
            for i in range(self.N):
                if self.Matrix[e][i] > 0:
                    if label[i] == 0:
                        label[i] = 1
                        F.append(i)
        for i in range(self.N):
            if label[i] == 0:
                return 0
        return 1
