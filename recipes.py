def cakes(recipe, available):
    multiples = []
    for i in recipe:
        try:
            multiples.append(available[i]/recipe[i])
        except KeyError:
            multiples.append(0)
    final_number = int(sorted(multiples)[0])
    print(final_number)
    print(recipe.get('apples',0))
    return final_number

#simplified into one line from Codewars:
#def cakes(recipe, available):
#    return min(available.get(k, 0)/recipe[k] for k in recipe)
#def cakes(recipe, available):
#    try:
#        return min([available[a]/recipe[a] for a in recipe])
#    except:
#        return 0

# must return 2
cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
# must return 0
cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000})