fpath = r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt'
score = 0
convertAZ = {"A": "X", "B": "Y", "C": "Z"}
convertWin = {"Z": "X", "X": "Y", "Y": "Z"}
convertLose = {"X": "Z", "Y": "X", "Z": "Y"}
#Checks For Win / Loss
def test(elf: str,user: str):
    global score
    #Checks For Draw
    if (elf == user):
        score += 3
    #Checks For Win
    elif (elf == "X" and user == "Y") or (elf == "Y" and user == "Z") or (elf == "Z" and user == "X"):
        score += 6
    #We Don't Need To Check For Loss Because No Points Are Gained

#Adds Value Of Turn Played
def turnValue(turn: str):
    global score
    choice = {"X": 1, "Y": 2, "Z": 3}
    score += choice.get(turn, 0)

def edit_chars(chars):
    #Draw
    if (chars[1] == "Y"):
        #If Draw Set User Turn To The Same
        chars[1] = chars[0]
    #Lose
    elif (chars[1] == "X"):
        chars[1] = convertLose[chars[0]]
    #Win
    else:
        chars[1] = convertWin[chars[0]]
    revised_chars = chars
    return revised_chars

with open(fpath, 'r') as file:
    #Iterate Through Every Game Played
    for line_number, line in enumerate(file, start=1):
        # Split each line into two characters
        chars = line.strip().split()
        #Turns ABC to XYZ
        chars[0]= convertAZ.get(chars[0], chars[0])
        #Decripts the Win / Lose / Draw Strategy
        chars_new = edit_chars(chars)
        #Checks For Winner
        test(chars_new[0],chars_new[1])
        #Adds To Score For Shape Played
        turnValue(chars_new[1])

print(score)
