n = int(input("Въведете число: "))
sum = 0
count = 0
while sum < n:
    count += 1
    sum += count
print("За да се получи числото", n, "трябва да се сумират", count, "последователни числа.")