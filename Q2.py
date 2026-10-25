N = int(input("Enter N: "))
slot = 1
while slot <= 1000:
    if slot%N == 0:
        if slot%4 == 0:
            slot += 1
            continue
        print(slot,end="")
    slot += 1
    print()