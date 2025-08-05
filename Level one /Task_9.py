string = input("Enter your password: ")
vowles = "aouie"
password = ""
for i in string:
    if i in vowles:
        password += '*'
    else:  
        password += i
print(password)
