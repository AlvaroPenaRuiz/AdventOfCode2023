from functools import reduce
import re

number_translation = {
    "one":      "1",
    "two":      "2",
    "three":    "3",
    "four":     "4",
    "five":     "5",
    "six":      "6",
    "seven":    "7",
    "eight":    "8",
    "nine":     "9",
}
rawdata = ""

with open("data.txt", "r") as file:
    rawdata = file.read()

def decrypt_line(line: str):
    first = None
    last = None

    for char in line:
        if char.isnumeric(): 
            last = char
            if not first:
                first = char

    return f"{first}{last}"


def decrypt_line_hardway(line: str):
    numbers_positioned = []

    for index, char in enumerate(line):
        if char.isnumeric(): 
            numbers_positioned.append((index, char))

    for number in number_translation:
        for word_matched in re.finditer(number, line):
            numbers_positioned.append((word_matched.start(), number_translation[number]))
    
    numbers_positioned.sort(key=lambda element : int(element[0]))


    return f"{numbers_positioned[0][1]}{numbers_positioned[-1][1]}"


data = rawdata.split("\n")
lines_decrypted_wrongly = [decrypt_line(line) for line in data]
lines_decrypted_rightly = [decrypt_line_hardway(line) for line in data]


# Result exercise 1
total_wrongly = reduce(lambda a,b : int(a) + int(b), lines_decrypted_wrongly) 
print(total_wrongly)

# Result exercise 2
total_rightly = reduce(lambda a,b : int(a) + int(b), lines_decrypted_rightly) 
print(total_rightly)

