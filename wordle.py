from nltk.corpus import words
w = words.words()

l = []
for i in w:
    if len(i)==5:
        l+= [i.lower()]

## l contains all 5 letter words
def check(history_):#state_, cont, no_, past):#both are strings
    global l
    f4 = l
    hh=zip(history_[0],history_[1],history_[2],history_[3])
    for state_, cont, no_, past in hh:
        f1 = []
        for w in f4:##green state
            s1=w[0]==state_[0]
            s2=state_[0]=='*'

            s3=w[1]==state_[1]
            s4=state_[1]=='*'

            s5=w[2]==state_[2]
            s6=state_[2]=='*'

            s7=w[3]==state_[3]
            s8=state_[3]=='*'

            s9=w[4]==state_[4]
            s10=state_[4]=='*'
           
            if (s1 or s2) and (s3 or s4) and (s5 or s6) and (s7 or s8) and (s9 or s10):
                f1 += [w]
       
        f2 = []
        for w in f1:##yellow state
            s1=w[0]==cont[0]
            s11=w.__contains__(cont[0])
            s2=cont[0]=='*'

            s3=w[1]==cont[1]
            s33=w.__contains__(cont[1])
            s4=cont[1]=='*'

            s5=w[2]==cont[2]
            s55=w.__contains__(cont[2])
            s6=cont[2]=='*'

            s7=w[3]==cont[3]
            s77=w.__contains__(cont[3])
            s8=cont[3]=='*'

            s9=w[4]==cont[4]
            s99=w.__contains__(cont[4])
            s10=cont[4]=='*'
           
            if (s2 or (not s1 and s11)) and (s4 or (not s3 and s33)) and (s6 or (not s5 and s55)) and (s8 or (not s7 and s77)) and (s10 or (not s9 and s99)):
                f2 += [w]
       
           
        f3 = []
       
        for w in f2:##grey state
            s1=w.__contains__(no_[0])
            s2=no_[0]=='*'

            s3=w.__contains__(no_[1])
            s4=no_[1]=='*'

            s5=w.__contains__(no_[2])
            s6=no_[2]=='*'

            s7=w.__contains__(no_[3])
            s8=no_[3]=='*'

            s9=w.__contains__(no_[4])
            s10=no_[4]=='*'
           
            if (not s1 or s2) and (not s3 or s4) and (not s5 or s6) and (not s7 or s8) and (not s9 or s10):
                f3 += [w]
               
        f4=[]
        for w in f3:
            include=True
            for ch in list(past):
                if w.__contains__(ch):
                    include=False
                    break
            if include:
                f4+=[w]
               
    return f4


past=''

history_ = [[],[],[], []]

while(1):
    state_ = input("give green characters,  else input *: ")#green characters, '*e*op'
    cont   = input("give yellow characters, else input *: ")#yellow characters, '*e*op'
    no_    = input("give grey characters,   else input *: ")# grey characters, '*e*op'
    past = no_.replace("*",'')+past

    history_[0] += [state_]
    history_[1] += [cont]
    history_[2] += [no_]
    history_[3] += [past]


    for w in check(history_):
        print(w)
    print("**************************************")