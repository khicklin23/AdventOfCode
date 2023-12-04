file_path = r'/Users/kadenhicklin/Desktop/AdventOfCode/input.txt'
import re


def partOne(file_input: str):
    sum = 0
    with open(file_input, 'r') as file:
        redMax, greenMax, blueMax = 12,13,14
        for LineNum, line in enumerate(file, start=1):
            myStr = line.strip()
            myStr.replace(',','')
            print(myStr)
            strArr = myStr.split(' ')
            strArr = strArr[2:]
            for i in strArr:
                if i%2 == 0:
                    if "blue" in strArr[i]:
                        b += d
                r,g,b = 0,0,0
            print(strArr)
            
            
            
            
"""def partTwo(file_input: str):
    sum = 0
    with open(file_path, 'r') as file:
        for LineNum, line in enumerate(file, start=1):"""
            
partOne('/Users/kadenhicklin/Desktop/AdventOfCode/input.txt')
#partTwo('/Users/kadenhicklin/Desktop/AdventOfCode/input.txt')


