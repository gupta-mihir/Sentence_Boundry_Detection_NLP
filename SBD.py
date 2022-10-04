

from cgi import test
import re
from time import perf_counter
from turtle import right
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import math


#Learning how to use sklearn 
#FUNC to remove class Label and number from period word
def rm_num(word):
    counter = 0
    for x in word:
        if x.isalpha() != True and x != ' ' and x != '$' and x != '%':
            counter +=1
    new_word = word[counter:]
    return new_word

def convertToNumber (s):
    return int.from_bytes(s.encode(), 'little')

def convertFromNumber (n):
    return n.to_bytes(math.ceil(n.bit_length() / 8), 'little').decode()



with open('SBD.train.txt') as f:
    lines = f.read()
    s1 = re.sub("[!,:,?,]", "", lines)
    import re
    myex = re.compile(r"(TOK)")
    final_str = re.sub(myex, '',s1)
    init_counter = 0
    neos_counter = 0
    split_str = final_str.splitlines()
#FEATURE VECTOR features assigned
    left_per = []
    right_per = []
    len_three = []
    left_cap = []
    right_cap = []
    cl_label = []
#3 MORE Feature Vectors


    per_counter = 0
    
    for y in range(len(split_str)):
        x = split_str[y]
        if '.' in x:
            per_counter+=1
            if ' EOS' in x:
                cl_label.append('EOS')
                init_counter += 1
                l_word = x[:-4]
                #l_word = rm_label(x, 'EOS')
                new_word_l = rm_num(l_word)
                left_per.append(new_word_l)
                #Right word of period
                if y+1 < len(split_str):
                    r_count = 0
                    r_str = split_str[y+1]
                    new_word_r = rm_num(r_str)
                   # new_word_r = r_str[r_count-1:]
                    fl_r = convertToNumber(new_word_r)
                    right_per.append(fl_r)

                    if new_word_r[0] != ' ':
                        if new_word_r[0].isupper():
                            right_cap.append(1)
                        else:
                            right_cap.append(0)
                    elif new_word_r[0] == ' ' and new_word_r[1].isalpha:
                        if new_word_r[1].isupper():
                            right_cap.append(1)
                        else:
                            right_cap.append(0)
                    else:
                        right_cap.append(0)

                else:
                    right_per.append(0)
                    right_cap.append(0)

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
                #l_word = rm_label(x, 'NEOS')
                new_word_l = rm_num(l_word)
                left_per.append(new_word_l)
                #left_per.append(new_word_l)
                #right of period
                if y+1 < len(split_str):
                    r_count = 0
                    r_str = split_str[y+1]
                    new_word_r = rm_num(r_str)
                    fl_r = convertToNumber(new_word_r)
                    right_per.append(fl_r)
                    
                    if new_word_r[0] != ' ':
                        if new_word_r[0].isupper():
                            right_cap.append(1)
                        else:
                            right_cap.append(0)
                    elif new_word_r[0] == ' ' and new_word_r[1].isalpha:
                        if new_word_r[1].isupper():
                            right_cap.append(1)
                        else:
                            right_cap.append(0)
                    else:
                        right_cap.append(0)

                else:
                    right_per.append(0)
                    right_cap.append(0)

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
    
    f_vect = [[] for x in range(len(left_per))]
    for x in range(len(left_per)):
        f_in_vect = []
        f_in_vect.append(left_per[x])
        f_in_vect.append(right_per[x])
        f_in_vect.append(len_three[x])
        f_in_vect.append(left_cap[x])
        f_in_vect.append(right_cap[x])
        #f_in_vect.append(cl_label[x])
        f_vect[x] = f_in_vect

   # X = f_vect
    #Y = cl_label
    #X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)
    #clf = DecisionTreeClassifier()
    #clf = clf.fit(X_train, Y_train)
    #print(clf.get_params())






   



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
    #print(f_vect)
   # print(len(f_vect))
    print(right_per)
   # print(left_per)
    #print (right_per)
   # print(right_cap)

    #print(s1, end='')
    
#Need to make a feature vector
#Each feature vector will be 0,1 or number representation of word
#EXAMPLE: L<3 = [0,0,0,0,1,1,0,1] 
#Example: Word Left of (.) = []