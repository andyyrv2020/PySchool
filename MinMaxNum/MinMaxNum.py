n = int(input("Въведете броя на числата: "))
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
min_num = min(numbers)
max_num = max(numbers)
print("Минимумът е:", min_num)
print("Максимумът е:", max_num)
