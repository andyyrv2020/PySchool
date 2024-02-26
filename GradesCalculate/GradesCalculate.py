grade = float(input("Въведете оценка: "))
if 2.00 <= grade <= 2.99:
    print("слаб")
elif 3.00 <= grade <= 3.49:
    print("среден")
elif 3.50 <= grade <= 4.49:
    print("добър")
elif 4.50 <= grade <= 5.49:
    print("мн. добър")
elif 5.50 <= grade <= 6.00:
    print("отличен")
else:
    print("Невалидна оценка")
