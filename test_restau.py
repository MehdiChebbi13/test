import random
x=1740
n=4670
X= str(x)
N=str(n)
print(X)
print(N)
ch=[]
for j in range(4):
    for i in range(4):
        if X[i]==N[j]:
            if i==j:
                print(i)
                ch.append("T")
            else:
                ch.append("V")
random.shuffle(ch)
print(ch)