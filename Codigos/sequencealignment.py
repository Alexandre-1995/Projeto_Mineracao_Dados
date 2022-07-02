# -*- coding: utf-8 -*-

   
"""
Algorithm for solving sequence alignment
Input strings x,y of len(x) = m, len(y) = n and find minimum number of
edit steps and the specific steps to transform x into y.
Time Complexity: O(nm)
"""


class SequenceAlignment(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.solution = []

    delta = lambda self, x, y, i, j: 2 if x[i] != y[j] else 0

    def alignment(self):
        n = len(self.y)
        m = len(self.x)
        OPT = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(1, m + 1):
            OPT[i][0] = i

        for j in range(1, n + 1):
            OPT[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                OPT[i][j] = min(
                    OPT[i - 1][j - 1] + self.delta(self.x, self.y, i - 1, j - 1),
                    OPT[i - 1][j] + 1,
                    OPT[i][j - 1] + 1,
                )  # align, delete, insert respectively

#        self.find_solution(OPT, m, n)

#        return (OPT[m][n], self.solution[::-1])
        return (OPT[m][n])



 #    print('Minimum amount of edit steps are: ' + str(min_edit))
 #    print('And the way to do it is: ' + str(steps))