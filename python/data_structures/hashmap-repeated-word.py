
def hash_repeat(sentence):
    dic = {}
    sentence = sentence.replace(',' and '.' and '-', '').lower().split()

    for word in sentence:
        if word in dic:
            print(word)
            break
        else:
            dic[word] = 1
