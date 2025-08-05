string = input("Enter your binary number:")
binary_num = string[::-1]  # reveser the binary number to read form right ot left
result = 0   # result in decimal number
power = 0    #power of number

for i in binary_num:
    if i == '1':
        result += 2 ** power
        power += 1
    else:
        power += 1
print(f"the decimal number of {string} = {result}")