elements = [0,1,2,3,4,5,6,7,8,9]

for i in reversed(elements):

    print i

    if(i == 4):
        elements.remove(i)
