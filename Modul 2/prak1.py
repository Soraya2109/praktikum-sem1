a, b, c = map(int, input().split(" "))

if a < b < c :
    print(f"{a} {b} {c}")
elif b < c < a :
    print(f"{b} {c} {a}")
elif c < b < a :
    print(f"{c} {b} {a}")
elif b < a < c :
    print(f"{b} {a} {c}")
elif c < a < b :
    print(f"{c} {a} {b}")
elif a < c < b :
    print(f"{a} {c} {b}")
else :
    print("hah?")