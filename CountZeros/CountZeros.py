n = int(input("Въведете брой числа: "))
count = 0
for _ in range(n):
    num = int(input())
    if num == 0:
        count += 1
print("Брой на срещанията на 0:", count)
