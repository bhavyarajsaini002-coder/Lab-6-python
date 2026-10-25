print("N","N^2","N^3","Square Root")

for n in range(1,16):
    square = n*n
    cube = n*n*n
    root = n**0.5

    rounded_root = round(root,4)

    print(n,square,cube,rounded_root)