price_vegetables_per_kg = float(input("Моля, въведете цена за килограм зеленчуци: "))
price_fruits_per_kg = float(input("Моля, въведете цена за килограм плодове: "))
kg_vegetables = int(input("Моля, въведете общо килограми зеленчуци: "))
kg_fruits = int(input("Моля, въведете общо килограми плодове: "))
total_income_lv = price_vegetables_per_kg * kg_vegetables + price_fruits_per_kg * kg_fruits
total_income_euro = total_income_lv / 1.94
print(round(total_income_euro, 2))

