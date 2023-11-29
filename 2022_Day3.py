fpath = r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt'
sum = 0
#I believe python has a built in function for 
def find_common(first: str, second: str):
    global sum
    for i in first:
        if i in second:
            if i.isupper():
                #Return 27-52 for uppercase
                sum += (ord(i) - ord('A') + 27)
            else:
                #Returns 1-26 for lowercase
                sum += (ord(i) - ord('a') + 1)
            break

with open(fpath, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        line_length = len(line)
        #Splits str into two even strings
        first_rucksack = line[:line_length // 2]
        second_rucksack = line[line_length // 2:]
        #Plugs each str into function
        find_common(first_rucksack , second_rucksack)
print(sum)

