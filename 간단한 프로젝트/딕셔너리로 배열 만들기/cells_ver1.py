D = {}      #empty dictionary

D['row'] = [1,2,3,4,5,6]    #6줄
D['column'] = [1,2,3,4]     #4줄

def cell(x, y):
    return (D['row'][x]*D['column'][y])

for i in range(0, len(D['row'])):
    for j in range(0, len(D['column'])):
        print(cell(i, j), end='\t')
    print()
