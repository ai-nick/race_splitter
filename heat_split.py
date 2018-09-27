



def test_for_range():
    upper = 321
    lower = 10
    gates = 8
    with open("%d_gate_heats.csv" %(gates), 'w') as f:
        for parts in range(lower,upper):
            firstLine = "%d racers \n" %(parts)
            f.write(firstLine)
            splits = get_splits_(gates, parts)
            mains = create_race_list(splits[0], splits[1], parts)
            print(mains)
            for i in mains:
                nextLine = "%d ," %(i)
                f.write(nextLine)
            f.write("\n")
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
            ix = 0
            for y in range(0, (rSize - leftovers)):
                ix += 1
                if(ix > len(r_list)):
                    ix = 1
                #print(ix)
                r_list[-ix] -= 1 
                extra += 1
            r_list.append(extra)
        else:
            r_list.append(leftovers)
    return r_list


def split_heat_to_finals(race_list, np):
    return 

#test_for_range_two()
test_for_range()


