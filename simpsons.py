def namelist(names):
    #check for empty input
    if len(names) > 0:
        #if not empty, create a list via a list comprehension
        names_list = [names[i]['name'] for i in range(len(names))]
    else:
        #else create an empty string
        names_list = ''
    #break the list into two to add commas and ampersand as required
    #create two empty strings if the initial list was empty (i.e., it was an empty input)
    if len(names_list) == 0:
        list1, list2 = '',''
    else:
        #first list is all members except for the last (or empty if only one member)
        list1 = names_list[0:-1]
        #second list is just the final member
        list2 = names_list[-1]
    #if the first list is empty it was either empty input or just one member recorded in list2
    if len(list1) == 0:
        return list2
    #otherwise combine the lists with commas and ampersand as per the requirement
    else:
        complete_list  = ', '.join(list1),' & ',list2
        complete_list2 = ''.join(complete_list)
        return complete_list2

namelist([{'name' : 'Bart'}, {'name' : 'Marge'}])
namelist([{'name' : 'Bart'}, {'name' : 'Marge'}, {'name' : 'Lisa'}, {'name' : 'Maggie'}, {'name' : 'Homer'}])
namelist([{'name' : 'Bart'}])
namelist([{'name' : 'Bart'}, {'name' : 'Marge'}, {'name' : 'Lisa'}, {'name' : 'Maggie'}])
namelist([])

#solution from codewars:
#def namelist(names):
#    if len(names) > 1:
#        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
#                                names[-1]['name'])
#    elif names:
#        return names[0]['name']
#    else:
#        return ''
