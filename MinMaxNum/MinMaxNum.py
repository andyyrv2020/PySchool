n = int(input("�������� ���� �� �������: "))
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
min_num = min(numbers)
max_num = max(numbers)
print("��������� �:", min_num)
print("���������� �:", max_num)
