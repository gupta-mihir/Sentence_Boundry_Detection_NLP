

import re
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import math
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import sys


#Learning how to use sklearn 
#FUNC to remove class Label and number from period word
def rm_num(word):
    counter = 0
    for x in word:
        if x.isalpha() != True and x != ' ' and x != '$' and x != '%':
            counter +=1
    new_word = word[counter:]
    return new_word

train_data_filename = sys.argv[1]
test_data_filename = sys.argv[2]

with open(train_data_filename) as f:
    lines = f.read()
    s1 = re.sub('[!,:,?,]', "", lines)
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
    second_left = [] #word before the Word Left of Period 
    small_second_right = [] # Length of the 2nd right word
    second_right = [] #word after the Word Right of Period

    per_counter = 0
    
    for i in range(len(split_str)):
        x = split_str[i]
        if '.' in x:
            per_counter+=1
            if ' EOS' in x:
                cl_label.append('EOS')

                #LEFT WORD OF PERIOD
                init_counter += 1
                l_word = x[:-4]
                new_word_l = rm_num(l_word)
                left_per.append(hash(new_word_l))

                #SECOND LEFT WORD OF PERIOD
                if i != 0:
                    l_count = 0
                    sl_str = split_str[i-1]
                    word_l = rm_num(sl_str)
                    second_left.append(hash(word_l))
                else:
                    second_left.append(0)

                #RIGHT WORD OF PERIOD
                if i+1 < len(split_str):
                    r_count = 0
                    r_str = split_str[i+1]
                    new_word_r = rm_num(r_str)
                    right_per.append(hash(new_word_r))

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
                #SECOND WORD AFTER RIGHT OF PERIOD
                if i+2 < len(split_str):
                    r_count = 0
                    r_str = split_str[i+2]
                    new_word_r = rm_num(r_str)
                    second_right.append(hash(new_word_r))
                    if len(new_word_r) < 4:
                        small_second_right.append(1.0)
                    else:
                        small_second_right.append(0.0)
                else:
                    second_right.append(0)
                    small_second_right.append(0.0)
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
                
                #LEFT WORD OF PERIOD
                l_word = x[:-5]
                new_word_l = rm_num(l_word)
                left_per.append(hash(new_word_l))

                #SECOND WORD LEFT OF PERIOD
                if i != 0:
                    l_count = 0
                    sl_str = split_str[i-1]
                    word_l = rm_num(sl_str)
                    second_left.append(hash(word_l))
                else:
                    second_left.append(0)
                #RIGHT WORD OF PERIOD
                if i+1 < len(split_str):
                    r_count = 0
                    r_str = split_str[i+1]
                    new_word_r = rm_num(r_str)
                    right_per.append(hash(new_word_r))
                    
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
                
                #SECOND WORD RIGHT OF PERIOD
                if i+2 < len(split_str):
                    r_count = 0
                    r_str = split_str[i+2]
                    new_word_r = rm_num(r_str)
                    second_right.append(hash(new_word_r))
                    if len(new_word_r) < 4:
                        small_second_right.append(1.0)
                    else:
                        small_second_right.append(0.0)
                else:
                    second_right.append(0)
                    small_second_right.append(0.0)
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


    #print(small_second_right)

    #lb = LabelEncoder()
    #fl_right_per = lb.fit_transform(right_per)
    #fl_left_per = lb.fit_transform(left_per)
    #sec_fl_left = lb.fit_transform(second_left)
    #sec_fl_right = lb.fit_transform(second_right)
        
    f_vect = [[] for x in range(len(left_per))]
    for x in range(len(left_per)):
        f_in_vect = []
        f_in_vect.append(left_per[x])
        f_in_vect.append(right_per[x])
        f_in_vect.append(len_three[x])
        f_in_vect.append(left_cap[x])
        f_in_vect.append(right_cap[x])
        f_in_vect.append(second_left[x])
        f_in_vect.append(second_right[x])
        f_in_vect.append(small_second_right[x])
        
        
        f_vect[x] = f_in_vect
    


