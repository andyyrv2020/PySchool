temperature = float(input("Въведете температура на водата: "))
if temperature <= 0:
    print("твърдо")
elif 0 < temperature < 100:
    print("течно")
else:
    print("газообразно")
