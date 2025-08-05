
for i in range(10):
    for j in range(10):
        for k in range(10):
            for n in range(10):
                print(i,j,k,n, end=" ")
                if i == 9 and j == 9 and k == 9 and n == 9:
                    break
                print("-", end=" ")
