price_vegetables_per_kg = float(input("����, �������� ���� �� �������� ���������: "))
price_fruits_per_kg = float(input("����, �������� ���� �� �������� �������: "))
kg_vegetables = int(input("����, �������� ���� ��������� ���������: "))
kg_fruits = int(input("����, �������� ���� ��������� �������: "))
total_income_lv = price_vegetables_per_kg * kg_vegetables + price_fruits_per_kg * kg_fruits
total_income_euro = total_income_lv / 1.94
print(round(total_income_euro, 2))

