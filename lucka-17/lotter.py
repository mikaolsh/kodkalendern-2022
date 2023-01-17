import math
for i in range(1, 1000 + 1):
    i0_string = str(i)
    i1_string = str(i+1)
    sum = int(i0_string + i1_string)
    if math.sqrt(sum).is_integer():
        print(i)
