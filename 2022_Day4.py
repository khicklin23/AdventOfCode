"""
Things are getting spicy so I'm going to include both parts now.

Part one:
fpath = r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt'
sum = 0
import re #This import is a cheatcode for this stuff

def compare(a1: int, a2: int, b1: int, b2: int):
    global sum
    if ((a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2)):
        sum += 1
        

with open(fpath, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        myStr = line.strip()
        pattern = r'(\d+)-(\d+)'
        # Find all matches in the input string
        matches = re.findall(pattern, myStr)
        num1, num2 = map(int, matches[0])
        num3, num4 = map(int, matches[1])
        compare(num1,num2,num3,num4)
print(sum)  
"""
#Part 2
fpath = r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt'
sum = 0
import re #This import is a cheatcode for this stuff

def compare(a1: int, a2: int, b1: int, b2: int):
    global sum
    #I try to get away from using a lot of if statements but I couldn't think of a fancy way to do this one
  
    #Checking for total overlap
    if ((a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2)):
        sum += 1
    #Checking for bottom overlap
    elif ((a1 <= b1 and a2 >= b1) or (b1 <= a1 and b2 >= a1)):
        sum += 1
    #Checking for upper overlap
    elif ((a1 <= b2 and a2 >= b2) or (b1 <= a2 and b2 >= a2)):
        sum += 1  

with open(fpath, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        myStr = line.strip()
        pattern = r'(\d+)-(\d+)'
        # Find all matches in the input string
        matches = re.findall(pattern, myStr)
        num1, num2 = map(int, matches[0])
        num3, num4 = map(int, matches[1])
        compare(num1,num2,num3,num4)
print(sum)  
