N = int(input("Enter numbers of lines: "))

for i in range(1,N+1):
    print(" "*(N-i),end="")
    
    for j in range(i):
        print(i,end=" ")
    print()