def change(w,looser):
    c=looser[0]
    w.pop(0)
    w.append(c)
    looser.pop(0)
    
    
def winner(p1,p2,asc):
    if asc.index(p1)>asc.index(p2):
        return 1
    elif asc.index(p1)<asc.index(p2) :
        return 2
    else:
        return 3


n=int(input())
asc=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
t=[0]*n
for k in range(n):
    user_in = input()
    ch1 = user_in.split()
    user_i = input()
    ch2 = user_i.split()
    while (len(ch1)>0 and len(ch2)>0)or(ch1==ch2):
        w=winner(ch1[0],ch2[0],asc)
        if w==1:
            change(ch1,ch2)
        elif w==2:
            change(ch2,ch1)
        else :
            x=ch1[0]
            ch1.pop(0)
            ch2.pop(0)
            ch1.append(x)
            ch2.append(x)
            
            
    if len(ch1)>len(ch2):
        t[k]=1
    elif len(ch1)<len(ch2):
        t[k]=2
    else:
        t[k]=3
for i in range(n):
    if t[i]==1:
        print("player 1")
    elif t[i]==2:
        print("player 2")
    else:
        print("draw")
    
