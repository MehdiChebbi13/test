def count(list):
    v = [0 for _ in range(7)]
    for string in list:
        v[0] += string.count('a')
        v[1] += string.count('b')
        v[2] += string.count('c')
        v[3] += string.count('d')
        v[4] += string.count('e')
        v[5] += string.count('f')
        v[6] += string.count('g')
    return v


def max(t, n, j):
    max_index = t[0][1][j]
    indx=0
    for i in range(1,n):
        if t[i][1][j]>max_index:
            max_index=t[i][1][j]
            indx=i
    return indx
n = int(input())
t = []
O = [0] * 7
for i in range(n):
    user_in = input()
    list = user_in.split()
    t.append((list, count(list)))
for j in range(n):
    alph = chr(j + 65)
    ind_alph = max(t, n, j)
    O[ind_alph] = alph
print(O)
