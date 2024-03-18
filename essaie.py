def possible_ebne(list):
    ch=list[1]
    while not ((ch!="")& (int(ch) in range(0,9))):
        if (int (ch(list[0]-1))%2!=0):
            for i in range (list[0]-2,0):
                ch= list[1].replace(list[1][i],"")
                if ebne_test(int(ch)):
                    return ch
    return -1    
    
        


    
    