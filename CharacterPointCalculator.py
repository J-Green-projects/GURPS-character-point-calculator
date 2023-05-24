def PointCalc(text, delimiter):
    '''[list of strings], string -> number
    \ntakes a readlines output and returns a sum of the integers after a custom delimiter'''

    NumberBin = []

    for i in range(len(text)):
        # get indices of all start delimiters
        if delimiter in text[i]:
            indices = [j for j, c in enumerate(text[i]) if c == delimiter] 
            # copy text up to 3 characters after the delimiter depending on amount of digits
            for k in range(len(indices)):
                if len(text[i][indices[k]:]) > 3:
                    if text[i][indices[k]+3].isdigit():
                        NumberBin.append(text[i][indices[k]+1:indices[k]+4])
                    elif text[i][indices[k]+2].isdigit():
                        NumberBin.append(text[i][indices[k]+1:indices[k]+3])
                    else:
                        NumberBin.append(text[i][indices[k]+1])
                elif len(text[i][indices[k]:]) > 2:
                    if text[i][indices[k]+2].isdigit():
                        NumberBin.append(text[i][indices[k]+1:indices[k]+3])
                    else:
                        NumberBin.append(text[i][indices[k]+1]) 
                else:
                        NumberBin.append(text[i][indices[k]+1]) 
    # convert string-digits into integers
    for i in range(len(NumberBin)):
        if NumberBin[i].isnumeric():
            NumberBin[i] = int(NumberBin[i])
        else:
            NumberBin[i] = 0
    # final product, a tally.
    return sum(NumberBin)

# "user interface"
x = input("please enter the filepath: ")

with open(x, 'r') as file:
    sheet = file.readlines()

y = input("please enter your delimiter (the character before the number): ")


print("your total is: " + str(PointCalc(sheet, y)) + " points")

input("press enter to exit script...")
