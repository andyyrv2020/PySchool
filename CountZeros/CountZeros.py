n = int(input("�������� ���� �����: "))
count = 0
for _ in range(n):
    num = int(input())
    if num == 0:
        count += 1
print("���� �� ���������� �� 0:", count)
