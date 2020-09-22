#def sort_array(source_array):
#    odd_list = [x for x in source_array if x%2 == 1]
#    sorted_odd = sorted(odd_list)
#    n = 0
#    for i in range(len(source_array)):
#        if source_array[i]%2 == 1:
#            source_array[i] = sorted_odd[n]
#            n += 1
#        else:
#            source_array[i]        
#    return source_array

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  print(odds)
  #print ([x if x%2==0 else odds.pop() for x in arr])
  return [x if x%2==0 else odds.pop() for x in arr]

sort_array([5,3,2])
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

