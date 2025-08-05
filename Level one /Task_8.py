
string = input("Enter your string: ")
new_string = ""
for  i in string:
    if ord(i) >= 97 and ord(i) <= 122:
        new_string += chr(ord(i) - 32)
    elif ord(i) >= 65 and ord(i) <= 90:
        new_string += chr(ord(i) + 32)
    else:
        new_string += i
print(new_string)
