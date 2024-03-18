import string
import itertools

def solution(N,S):
    Letters=string.ascii_lowercase()
    sum=0
    for string in itertools.product(Letters, repeat=N):
        Power =0
        for Si in S:
            Power += string.count(Si , 0,N-1)
            sum += 2** Power 
            
    return (sum % (998244353))
    
user_input=input()
integer_list = user_input.split()
integer_list = [int(i) for i in integer_list]
N=integer_list[0]
M=integer_list[1]
S = []
for i in range(M):
  S.append(input())
x=solution(N,S)
print(x)