from scipy.stats import wilcoxon


A = """
1
2
2
1
1
3
1
2
1
1
2
1
1
2
2
1
1
2
2
3
1
3
1
1
1
2
2
2
1
3
1
2
3
2
1
1
1
1
3
1
1
2
2
3
3
2
1
1
1
1
1
1
1
2
2
2
1
1
1
2
2
1
2
1
2
1
2
3
4
1
3
3
1
2
2
2
2
3
2
1
2
2
2
2
1
1
2
1
2
2
2
3
1
2
3
3
1
3
1
2
1
2
1
2
2
1
2
2
3
1
1
1
1
3
2
3
1
2
1
1
"""
B = """
1
2
2
2
1
3
1
2
3
2
1
1
1
1
3
1
1
2
2
3
3
2
1
1
1
2
2
2
2
4
2
2
2
1
1
2
4
1
1
1
3
4
2
3
5
2
3
2
3
3
4
3
4
5
4
4
4
3
3
2
3
5
4
1
4
5
2
3
5
1
4
4
2
4
2
3
2
4
3
3
3
2
3
2
3
2
3
1
2
4
2
4
4
3
4
5
2
4
3
4
4
4
3
4
4
2
4
3
3
1
2
1
4
3
2
4
3
2
4
4
"""


A = [int(a.strip()) for a in A.split("\n") if len(a)>0]
B = [int(a.strip()) for a in B.split("\n") if len(a)>0]

A = [1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 3, 1, 3, 1, 1, 1, 2, 2, 2, 1, 3, 1, 2, 3, 2, 1, 1, 1, 1, 3, 1, 1, 2, 2, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 3, 4, 1, 3, 3, 1, 2, 2, 2, 2, 3, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 3, 1, 2, 3, 3, 1, 3, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 3, 1, 1, 1, 1, 3, 2, 3, 1, 2, 1, 1]
B = [1, 2, 2, 2, 1, 3, 1, 2, 3, 2, 1, 1, 1, 1, 3, 1, 1, 2, 2, 3, 3, 2, 1, 1, 1, 2, 2, 2, 2, 4, 2, 2, 2, 1, 1, 2, 4, 1, 1, 1, 3, 4, 2, 3, 5, 2, 3, 2, 3, 3, 4, 3, 4, 5, 4, 4, 4, 3, 3, 2, 3, 5, 4, 1, 4, 5, 2, 3, 5, 1, 4, 4, 2, 4, 2, 3, 2, 4, 3, 3, 3, 2, 3, 2, 3, 2, 3, 1, 2, 4, 2, 4, 4, 3, 4, 5, 2, 4, 3, 4, 4, 4, 3, 4, 4, 2, 4, 3, 3, 1, 2, 1, 4, 3, 2, 4, 3, 2, 4, 4]

print(sum(A)/len(A))
print(sum(B)/len(B))

w, p = wilcoxon(A, B)
print(p)