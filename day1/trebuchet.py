import re

numbers_dict = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

def get_numbers(string):
    numbers = re.findall(r"(\d|one|two|three|four|five|six|seven|eight|nine)", string)
    first_number = ""
    last_number = ""

    if (numbers[0].isdigit()):
        first_number = numbers[0]
    else:
        first_number = numbers_dict.get(numbers[0])

    if (numbers[-1].isdigit()):
        last_number = numbers[-1]
    else:
        last_number = numbers_dict.get(numbers[-1])

    return first_number + last_number

lines = open("input.txt", "r").readlines()
calibration_total = 0

for line in lines:
    calibration_total += int(get_numbers(line))

print(calibration_total)