#?????????????????????????????????????????????
#/////////////////////////////////////////////
with open(test_data_filename) as f_test:
    lines_test = f_test.read()
    s1_test = re.sub('[!,:,?,]', "", lines)
    myex_test = re.compile(r"(TOK)")
    final_str_test = re.sub(myex, '',s1)
    init_counter_test = 0
    neos_counter_test = 0
    split_str_test = final_str_test.splitlines()
#FEATURE VECTOR features assigned
    left_per_test = []
    right_per_test = []
    len_three_test = []
    left_cap_test = []
    right_cap_test = []
    cl_label_test = []
    

#3 MORE Feature Vectors
    second_left_test = [] #word before the Word Left of Period 
    small_second_right_test = [] # Length of the 2nd right word
    second_right_test = [] #word after the Word Right of Period

    per_counter_test = 0
    
    for i in range(len(split_str_test)):
        x = split_str_test[i]
        if '. ' in x:
            per_counter_test+=1
            if ' EOS' in x:
                cl_label_test.append('EOS')

                #LEFT WORD OF PERIOD
                init_counter_test += 1
                l_word = x[:-4]
                new_word_l = rm_num(l_word)
                left_per_test.append(hash(new_word_l))

                #SECOND LEFT WORD OF PERIOD
                if i != 0:
                    l_count = 0
                    sl_str = split_str[i-1]
                    word_l = rm_num(sl_str)
                    second_left_test.append(hash(word_l))
                else:
                    second_left.append(0)

                #RIGHT WORD OF PERIOD
                if i+1 < len(split_str_test):
                    r_count = 0
                    r_str = split_str[i+1]
                    new_word_r = rm_num(r_str)
                    right_per_test.append(hash(new_word_r))

                    if new_word_r[0] != ' ':
                        if new_word_r[0].isupper():
                            right_cap_test.append(1)
                        else:
                            right_cap_test.append(0)
                    elif new_word_r[0] == ' ' and new_word_r[1].isalpha:
                        if new_word_r[1].isupper():
                            right_cap_test.append(1)
                        else:
                            right_cap_test.append(0)
                    else:
                        right_cap_test.append(0)

                else:
                    right_per_test.append(0)
                    right_cap_test.append(0)
                #SECOND WORD AFTER RIGHT OF PERIOD
                if i+2 < len(split_str_test):
                    r_count = 0
                    r_str = split_str_test[i+2]
                    new_word_r = rm_num(r_str)
                    second_right_test.append(hash(new_word_r))
                    if len(new_word_r) < 4:
                        small_second_right_test.append(1.0)
                    else:
                        small_second_right_test.append(0.0)
                else:
                    second_right_test.append(0)
                    small_second_right_test.append(0)
                #LEFT WORD LESS THAN 3 CHARS
                if len(new_word_l) < 3:
                    len_three_test.append(1)
                else:
                    len_three_test.append(0)
                # LEFT UPPERCASE FEATURE VECTOR
                if new_word_l[0].isupper():
                    left_cap_test.append(1)
                else:
                    left_cap_test.append(0)

            elif 'NEOS' in x:
                cl_label_test.append('NEOS')
                neos_counter_test += 1
                
                #LEFT WORD OF PERIOD
                l_word = x[:-5]
                new_word_l = rm_num(l_word)
                left_per_test.append(hash(new_word_l))

                #SECOND WORD LEFT OF PERIOD
                if i != 0:
                    l_count = 0
                    sl_str = split_str_test[i-1]
                    word_l = rm_num(sl_str)
                    second_left_test.append(hash(word_l))
                else:
                    second_left_test.append(0)
                #RIGHT WORD OF PERIOD
                if i+1 < len(split_str_test):
                    r_count = 0
                    r_str = split_str[i+1]
                    new_word_r = rm_num(r_str)
                    right_per_test.append(hash(new_word_r))
                    
                    if new_word_r[0] != ' ':
                        if new_word_r[0].isupper():
                            right_cap_test.append(1)
                        else:
                            right_cap_test.append(0)
                    elif new_word_r[0] == ' ' and new_word_r[1].isalpha:
                        if new_word_r[1].isupper():
                            right_cap_test.append(1)
                        else:
                            right_cap_test.append(0)
                    else:
                        right_cap_test.append(0)

                else:
                    right_per_test.append(0)
                    right_cap_test.append(0)
                
                #SECOND WORD RIGHT OF PERIOD
                if i+2 < len(split_str_test):
                    r_count = 0
                    r_str = split_str_test[i+2]
                    new_word_r = rm_num(r_str)
                    second_right_test.append(hash(new_word_r))
                    if len(new_word_r) < 4:
                        small_second_right_test.append(1.0)
                    else:
                        small_second_right_test.append(0.0)
                else:
                    second_right_test.append(0)
                    small_second_right_test.append(0.0)
                #LEFT WORD LESS THAN 3 CHARS
                if len(new_word_l) < 3:
                    len_three_test.append(1)
                else:
                    len_three_test.append(0)

                # LEFT UPPERCASE FEATURE VECTOR
                if new_word_l[0].isupper():
                    left_cap_test.append(1)
                else:
                    left_cap_test.append(0)


    #print(small_second_right)


