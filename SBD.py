import re
#Learning how to use sklearn 


with open('SBD.train.txt') as f:
    lines = f.read()
    s1 = re.sub("[!,:,?,]", "", lines)
    import re
    myex = re.compile(r"(TOK)")
    final_str = re.sub(myex, '',s1)
    print(final_str, end='')
    #print(s1, end='')
    
