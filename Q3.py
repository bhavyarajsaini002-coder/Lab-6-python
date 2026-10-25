N = int(input("Enter N for pattern A: "))
row = 1

while row <= N:
    col = 1
    while col <= row:
        print(col,end=" ")
        col += 1
    print()
    row += 1


N = int(input("Enter the number of lines: "))
i = 0
while i< N:
    print(""*i, end="")
    j = 0
    while j < (N-i):
        print("*", end=" ")
        j += 1
    print()
    i +=1


N = int(input('Enter the number of lines: '))
i = 1
while i <= N:
    print(" "*(N-i),end="")
    j = 1
    while j <= i:
        print('*',end='')
        j += 1
    print()
    i += 1