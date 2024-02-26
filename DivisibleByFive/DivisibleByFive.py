n = int(input("Въведете броя на числата: "))
count = 0
for _ in range(n):
    num = int(input())
    if num % 5 == 0:
        count += 1
print("Броят на числата, които се делят на 5, е:", count)
