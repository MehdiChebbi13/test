t=int(input())
for f in range(t):
    n=int(input())
    k=0
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    while (k<=n):
        user_input = input()
        integer_list = user_input.split()
        integer_list = [int(i) for i in integer_list]
        for j in range(n):
            matrix[k][j]=integer_list[j]
        k=k+1
print(matrix)
                