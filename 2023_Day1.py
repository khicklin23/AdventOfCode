#Part One
"""fpath = r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt'
sum = 0
with open(fpath, 'r') as file:
    for LineNum, line in enumerate(file, start=1):
        myStr = line.strip()
        intArr = []
        for i in myStr:
            if i.isdigit():
                intArr.append(i)
        var = (str(intArr[0])+str(intArr[-1]))
        sum += int(var)  
print(sum)              
"""
