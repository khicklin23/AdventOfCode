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
                #Every odd index of strArr is a color name and index prior is the amount
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
    with open(file_path, 'r') as file:
        for LineNum, line in enumerate(file, start=1):                
            #In progress
    



#PC
partOne(r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt')
#partTwo(r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt')

#MacBook
#partOne(r'/Users/kadenhicklin/Desktop/AdventOfCode/input.txt')
#partTwo(r'/Users/kadenhicklin/Desktop/AdventOfCode/input.txt')



