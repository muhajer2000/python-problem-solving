
year = int(input("Enter your year: "))   #enter your year

# check your year if it leap
if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    print("is leap")
else:
    print("not leap")