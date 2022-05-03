#Code by David Josipovic

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)
        for i in matrix:
            if len(i) != self.width:
                print("Error: Inconsistent width")
    def toString(self):
        maxLen = 0
        for i in self.matrix:
            for j in i:
                maxLen = max(maxLen, len(str(j)))
        if self.height == 1:
            return "[ " + " ".join([str(i) + (" " * (maxLen - len(str(i)))) for i in self.matrix[0]]) + " ]"
        layers = []
        for row in range(self.height):
            if row == 0:
                layers.append("⌈ " + " ".join([str(i) + (" " * (maxLen - len(str(i)))) for i in self.matrix[row]]) + " ⌉")
            elif row == self.height-1:
                layers.append("⌊ " + " ".join([str(i) + (" " * (maxLen - len(str(i)))) for i in self.matrix[row]]) + " ⌋")
            else:
                layers.append("| " + " ".join([str(i) + (" " * (maxLen - len(str(i)))) for i in self.matrix[row]]) + " |")
        return "\n".join(layers)
    def times(self, B):
        A = self
        if A.width == B.height:
            C = []
            for i in range(A.height):    # i --> Row of C and A
                for j in range(B.width): # j --> Column of C and B
                    if i >= len(C):
                        C.append([])
                    dp = 0
                    for k in range(A.width):
                        dp += A.matrix[i][k] * B.matrix[k][j]
                    C[i].append(dp)
            return Matrix(C)
        else:
            print(f"Can't multiply {A.width}x{A.height} matrix with {B.width}x{B.height} matrix")
    def plus(self, B):
        A = self
        if (A.width == B.width) and (A.height == B.height):
            C = []
            for i in range(A.height):
                C.append([])
                for j in range(A.width):
                    C[-1].append(A.matrix[i][j] + B.matrix[i][j])
            return Matrix(C)
        else:
            print(f"Can't add {A.width}x{A.height} matrix with {B.width}x{B.height} matrix")