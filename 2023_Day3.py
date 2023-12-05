

def partOne(file_input: str):
    sum = 0
    twoDarr = []
    with open(file_input, 'r') as file:
        for line in file:
            row = list(line.strip())
            twoDarr.append(row)
    for row in twoDarr:
        for i in row:
            if i.isdigit() and [i + 1].isdigit() and [i + 2].isdigit():
                #Something like this to check for three digit then check surroundings but out of index errors might be a pain idk gtg tho
                
        break


"""
Pseudocode
    2d array

    Algorithim for single digits:
    if (i, row +- 1) != . -check above and below
       (i+-1 ,row +- 1) . -check perpendicular
    
    -Build string of chars then once next char down is != num then check but will have to account for length of num 
    -I think I'm going to cheat and check and see if its a one digit, two digit, or three digit num
        this will make it a lot easier than enabling ulimited digits

"""


#PC
print("Part One Answer:")
partOne(r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt')


#MacBook
#partOne(r'/Users/kadenhicklin/Desktop/AdventOfCode/input.txt')
#partTwo(r'/Users/kadenhicklin/Desktop/AdventOfCode/input.txt')




