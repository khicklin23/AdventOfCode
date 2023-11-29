fpath = r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt'
elf,curCal,mostCal1,mostCal2,mostCal3,lineNum= 0 , 0 , 0 , 0 , 0 , 0
with open(fpath, 'r') as file:

    for line in file:
        lineNum+=1
        #If Line Empty / End of elf's calorie list then determine whether or not to store value
        if not line.strip():
            if curCal > mostCal3:
                #If num1
                if (curCal > mostCal1) & (curCal > mostCal2):
                    mostCal2, mostCal3 = mostCal1, mostCal2
                    mostCal1 = curCal
                #If num2
                elif (curCal < mostCal1) & (curCal > mostCal2):
                    mostCal3 ,mostCal2, = mostCal2, curCal
                #If num3
                elif (curCal < mostCal1) & (curCal<mostCal2):
                    mostCal3, curCal = curCal, 0
            curCal = 0
            continue

        #If line has int then add to currentCalories
        curCal += int(line.strip())
        print(int(line.strip()))

sumE = (mostCal1 + mostCal2 + mostCal3)
print("\nThe Sum For Each Of The Individual Of The Top Three Elves Were: ",mostCal1, mostCal2, mostCal3)
print("\nThe sum of the top three elves is : " , sumE , "\n\n")
