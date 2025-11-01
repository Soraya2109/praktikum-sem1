a, b = map(int, input().split(" "))

if a > b :
    min = b
    max = a
    while a > min :
        print(str(a) + " " + str(b) + " - ", end="")
        a = a - 1
        b = b + 1
    print(str(a) + " " + str(b), end=" ")

else :
    min = a
    max = b
    while a < max :
        print(str(a) + " " + str(b) + " - ", end="")
        a = a + 1
        b = b - 1
    print(str(a) + " " + str(b), end=" ")