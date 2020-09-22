def pig_it(text):
    #your code here
    split_text = text.split(' ')
    print(split_text)
    pig_sent = []
    for i in range(len(split_text)):
        if len(split_text[i]) > 1:
            new_word = split_text[i][1:] + split_text[i][0] + 'ay'
        elif i < len(split_text)-1:
            new_word = split_text[i] + 'ay'
        else:
            new_word = split_text[i]
        print(new_word)
        pig_sent.append(new_word)
    print(' '.join(pig_sent))
    final_sent = ' '.join(pig_sent)
    return final_sent

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
pig_it('O tempora o mores !')