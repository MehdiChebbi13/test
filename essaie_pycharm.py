def reco(ch):
    list = ch.split()
    for i in range (len(list)-1):
        if (list[i]=="the"):
            return True
    return False
def dec(s_cases):
    ch=s_cases[0]
    x=s_cases[1]
    resultat = ""
    for caractere in ch:
        if reco(ch):
            if caractere!=" ":
                nouveau_caractere = chr(((ord(caractere.lower()) - ord('a') - x) % 26) + ord('a'))
                resultat += nouveau_caractere
            else:
                resultat+=" "
        else:
            if caractere!=" ":
                nouveau_caractere = chr(((ord(caractere.lower()) - ord('a') + x) % 26) + ord('a'))
                resultat += nouveau_caractere
            else:
                resultat+=" "
    return resultat
n=int(input())
t=[]
for i in range (n):
    s_cases=[]
    s=int(input())
    ch=input()
    s_cases.append((s, ch))
    t.append(dec(s_cases))
for j in range (n):
    print(t[j])


