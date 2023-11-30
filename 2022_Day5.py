'''
#Edit - I just went and looked at part 2 and I think I'm gonna have to rework it all lol
#Part One
fpath = r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt'
import re #This import is a cheatcode for this stuff

"""
I think this is the only time I've ever used a stack willingly I've been waiting 3 years for this lol,
this one was basically taylormade for it, you could do it with an array but it'd take longer
I really did try to automate the initializaiton of the stacks to where you didn't have
to type the stack contents in the code but it was going to take too long so I just cheated
and initialized them myself. I might come back later and do it.
"""

class Crates:
    #Standard multi-stack class
    def __init__(self): 
        self.stacks = [["W","M","L","F"], ["B", "Z", "B","M","F"], ["H","V","R","S","L","Q"],["F","S","V","Q","P","M","T","J"],["L","S","W"],
                       ["F","V","P","M","R","J","W"],["J","Q","C","P","N","R","F"],["V","H","P","S","Z","W","R","V"],["B","M","J","C","G","H","Z","W"]]
    def push(self, stack_num, item):
        self.stacks[stack_num - 1].append(item)
    
    def pop(self, stack_num):
        return self.stacks[stack_num - 1].pop()

    def move(self, from_stack, to_stack):
        item = self.pop(from_stack)
        self.push(to_stack, item)


crates = Crates()

with open(fpath, 'r') as file:
    for LineNum, line in enumerate(file, start=1):
        #Skips first 11 lines but if you wanted to get fancier you could
        if LineNum < 11:
            continue
        
        myStr = line.strip()
        #Life Saver
        pattern = r"move (\d+) from (\d+) to (\d+)"
        match = re.match(pattern, myStr)
        amount = int(match.group(1))
        fromCrate = int(match.group(2))
        toCrate = int(match.group(3))

        while amount >0:
            crates.move(fromCrate, toCrate)
            amount -= 1

print("Key: ",crates.pop(1), crates.pop(2), crates.pop(3), crates.pop(4), crates.pop(5), crates.pop(6), crates.pop(7), crates.pop(8), crates.pop(9), sep="")
'''
