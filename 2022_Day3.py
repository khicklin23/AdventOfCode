fpath = r'C:\Users\hickl\OneDrive\Documents\AdventOfCode\input.txt'
sum = 0
#Function to check for common char and find numerical value then append it to sum
def find_common(first: str, second: str , third: str):
    global sum
    for i in first:
        if i in second:
            if i in third:    
                if i.isupper():
                    #Return 27-52 for uppercase
                    sum += (ord(i) - ord('A') + 27)
                else:
                    #Returns 1-26 for lowercase
                    sum += (ord(i) - ord('a') + 1)
                break
with open(fpath, 'r') as file:
    str1,str2,str3="","",""
    for line_number, line in enumerate(file, start=1):
        #Assigns line 1,2,3 to variables then calls the function every 3 lines and resets
        if line_number % 3 == 1:
            str1 = line.strip()
        elif line_number % 3 == 2:
            str2 = line.strip()
        elif line_number % 3 == 0:
            str3 = line.strip()
            find_common(str1 ,str2 ,str3)
print(sum)
