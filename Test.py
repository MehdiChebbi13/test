def c_n_p(n,h0,a,c,q):
    heights=[0 for _ in range(n)]
    heights[0]=h0
    for i in range(1,n):
        h=((a*h0+c)%q)
        heights.append(h)
    c=n-1
    for i in range(n):
        for j in range(i+1,n,-1):
            if (heights[j]>heights[i]) :
                break
            else:
                c+=1
    return c

user_input = input()
integer_list = user_input.split()
integer_list = [int(i) for i in integer_list]
n=integer_list[0]
h0=integer_list[1]
a=integer_list[2]
c=integer_list[3]
q=integer_list[4]
count=c_n_p(n,h0,a,c,q)
print (count)
