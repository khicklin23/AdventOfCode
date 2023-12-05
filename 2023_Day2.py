#2023 Day 2
def partOne(file_input: str):
    sum = 0
    with open(file_input, 'r') as file:
        redMax, greenMax, blueMax = 12,13,14
        key = 0
        for LineNum, line in enumerate(file, start=1):
            myStr = line.strip()
            posGame = True
            strArr = myStr.split(' ')
            #Remove "Game N:"
            strArr = strArr[2:]
            for index, i in enumerate(strArr):
                #Every odd index of strArr is a color name and index prior is the amount ('4' , 'red')
                if index % 2 != 0:
                    if "blue" in i and int(strArr[index-1]) > blueMax:
                        posGame = False
                    elif "red" in i and int(strArr[index-1]) > redMax:
                        posGame = False
                    elif "green" in i and int(strArr[index-1]) > greenMax:
                        posGame = False
            if posGame == True:
                #Add Game ID to running count
                key += LineNum
        print(key)


def partTwo(file_input: str):
    sum = 0
    with open(file_input, 'r') as file:               
        key = 0
        for LineNum, line in enumerate(file, start=1):
            #Don't forget to set back to zero each line
            redMin, greenMin, blueMin = 0,0,0
            myStr = line.strip()
            strArr = myStr.split(' ')
            strArr = strArr[2:]
            for index, i in enumerate(strArr):
                if index % 2 != 0:
                    #Starts at zero and if biggest num so far then set new high
                    if "blue" in i and int(strArr[index-1]) > blueMin:
                        blueMin = int(strArr[index-1])
                    elif "red" in i and int(strArr[index-1]) > redMin:
                        redMin = int(strArr[index-1])
                    elif "green" in i and int(strArr[index-1]) > greenMin:
                        greenMin = int(strArr[index-1])
            key += (greenMin*redMin*blueMin)
        print(key)



#PC
print("Part One Answer:")
partOne(r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt')
print("Part Two Answer:")
partTwo(r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt')

#MacBook
#partOne(r'/Users/kadenhicklin/Desktop/AdventOfCode/input.txt')
#partTwo(r'/Users/kadenhicklin/Desktop/AdventOfCode/input.txt')



