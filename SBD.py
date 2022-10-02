
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
    left_per = []
    right_per = []
    len_three = []
    left_cap = []
    right_cap = []
    cl_label = []
    
    for y in range(len(split_str)):
        x = split_str[y]
        if '.' in x:
            if ' EOS' in x:
                cl_label.append('EOS')
                init_counter += 1
                l_word = x[:-4]
                num_counter = 0
                for a in x:
                    if a.isalpha() != True:
                        num_counter += 1
                new_word_l = l_word[num_counter-2:]
                left_per.append(new_word_l)
                #LEFT WORD LESS THAN 3 CHARS
                if len(new_word_l) < 3:
                    len_three.append(1)
                else:
                    len_three.append(0)
                # LEFT UPPERCASE FEATURE VECTOR
                if new_word_l[0].isupper():
                    left_cap.append(1)
                else:
                    left_cap.append(0)

            elif 'NEOS' in x:
                cl_label.append('NEOS')
                neos_counter += 1
                l_word = x[:-5]
                num_counter = 0
                for a in x:
                    if a.isalpha() != True:
                        num_counter += 1
                new_word_l = l_word[num_counter-2:]
                left_per.append(new_word_l)
                #LEFT WORD LESS THAN 3 CHARS
                if len(new_word_l) < 3:
                    len_three.append(1)
                else:
                    len_three.append(0)
                # LEFT UPPERCASE FEATURE VECTOR
                if new_word_l[0].isupper():
                    left_cap.append(1)
                else:
                    left_cap.append(0)


   # print(final_str, end='')
    #print(split_str)
    print ('\n')
    print('Number of EOS:', init_counter - neos_counter)
    print('Number of NEOS:', neos_counter)
    print(cl_label)

    #print(s1, end='')
    
#Need to make a feature vector
#Each feature vector will be 0,1 or number representation of word
#EXAMPLE: L<3 = [0,0,0,0,1,1,0,1] 
#Example: Word Left of (.) = []