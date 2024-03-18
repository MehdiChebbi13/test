user_input = input()
integer_list = user_input.split()
integer_list = [int(i) for i in integer_list]
n=integer_list[0]
m=integer_list[1]
rhymes=[0]*n
for i in range (n):
    lines = input()
    rhymes[i] = lines.split()
t=[]
for j in range (m):
    lin = input()
    poem = lin.split()
    t.append((poem[len(poem)-1],j))

def rhyme(rhymes,ch):
    for i in range(len(rhymes)):
        for string in rhymes[i]:
            if ch==string:
                return i
    return 'X'
def replace(t,rhymes,n):
    v=[]
    for i in range(n):
        v.append(rhyme(rhymes,t[i]))
    j=0
    for i in range(n):
        if v[i]==v[i+1]:
            t[i]
    
    
    
 
    


    
    
        
        
    