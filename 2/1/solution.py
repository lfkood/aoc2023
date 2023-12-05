import re

with open("2.txt", "r") as file:
    input_string = file.read()

red_max = 12
green_max = 13
blue_max = 14
sum = 0

def cast_to_int_and_sort(list):
    new_list = []
    for x in list:
        new_list.append(int(x))
        new_list.sort(reverse=True)
    return new_list
for line in input_string.splitlines():
    a = re.findall("(\d+):", line)
    
    reds = cast_to_int_and_sort(re.findall("(\d+) red", line))
    greens = cast_to_int_and_sort(re.findall("(\d+) green", line))
    blues = cast_to_int_and_sort(re.findall("(\d+) blue", line))

    if reds != None:
        if int(reds[0]) > red_max:
            continue
    if greens != None:
        if int(greens[0]) > green_max:
            continue
    if blues != None:
        if int(blues[0]) > blue_max:
            continue

    sum += int(a[0])

print(sum)