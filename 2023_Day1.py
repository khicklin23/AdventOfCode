file_path = r'/Users/kadenhicklin/Desktop/AdventOfCode/input.txt'

def partTwo(file_input: str):
    sum = 0
    charToNum = { "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, 
                 "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9 }
    with open(file_path, 'r') as file:
        for LineNum, line in enumerate(file, start=1):
            intArr = []
            myStr = line.strip()
            for word, num in charToNum.items():
                myStr = myStr.replace(word, str(num))
            for i in myStr:
                if i.isdigit():
                    intArr.append(i)
            var = (str(intArr[0])+str(intArr[-1]))
            sum += int(var)
            print(var)
        print(sum)


def partOne(file_input: str):
    sum = 0
    with open(file_input, 'r') as file:
        for LineNum, line in enumerate(file, start=1):
            myStr = line.strip()
            intArr = []
            for i in myStr:
                if i.isdigit():
                    intArr.append(i)
            var = (str(intArr[0])+str(intArr[-1]))
            sum += int(var)  
        print(sum)   
            
#partOne('/Users/kadenhicklin/Desktop/AdventOfCode/input.txt')
partTwo('/Users/kadenhicklin/Desktop/AdventOfCode/input.txt')

