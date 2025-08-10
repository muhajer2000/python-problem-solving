# task :  Continuously ask for a password until the correct one is entered.

user = input("Enter your user name: ")
passkey = ''
user_password = "1234"
while passkey != user_password:
    passkey = input("Enter your pass: ")
print("Alow acess")