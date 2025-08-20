
# Nested loops --> Loops inside a loop.

#Outer loop -- controls rows
#inner loop -- controls columns


# A square of stars

#rows = 5

#for i in range(rows):
#    for j in  range(rows):
#        print('*', end = ' ')
#    print()
    

for i in range(1,6):
    for j in  range(i):
        print('*', end = ' ')
    print()
        