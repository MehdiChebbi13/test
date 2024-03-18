
n=int(input())
s=0   
for i in range(n):
    user_input = input()
    integer_list = user_input.split()
    integer_list = [int(i) for i in integer_list]
    if ((integer_list[0]+integer_list[1]+integer_list[2])>=2):
        s+=1
print(s)
    



