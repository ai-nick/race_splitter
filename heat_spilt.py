



def test_for_range():
    upper = 1000
    lower = 8
    gates = 16
    for parts in range(lower,upper):
        splits = get_splits_(gates, parts)
        numRaces = splits[0]
        avg_size = splits[1]
        #last = splits[2]
        histo = '   ' + str(parts) + '   :: '
        for x in range(0, int(numRaces-1)):
            histo += ' ' + str(avg_size)
        histo += ' ' + str((avg_size*numRaces)-parts)
        histo += '     races = ' + str(numRaces) + '  capacity: ' + str(avg_size * numRaces)
        '''
        histo += '   raceXavg_race_size = ' + str(numRaces * avg_size)
        '''
        print(histo)

def get_splits_(g, p):
    nr = 0
    if (p//g < g):
        g = g//2
        if (p%g == 0):
            nr = p//g
            race_size = g
        else:
            nr = (p//g) + 1
            race_size = g
    else:
        if (p%g > 0):
            '''
            mid = g//2
            for x in range(mid, g):
                if(p%x == 0):
                    nr = p//x
                    race_size = x
                    '''
            nr = (p//g)+1
            race_size = g
    if(nr == 0):
        nr = (p//g) + 2
        race_size = g
    if (nr > 30):
        nr = p//(g*2)
        race_size = g*2
    if (p > nr * (p//nr)):
        nr += 1
    return nr, race_size

test_for_range()



