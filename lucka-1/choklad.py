print('Here is the answer to the first door in the Code Calendar 2022, Mikael!')

# 1. Create a variable to store the value
result = 0

# 2. Loop through the first range of numbers and add their values to the var
for digit in range(67, 95 + 1):
    result += digit

# 3. Loop through the second range of numbers and subtract their values from the var
for digit in range(48, 63 + 1):
    result -= digit

# 4. Print the var's value
print(f'The code is: {result}')
