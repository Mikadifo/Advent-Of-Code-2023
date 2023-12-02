lines = open("input.txt", "r").readlines()
calibration_total = 0

for line in lines:
    numbers_only = "".join(c for c in line if c.isdigit())
    calibration_total += int(numbers_only[0] + numbers_only[-1])

print(calibration_total)
