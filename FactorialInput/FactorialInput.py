n = int(input("Въведете число: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(n, "x", i, "=", factorial)
