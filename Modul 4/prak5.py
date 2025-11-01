a, b = map(int, input().split(" "))

sum = 0

for baris in range(1, a+1) :
    this_sum = 0
    for j in range(baris, 0, -1) :
        this_sum += j * b

        if (j > 1) :
            print(f"({j} * {b}) + ", end="")
        else :
            print(f"({j} * {b}) ", end="")

    print(f"= {this_sum}")
    sum += this_sum

print(f"{sum}")