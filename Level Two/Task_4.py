#check if it prime number
# start from zero to 100

number = int(input("Enter your number: "))

for n in range(number):
    if n > 1:
        i = 2
        is_prime = False
        while i * i <= n:
            if n % i == 0:
                is_prime = True
                break
            i +=1
        if is_prime == False:
            print(n)
    