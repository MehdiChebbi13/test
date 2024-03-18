import random

def rand_numb():
    digits = list(range(10))
    random.shuffle(digits)
    return int(''.join(map(str, digits[:4])))


def test_j(x,n):
    X= str(x)
    N =str(n)
    ch=[]
    for j in range(4):
        for i in range(4):
            if X[i]==N[j]:
                if i==j:
                    ch.append("T")
                else:
                    ch.append("V")
    random.shuffle(ch)
    return ch
    
n=rand_numb()
print("The game is simple, all you have to do is to get the mystery number in 5 tries or less to be named the King of Numbers!!!")
i=0
print("enter your first guess: ")
x=int(input())
while((i<5)or(x==n)):
    print(test_j(x,n))
    print("take another guess: ")
    x=int(input())
    i+=1
if(x==n):
    if (i<2) :
        print("NO WAYYY,you're a mind reader!")
    else:
        print("You're good king but you could do better than ",i," tries")
else:
    print("You're a waste of time, the number was ",n)
    
    
    
        
