def countBits(n):
    binary_n = bin(n)
    binary_n_list = list(binary_n)
    keep_ones = [x for x in binary_n_list if x == '1']
    return len(keep_ones)

countBits(1234)

#def countBits(n):
#    return bin(n).count("1")