#lb_test = LabelEncoder()
#fl_right_per_test = lb_test.fit_transform(right_per_test)
#fl_left_per_test = lb_test.fit_transform(left_per_test)
#sec_fl_left_test = lb_test.fit_transform(second_left_test)
#sec_fl_right_test = lb_test.fit_transform(second_right_test)

print(len(left_per_test))
print(len(right_per_test))
print(len(len_three_test))
print(len(left_cap_test))
print(len(second_left_test))
print(len(second_right_test))
print(len(small_second_right_test))
print(len(second_right))
print(len(small_second_right))
f_vect_test = [[] for x in range(len(second_right_test))]
for x in range(len(left_per_test)):
    f_in_vect_test = []
    f_in_vect_test.append(left_per_test[x])
    f_in_vect_test.append(right_per_test[x])
    f_in_vect_test.append(len_three_test[x])
    f_in_vect_test.append(left_cap_test[x])
    f_in_vect_test.append(right_cap_test[x])
    f_in_vect_test.append(second_left_test[x])
    f_in_vect_test.append(second_right_test[x])
    f_in_vect_test.append(small_second_right_test[x])
   
 
    f_vect_test[x] = f_in_vect_test


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


X_train = f_vect
Y_train = cl_label
X_test = f_vect_test
Y_test = cl_label_test

clf = DecisionTreeClassifier(max_depth=9, criterion="entropy")
clf = clf.fit(X_train, Y_train)

#res_pred = clf.predict(X_test)
score = clf.score(X_test, Y_test) 
print(score)




    


   



   # print(final_str, end='')
    #print(split_str)
    
   # print ('\n')
   # print('Number of EOS:', init_counter - neos_counter)
  #  print('Number of NEOS:', neos_counter)
   # print('Length of Left Per:', len(left_per))
   # print('Length of Right Per:', len(right_per))
   # print('Length of < 3:', len(len_three))
   # print('Length of Left Cap:', len(left_cap))
   # print('Length of Class:', len(cl_label))
   # print('Number of Per Counter:', per_counter)
    #print(f_vect)
   # print(len(f_vect))
    #print(right_per)
   # print(left_per)
    #print (right_per)
   # print(right_cap)

    #print(s1, end='')
    
#Need to make a feature vector
#Each feature vector will be 0,1 or number representation of word
#EXAMPLE: L<3 = [0,0,0,0,1,1,0,1] 
#Example: Word Left of (.) = []