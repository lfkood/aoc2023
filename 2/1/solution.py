import re

with open("input.txt", "r") as file:
    input_string = file.read()

red_max = 12
green_max = 13
blue_max = 14
sum = 0

for line in input_string.splitlines():
    a = re.search("(\d+):", line)
    reds = re.findall("(/d+) red", line).sort(True)
    greens = re.findall("(/d+) green", line).sort(True)
    blues = re.findall("(/d+) blue", line).sort(True)

    if reds[0] > red_max:
        continue
    elif greens[0] > green_max:
        continue
    elif blues [0] > blue_max:
        continue

    sum += int(a)