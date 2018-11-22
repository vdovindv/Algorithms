#Uses python3

import sys

def lcs2(s, t):
    m = len(s)
    n = len(t)
    matrix = [[None]*(n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif s[i - 1] == t[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[m][n]


input = sys.stdin.read()
data = list(map(int, input.split()))

n = data[0]
a = str(data[1])
m = data[2]
b = str(data[3])

print(lcs2(a, b))
