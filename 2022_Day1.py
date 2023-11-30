fpath = r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt'
elf,curCal,mostCal1,mostCal2,mostCal3= 0 , 0 , 0 , 0 , 0 , 0
with open(fpath, 'r') as file:
    for line in file:
        #Runs when an empty line is met to signify the end of the elf calorie list
        if not line.strip():
            #Checks to see if it belongs on the podium
            if curCal > mostCal3:
                #Determines where (1,2, or 3)
                if (curCal > mostCal1) & (curCal > mostCal2):
                    mostCal2, mostCal3 = mostCal1, mostCal2
                    mostCal1 = curCal
                elif (curCal < mostCal1) & (curCal > mostCal2):
                    mostCal3 ,mostCal2, = mostCal2, curCal
                elif (curCal < mostCal1) & (curCal<mostCal2):
                    mostCal3, curCal = curCal, 0
            curCal = 0
            continue
        #Add line int to currentCalories
        curCal += int(line.strip())

sumE = (mostCal1 + mostCal2 + mostCal3)
print("\nThe Sum For Each Of The Individual Of The Top Three Elves Were: ",mostCal1, mostCal2, mostCal3)
print("\nThe sum of the top three elves is : " , sumE , "\n\n")
