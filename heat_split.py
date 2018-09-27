



def test_for_range():
    upper = 121
    lower = 10
    gates = 16
    for parts in range(lower,upper):
        splits = get_splits_(gates, parts)
        print(create_race_list(splits[0], splits[1], parts))
        '''
        numRaces = splits[0]
        avg_size = splits[1]
        #last = splits[2]
        histo = '   ' + str(parts) + '   :: '
        for x in range(0, int(numRaces)):
            histo += ' ' + str(avg_size)
        
        histo += '   number of races = ' + str(numRaces)
        
        print(histo)
        '''
'''
def test_for_range_two():
    upper = 1000
    lower = 16
    gates = 16
    for ix in range(lower,upper):
        race_list = split_races_two(gates, ix)
        print(race_list)

def split_races_two(g, p):
    nr = 0
    race_list = []
    if(p%g == 0):
        nr = p//g
        for x in range(0, nr):
            race_list.append(g)
        return race_list
    else:
        nr = p//g + 1
        short_races = g - (p%g)
        size_correct = 1
        if(short_races > nr):
            size_correct 
        for x in range(0, nr):
            if (x < short_races):
                race_list.append(g-1)
            else:
                race_list.append(g)
        return race_list
'''

def get_splits_(g, p):
    nr = 0
    if (p//g < g/2):
        g = g//2
        nr = p//g
        race_size = g
    else:
        nr = p//g
        race_size = g
    if (nr > 20):
        if (p%(g*2) == 0):
            nr = p//(g*2)
        else:
            nr = (p//(g*2))
        race_size = g*2
    return nr, race_size, p


def create_race_list(numRaces, rSize, racers):
    print(rSize)
    r_list = []
    leftovers = racers % rSize 
    for x in range(0, numRaces):
        r_list.append(rSize)
    #print(r_list)
    if(leftovers > 0):
        if((numRaces - leftovers) < numRaces):
            extra = leftovers
            '''
            for y in range(0, (numRaces - leftovers)):
                ix = 1+y
                #print(ix)
                r_list[-ix] -= 1 
                extra += 1
            '''
            r_list.append(extra)
        else:
            r_list.append(leftovers)
    return r_list


def split_heat_to_finals(race_list, np):
    return 

#test_for_range_two()
test_for_range()


