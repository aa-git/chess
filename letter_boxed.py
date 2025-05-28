from nltk.corpus import words

##all characters in CAPITALS

left = input('left col letters: ').upper()
right = input('right col letters: ').upper()
up = input('upper row letters: ').upper()
down = input('bottom row letters: ').upper()

memo = [ [ 0 for i in range(26)] for j in range(26) ]
words = words.words()
letters = [left, right, up, down]

#prepare memo table
for i in range(4):
    for j in range(4):
        if i==j:
            continue
        else:
            list_1 = letters[i]
            list_2 = letters[j]
            for ch_l in list_1:
                for ch_r in list_2:
                    memo[ord(ch_l)-65][ord(ch_r)-65] = 1
for i in range(26):
    for j in range(26):
        print (str(memo[i][j])+" ", end=' ')
    print("\n")

#filter words out using memo table
filtered_words = []
print("filtering words, total words in nltk corpus = "+str(len(words)))
for word_ in words:
    include = True
    word_ = word_.upper()

    if len(word_)<=2:
        include=False

    for i in range(len(word_)-1):
        if memo[ord(word_[i])-65][ord(word_[i+1])-65]==0:
            include = False
            break

    if include:
        filtered_words += [word_]

print(len(filtered_words[0]), filtered_words[4])

print("len of filtered words "+str(len(filtered_words)))
#print(filtered_words)

solutions = []## form [  [4, [..list of words..]], [5, [..list of words..]]   ] 

def add_to_solutions(word_indices):
    global solutions, filtered_words
    sol_to_add = [len(word_indices), []]
    for i in word_indices:
        sol_to_add[1] += [filtered_words[i]]
        #print(filtered_words[i])
    solutions += [sol_to_add]
    print (str(len(solutions))+" solutions found: ",sol_to_add)
    #raw_input()
    
    return

def get_next_word(words_chain_made, chs_to_cover, chain_length, starting_word):
    # words_chain_made is list of indices of words in corpus
    # chs_to_cover is a set
    # doesn't returns anything
    global filtered_words

    if chain_length<=0:
        return
    #print(chs_to_cover)
    if not starting_word:
        last_word = filtered_words[words_chain_made[-1]]
    for i in range(len(filtered_words)):    
        if starting_word or last_word[-1] == filtered_words[i][0]:
            if len(chs_to_cover.difference(set(filtered_words[i])))==0:
                add_to_solutions(words_chain_made+[i])
            else:
                get_next_word(words_chain_made+[i], chs_to_cover.difference(set(filtered_words[i])), chain_length-1, False)

    return

#calculate solutions
get_next_word([], set(left+right+up+down), 1, True)


print(str(len(solutions))+" solutions obtained")