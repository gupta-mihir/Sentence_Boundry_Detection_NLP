
import re
from time import perf_counter

#Learning how to use sklearn 
#FUNC to remove class Label and number from period word
def rm_num(word):
    counter = 0
    for x in word:
        if x.isalpha() != True and x != ' ':
            counter +=1
    new_word = word[counter:]
    return new_word

def rm_label(word, label):
    if ' EOS' in word:
        new_word = word[:-4]
    else:
        new_word = word[:-5]


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
    per_counter = 0
    
    for y in range(len(split_str)):
        x = split_str[y]
        if '.' in x:
            per_counter+=1
            if ' EOS' in x:
                cl_label.append('EOS')
                init_counter += 1
                l_word = x[:-4]
                num_counter = 0
                #for a in x:
                 #   if a.isalpha() != True:
                  #      num_counter += 1
                #new_word_l = l_word[num_counter-2:]
                new_word_l = rm_num(l_word)
                left_per.append(new_word_l)
                #Right word of period
                if y+1 < len(split_str):
                    r_count = 0
                    r_str = split_str[y+1]
                    for a in r_str:
                        if a.isalpha() != True:
                            r_count += 1
                    new_word_r = r_str[r_count-2:]
                    right_per.append(new_word_r)
                else:
                    right_per.append(0)

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
              #  for a in x:
                #    if a.isalpha() != True:
                 #       num_counter += 1
               # new_word_l = l_word[num_counter-2:]
                new_word_l = rm_num(l_word)
                left_per.append(new_word_l)
                left_per.append(new_word_l)
                #right of period
                if y+1 < len(split_str):
                    r_count = 0
                    r_str = split_str[y+1]
                    for a in r_str:
                        if a.isalpha() != True:
                            r_count += 1
                    new_word_r = r_str[r_count-2:]
                    right_per.append(new_word_r)
                else:
                    right_per.append(0)

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
    print('Length of Left Per:', len(left_per))
    print('Length of Right Per:', len(right_per))
    print('Length of < 3:', len(len_three))
    print('Length of Left Cap:', len(left_cap))
    print('Length of Class:', len(cl_label))
    print('Number of Per Counter:', per_counter)
    print(left_per)

    #print(s1, end='')
    
#Need to make a feature vector
#Each feature vector will be 0,1 or number representation of word
#EXAMPLE: L<3 = [0,0,0,0,1,1,0,1] 
#Example: Word Left of (.) = []