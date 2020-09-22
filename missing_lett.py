#def find_missing_letter(chars):
#    #sort the input list
#    ordered = sorted(chars)
#    #check if lowercase
#    x = ordered[0].lower() == ordered[0]
#    #create an alphabet string
#    alph = 'abcdefghijklmnopqrstuvwxyz'
#    #change alph to uppercase if needed
#    if x:
#        alph    
#    else:
#        alph = alph.upper()
#    #check first and last input letter index
#    min_ordered = ordered[0]
#    max_ordered = ordered[-1]
#    alph_list = list(alph)
#    #keep just the subset of the alph based on input
#    subset = alph_list[alph_list.index(min_ordered):alph_list.index(max_ordered)+1]
#    return ', '.join([x for x in subset if x not in ordered])

def find_missing_letter(chars):
    # added in case the list is not in alphabetical order
    chars = sorted(chars)
    n = 0
    #ord returns an ASCII code for the character
    #so here it checks that first letter code is exactly 1 lower than the second, then iterates over the list
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    #return the character based on the ASCII code following the one where condition is not met = it was missing in the list
    print(chr(1+ord(chars[n])))
    return chr(1+ord(chars[n]))
    
find_missing_letter(["D","B","A","E","F"])