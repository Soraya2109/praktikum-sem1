maks = int(input())

for i in range(1, maks+1) :
    if i % 2 != 0 :
        print(i, end=" ")
print(" ")
for i in range(maks, 1, -1):
    if i % 2 == 0:
        print(i, end=" ")