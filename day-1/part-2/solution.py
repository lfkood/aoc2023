import re

with open("input.txt", "r") as file:
    input_string = file.read()

input_string = re.sub("one", "o1ne", input_string)
input_string = re.sub("two", "t2o", input_string)
input_string = re.sub("three", "t3e", input_string)
input_string = re.sub("four", "4", input_string)
input_string = re.sub("five", "5e", input_string)
input_string = re.sub("six", "6", input_string)
input_string = re.sub("seven", "7", input_string)
input_string = re.sub("eight", "ei8ht", input_string)
input_string = re.sub("nine", "ni9ne", input_string)


sum = 0
for line in input_string.splitlines():
    calibration_number = ""
    for letter in line:
        if letter.isnumeric():
            calibration_number += str(letter)
            break
    for letter in line[::-1]:
        if letter.isnumeric():
            calibration_number += str(letter)
            break
    sum += int(calibration_number)
print(sum)
