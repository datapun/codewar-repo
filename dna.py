#def DNA_strand(dna):
#    list_chars = [char for char in dna]
#    new_list = []
#    for i in range(len(list_chars)):
#        if list_chars[i] == 'T':
#            x = list_chars[i].replace('T','A')
#            new_list.append(x)
#        elif list_chars[i] == 'A':
#            x = list_chars[i].replace('A','T')
#            new_list.append(x)
#        elif list_chars[i] == 'C':
#            x = list_chars[i].replace('C','G')
#            new_list.append(x)
#        elif list_chars[i] == 'G':
#            x = list_chars[i].replace('G','C')
#            new_list.append(x)
#        else:
#            continue
#    #print(''.join(new_list))
#    return ''.join(new_list)

#using maketrans and translate
def DNA_strand(dna):
    print(dna.translate(dna.maketrans("ATCG","TAGC")))

    
DNA_strand('TAACG')
DNA_strand('GGG')
DNA_strand('GGC')
DNA_strand('AAATTC')