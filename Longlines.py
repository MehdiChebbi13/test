

def voir(t):
    s=0
    for i in range (len(t)):
        n=0
        while t[i]>t[i+1]:
            n+=1
            
            
    return s
  

  
        
user_input = input()
integer_list = user_input.split()
integer_list = [int(i) for i in integer_list]
n=integer_list[0]
t=[0 for _ in range(n)]
t[0]=(integer_list[1])
for i in range (1,n):
    t[i]=((integer_list[2]*t[i-1]+integer_list[3])%integer_list[4])
print(voir(t))

    
