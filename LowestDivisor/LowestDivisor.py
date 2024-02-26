n = int(input("Въведете цяло число >= 2: "))
for i in range(2, n + 1):
    if n % i == 0:
        print("Най-малкият цял делител е:", i)
        break
