a = 10
b = 20

# understanding while loop structure
while b > a:
    if b % 2 == 0:
        b -= 1
        continue
    if b == 11:
        break
    print(b)
    b -= 1

else:
    print('Hey, I am done with looping and have exited normally!!')
