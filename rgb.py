def rgb(r, g, b):
    if r > 255:
        r = 255
    elif r < 0:
        r = 0
    else:
        r
    if g > 255:
        g = 255
    elif g < 0:
        g = 0
    else:
        g
    if b > 255:
        b = 255
    elif b < 0:
        b = 0
    else:
        b
    if len(hex(r)[2:].upper()) == 1: 
        hexr = '0'+hex(r)[2:].upper()
    else: 
        hexr = hex(r)[2:].upper()
    if len(hex(g)[2:].upper()) == 1: 
        hexg = '0'+hex(g)[2:].upper()
    else: 
        hexg = hex(g)[2:].upper()
    if len(hex(b)[2:].upper()) == 1: 
        hexb = '0'+hex(b)[2:].upper()
    else: 
        hexb = hex(b)[2:].upper()
    #add extra 0 for 10 ten base
    hexall = hexr+hexg+hexb
    #print(hexall)
    return hexall


rgb(255, 255, 255) # returns FFFFFF
rgb(1255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
rgb(1,2,3)
rgb(-20, 275, 125) 
