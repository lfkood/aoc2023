line_list = []
while True:
    line = input()
    if line == "":
        break
    line_list.append(line)

sum = 0
for line in line_list:
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