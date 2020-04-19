class Matrix_G:
    def __init__(self, N=1, matrix=[]):
        self.N = N
        self.Matrix = matrix

    def Print(self):
        print('   ', [i for i in range(self.N)])
        for i in range(self.N):
            print(i, ':', self.Matrix[i])
        return 1

    def writetxt(self, txtName="OUT_ALL_CUT_SETS.txt"):
        f = open(txtName, "a+")
        str11 = ''.join('%s' % self.N)
        f.write("\nadjacent matrix is " + str11 + "*" + str11 + "\nbegin:\n")
        for i in range(self.N):
            str1 = ",".join('%s' % id for id in self.Matrix[i])
            f.write(str1)
            f.write('\n')
        f.write('end\n')
        f.close()
        return 1
