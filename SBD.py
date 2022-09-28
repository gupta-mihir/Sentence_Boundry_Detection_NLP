import re
#Learning how to use sklearn 


with open('SBD.train.txt') as f:
    lines = f.read()
    s1 = re.sub("[!,:,?,]", "", lines)
    import re
    myex = re.compile(r"(TOK)")
    final_str = re.sub(myex, '',s1)
    init_counter = 0
    neos_counter = 0
    split_str = final_str.splitlines()
    for x in split_str:
        if '.' in x and ' EOS' in x:
            init_counter += 1
        if '.' in x and 'NEOS' in x:
            neos_counter += 1
   # print(final_str, end='')
    #print(split_str)
    print ('\n')
    print('Number of EOS:', init_counter - neos_counter)
    print('Number of NEOS:', neos_counter)

    #print(s1, end='')
    
