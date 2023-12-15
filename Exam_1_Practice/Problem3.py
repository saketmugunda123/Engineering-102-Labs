roster = [[123004567], ['Joe', 'Aggie', 'ENGE', 3.50]]
uin = int(input('Enter a UIN: '))
if uin in roster[0]:#If searching through list of lists, you have to check that particular list to see if it is in there, not the whole roster
    print(f'{roster[1][0]} {roster[1][1]}: {roster[1][2]}, {roster[1][3]}')

    
