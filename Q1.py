print("   ",end=" ")

for i in range(1,10):
    print(i,"\t",end="")
print()
print("="*45)

for i in range(1,10):
    # print(i,end="")
    print(i,"\t",end="")
    for j in range(1,10):
        print(i+j,"\t",end="")
    print()