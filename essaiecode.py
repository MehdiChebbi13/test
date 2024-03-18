def ebne_test(n):
    if (n%2!=0):
        ch=str(n)
        s=0
        for i in range (len(ch)):
            s+=int(ch[i])
        if (s%2==0):
            return True
    return False    
print ("enter ch")
ch=input()
n=len(ch)
while (int(ch)>0) and (int(ch)>10):
    if (int (ch[n-1])%2==0):
        
        ch=ch[0:n-1]
        n=n-1
        print("do",ch)
            # if ebne_test(int(ch)):
                # print(ch) 
                # break
    else:
        if ebne_test(int(ch)):
                print("yes",ch) 
                break
        ch=ch[0:n-2]+ch[n-1]
        n=n-1
        print("no,",ch)
            
                
print(-1)  