#def find_outlier(integers):
#    even_numbers = [x for x in integers if x%2 == 0]
#    odd_numbers = [x for x in integers if x%2 == 1]
#    if len(even_numbers) == 1:
#        x = even_numbers[0]
#        return x
#    else:
#        x = odd_numbers[0]
#        return x
#
#list1 = [2, 4, 0, 100, 4, 11, 2602, 36]
#
#list2 = [160, 3, 1719, 19, 11, 13, -21]
#
#find_outlier(list1)
#find_outlier(list2)

#another codewar example
def iq_test(numbers):
    num_list = numbers.split(' ')
    num_int = [int(x) for x in num_list]
    even = [x for x in num_int if x%2 == 0]
    odd = [x for x in num_int if x%2 == 1]
    if len(even) > len(odd):
        results = odd[0]
        print(results)
    else:
        results = even[0]
        print(results)
        #return results
    result = num_int.index(results)
    return(result+1)

iq_test("2 4 7 8 10")