#my solution
def anagrams(word, words):
    new_list = []
    orig_words = []
    for i in range(len(words)):
        orig_words.append(words[i])
    print(orig_words)
    for i in range(len(word)):
        for j in range(len(words)):
            if word[i] in words[j]:
                words[j] = words[j].replace(word[i],'',1)
                print(word[i], words[j])
            else:
                words[j] = words[j]
            if i == len(word)-1:
                print('final printout',words[j])
                new_list.append(words[j])
    print(new_list)
    print(orig_words)
    anagram_list = []
    print(orig_words[0])
    for i in range(len(new_list)):
        if new_list[i] == '' and len(word) == len(orig_words[i]):
            anagram_list.append(orig_words[i])
        else:
            continue
    print('anagram list',anagram_list)
    return anagram_list

#solution from Codewars:
#def anagrams(word, words): print([item for item in words if sorted(item)==sorted(word)])

#anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

#anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) #=> ['carer', 'racer']
#anagrams('abab',['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa'])
#anagrams('laser', ['lazing', 'lazy',  'lacer']) #=> []