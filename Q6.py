n = int(input())

for num in range(1,n+1):
    temp = num
    total = 0
    power = len(str(num))

    while temp > 0:
        digit = temp%10
        total = total+(digit**power)
        temp = temp//10

    if total == num:
        print(num)