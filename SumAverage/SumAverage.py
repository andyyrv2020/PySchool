n = int(input("Въведете броя на числата: "))
total = 0
for _ in range(n):
    num = int(input())
    total += num
average = total / n
print("Средно аритметичното е:", average)
