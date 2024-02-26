month = int(input("Въведете номер на месец: "))
if month in [4, 6, 9, 11]:
    print("30")
elif month == 2:
    print("28")
else:
    print("31")
