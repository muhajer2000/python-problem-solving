# task : login system



# check with date is store in database
user_name_saved = "muhajer"
muhajer_pass = "224488"
atemp = 3
while atemp > 0:
    user_name = input("enter your user_name: ")
    passkey = input("Enter your passkey: ")
    if user_name == user_name_saved and passkey == muhajer_pass:
            print("Allow Acess: wellcome", user_name)
            break
    else:
            atemp -= 1
            print("Access denid: wrong password or user name")
            if atemp > 0:
                print(f"you have {atemp} attempt left\n")
            else:
                print("Acess blocked, too many faild")
   