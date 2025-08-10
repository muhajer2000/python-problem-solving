#task : Check if a string is a palindrome.

string = input("Enter your string: ")
new_string = ""
for i in string: 
    if ord(i) > 65 and ord(i) < 90:
        new_string += chr(ord(i) + 32)
    else:
        new_string += i

print(f"\nstring after convert to lower case [{new_string}]")
i = 0 
j = len(new_string) - 1
is_plindorme = True
while i < j:
    if new_string[i] != new_string[j]:
        is_plindorme = False
        break
    i += 1
    j -= 1
if is_plindorme:
    print("string is plindorme")
else:
    print("string isn't plindorme")