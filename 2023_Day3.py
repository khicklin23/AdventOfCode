#2023 Day 3
def integrityCheck(matrix: list):
    for Row, currentLine in enumerate(matrix):
        for i in currentLine:
            #Doesn't recognize the numbers (T) as foreign chars
            if i != '.' and i != 'T':
                return True


def partOne(file_input: str):
    sum = 0
    matrix = []
    with open(file_input, 'r') as file:
        for line in file:
            currentLine = list(line.strip())
            matrix.append(currentLine)
        
    for Row, currentLine in enumerate(matrix):
        Column = 0
        while Column < len(currentLine):
            #Check For Three Digit Num First (Important)
            if Column+2 < len(currentLine) and currentLine[Column].isdigit() and currentLine[Column+1].isdigit() and currentLine[Column+2].isdigit():
                #Grab value of the 3 digits because were going to be changing that later
                num = int(matrix[Row][Column]+matrix[Row][Column+1]+matrix[Row][Column+2])
                #Set the baseline for the surrounding digit matrix dimensions
                minH,maxH, minW, maxW = -1,2,-1,4

                #Change the number to something else to make parsing through the matrix earlier
                #The matrixes will be different sizes so the integrityCheck() needs to know where the number location is
                matrix[Row][Column] = 'T'
                matrix[Row][Column+1] = 'T'
                matrix[Row][Column+2] = 'T'

                #Alters the perameters for the matrix if you are close to an edge
                if Row == 0:
                    minH = 0
                elif Row == len(matrix)-1:
                    maxH = 0
                if Column == 0:
                    minW = 0
                elif Column == len(currentLine)-3:
                    maxW = 3

                #Grabs the rows above and below the numbers (minH and maxH will change the rows grabbed if needed)
                testRows = matrix[Row+minH:Row+maxH]
                #Creates an array of all surrounding chars (minW and maxW will change the columns grabbed if needed)
                #Defintely didn't use google for this little function lol but I did alter it with the minW and stuff
                surroundings = [row[Column+minW:Column+maxW] for row in testRows]

                #Calls the integrity check to see if it can find any non '.' chars surrounding the letters
                if integrityCheck(surroundings) == True:
                    sum += int(num)

                #Skip ahead 3 spaces so that the following nums arent re-read as 2 or 1 digit nums
                Column += 3

            #Two Digit Num (Same but with different values)
            elif Column+1 < len(currentLine) and currentLine[Column].isdigit() and currentLine[Column+1].isdigit():
                num = int(matrix[Row][Column]+matrix[Row][Column+1])
                minH,maxH, minW, maxW = -1,2,-1,3
                matrix[Row][Column] = 'T'
                matrix[Row][Column+1] = 'T'
                if Row == 0:
                    minH = 0
                elif Row == len(matrix)-1:
                    maxH = 0
                if Column == 0:
                    minW = 0
                elif Column == len(currentLine)-2:
                    maxW = 2 

                testRows = matrix[Row+minH:Row+maxH]
                surroundings = [row[Column+minW:Column+maxW] for row in testRows]
                if integrityCheck(surroundings) == True:
                    sum += int(num)
                Column += 2
            
            #One Digit Num (Same but with different values)
            elif Column < len(currentLine) and currentLine[Column].isdigit():
                num = int(matrix[Row][Column])
                minH,maxH, minW, maxW = -1,2,-1,2
                matrix[Row][Column] = 'T'
                if Row == 0:
                    minH = 0
                elif Row == len(matrix)-1:
                    maxH = 0
                if Column == 0:
                    minW = 0
                elif Column == len(currentLine)-1:
                    maxW = 0

                testRows = matrix[Row+minH:Row+maxH]
                surroundings = [row[Column+minW:Column+maxW] for row in testRows]
                if integrityCheck(surroundings) == True:
                    sum += int(num)
                Column += 2

            else:
                #If not a num then continue
                Column +=1
    print(sum)



def partTwo(file_input: str):
    sum = 0
    matrix = []
    with open(file_input, 'r') as file:
        for line in file:
            currentLine = list(line.strip())
            matrix.append(currentLine)
        Column = 0
    for Row, currentLine in enumerate(matrix):
        while Column < len(currentLine):
            if matrix[Row][Column] == '*':
                print()
            """This is tricky, I'm gonna have to figure out how many digits the number is,
            I'll have to look for digits touching the * but will also have to record up to
            three digit numbers going away from the * so the miniMatrix will be 7 wide
            
            I think the easiest way to do this is to make three seperate functions, one"""


#PC
print("Part One Answer:")
partOne(r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt')
#print("Part Two Answer:")
#partTwo(r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt')


#MacBook
#partOne(r'/Users/kadenhicklin/Desktop/AdventOfCode/input.txt')
#partTwo(r'/Users/kadenhicklin/Desktop/AdventOfCode/input.txt')



