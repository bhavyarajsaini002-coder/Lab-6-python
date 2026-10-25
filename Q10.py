n = int(input("Enter an odd positive integers: "))

mid = n//2

for i in range(mid+1):
    for j in range(mid-i):
        print(" ",end="")

    for j in range(2*i+1):
        print("*",end="")

    print()

for i in range(mid-1,-1,-1):
    for j in range(mid-i):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()