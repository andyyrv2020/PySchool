wind_speed_m_s = float(input("�������� ������� �� ������ � m/s: "))
wind_speed_km_h = wind_speed_m_s * 3.6
if wind_speed_km_h == 0:
    print("���")
elif 1 <= wind_speed_km_h <= 6:
    print("��� �����")
elif 7 <= wind_speed_km_h <= 11:
    print("��� ����")
elif 12 <= wind_speed_km_h <= 19:
    print("���� �����")
elif 20 <= wind_speed_km_h <= 29:
    print("������ �����")
elif 30 <= wind_speed_km_h <= 39:
    print("��������� �����")
elif 40 <= wind_speed_km_h <= 50:
    print("����� �����")
elif 51 <= wind_speed_km_h <= 62:
    print("����� ����� �����")
elif 63 <= wind_speed_km_h <= 75:
    print("����� ����� �����")
elif 76 <= wind_speed_km_h <= 87:
    print("����")
elif 88 <= wind_speed_km_h <= 102:
    print("����� ����")
elif 103 <= wind_speed_km_h <= 117:
    print("������ ����")
else:
    print("������")
