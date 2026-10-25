num = int(input("Enter a positive integer: "))
original_num = num

if num == 0:
    octal_str = "0"
else:
    octal_str = ""
    while num > 0:
        remainder = num%8
        octal_str = str(remainder)+octal_str
        num = num // 8

print(f"octal equivalent(string):{octal_str}")
inbuilt_oct = oct(original_num)[2:]

if octal_str == inbuilt_oct:
    print("verification successful:matches inbuilt_oct()function!")
else:
    print("verification failed:does not match inbuilt_oct()function.")