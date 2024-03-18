def count_letters(list):
    v=[0]*7
    for string in list:
        v[0] += string.count('a')
        v[1] += string.count('b')
        v[2] += string.count('c')
        v[3] += string.count('d')
        v[4] += string.count('e')
        v[5] += string.count('f')
        v[6] += string.count('g')
    return v

def get_recipe(letter_count):
    max_count = max(letter_count)
    return chr(ord('A') + letter_count.index(max_count))
def max(t,n,j):
    max_index=0
    for i in range (n-2):
        if t[i+1][1][j]>t[max_index][1][j]:
            max_index=i
    return max_index

n = int(input())
recipes = []

for _ in range(n):
    user_input = input()
    letter_count = count_letters(user_input)
    recipes.append(get_recipe(letter_count))

for recipe in recipes:
    print(recipe)