#Python matrix transpose
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print [[row[col] for row in matrix] for col in range(len(matrix[0]))]

for col in range(len(matrix[0])):
    for row in matrix:
        print row[col]

print map(list, zip(*matrix))

# reverse list
a = [1,2,3]
a.reverse()
print a
print a[::-1]
print [i for i in reversed(a)]


#plus dist d1 and d2
d1 = {'name' : 'revotu', 'age' : 99}
d2 = {'age' : 24, 'sex' : 'male'}
# 1
d = {}
d.update(d1)
d.update(d2)
print d

# 2
d = d1.copy()
d.update(d2)
print d

# 3
d = dict(d1)
d.update(d2)
print d

# 4
d = dict(d1, **d2)
print d

# 5
d = {k:v for d in [d1, d2] for k,v in d.items()}
print d

# 6
d = dict(list(d1.items()+list(d2.items())))
print d

## 7
# d = dict(d1.items() | d2.items())
# print d
#
# # 8
# from collections import ChainMap
# d = dict(ChainMap(d1,d2))