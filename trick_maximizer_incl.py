def run(tricks):
    list_points = []
    #prob list
    prob_list = []
    for i in range(0,10):
        prob_list.append(tricks[0]['probability']**(i+1))
    print(prob_list)
    for i in range(0,10):
        points = tricks[0]['points']*tricks[0]['mult_base']**i
        list_points.append(points)
        #print(points)
    print(list_points)
    total_points = []
    for i in range(0,10):
        total_points.append(tricks[0]['probability']**(i+1)*sum(list_points[:(i+1)]))
        #print(total_points)
    print(total_points)
    max_points_index = total_points.index(max(total_points))
    max_points = max(total_points)
    print(max_points)
    print(max_points_index)

#run([{ 'name': 'kickflip', 'points': 100, 'mult_base': .8, 'probability': .95 },
#						{ 'name': 'pop shove it', 'points': 50, 'mult_base': .75, 'probability': .995 },
#						{ 'name': '360 flip', 'points': 250, 'mult_base': .825, 'probability': .9 },
#						{ 'name': '50-50 grind', 'points': 150, 'mult_base': .9, 'probability': .925 },
#						{ 'name': 'noseslide', 'points': 100, 'mult_base': .8, 'probability': .95 },
#						{ 'name': 'manual', 'points': 50, 'mult_base': .99, 'probability': .975 },])

# Maximum expected score: 329.151004...
run([{ 'name': 'kickflip', 'points': 100, 'mult_base': .8, 'probability': .95 },
{ 'name': 'pop shove it', 'points': 50, 'mult_base': .75, 'probability': .995 },
{ 'name': '360 flip', 'points': 250, 'mult_base': .825, 'probability': .9 },
                        { 'name': 'heelflip', 'points': 101, 'mult_base': .25, 'probability': .95 },])

#503.087741015625
#172.90305250507015
#209.19949999999997
