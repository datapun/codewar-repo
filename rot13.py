def rot13(message):
    list_message = list(message)
    print(list_message)
    new_message = []
    for i in list_message:
        #very brittle and non-dynamic
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            if ord(i) >= 110 or (ord(i) >= 78 and ord(i) <= 90):
                print('orig char',chr(ord(i)))
                print('new char is',chr(ord(i)-13))
                new_message.append(chr(ord(i)-13))
            elif (ord(i) >= 97 and ord(i) <= 109) or ord(i) <= 77: 
                print('orig char',chr(ord(i)))
                print('new char is',chr(ord(i)+13))
                new_message.append(chr(ord(i)+13))
        else:
            print('if special chars',i)
            new_message.append(chr(ord(i)))
    final_message = ''.join(new_message)
    print(final_message)
    return final_message

#using encode (was not allowed in codewars)
#import string
#
#def rot13(message):
#    return message.encode("rot13")

#top solution otherwise
#import string
#from codecs import encode as _dont_use_this_
#from string import maketrans, lowercase, uppercase
#
#def rot13(message):
#    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
#    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
#    return message.translate(lower).translate(upper)

rot13("testT.")
rot13("tnsdk")
rot13('N')