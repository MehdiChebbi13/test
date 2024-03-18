def ebne_test(n):
    if (n%2!=0):
        ch=str(n)
        s=0
        for i in range (len(ch)):
            s+=int(ch[i])
        if (s%2==0):
            return True
    return False    

def possible_ebne(list):
    ch=list[1]
    n=len(ch)
    while (int(ch)>0) and (int(ch)>10):
        if (int (ch[n-1])%2==0):
            ch=ch[0:n-1]
            n=n-1
        else:
            if ebne_test(int(ch)):
                return(ch) 
            ch=ch[0:n-2]+ch[n-1]
            n=n-1
    return -1 

t = int(input())
num_cases = []
for i in range(t):
    n = int(input())
    s = input()
    num_cases.append((n, s))
for i in range (t):
    if (ebne_test(int(num_cases[i][1]))):
        print(num_cases[i][1])
    else :
        p=possible_ebne(num_cases[i])
        print(p)
1
