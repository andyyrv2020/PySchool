wind_speed_m_s = float(input("Въведете скорост на вятъра в m/s: "))
wind_speed_km_h = wind_speed_m_s * 3.6
if wind_speed_km_h == 0:
    print("щил")
elif 1 <= wind_speed_km_h <= 6:
    print("тих вятър")
elif 7 <= wind_speed_km_h <= 11:
    print("лек бриз")
elif 12 <= wind_speed_km_h <= 19:
    print("слаб вятър")
elif 20 <= wind_speed_km_h <= 29:
    print("умерен вятър")
elif 30 <= wind_speed_km_h <= 39:
    print("полусилен вятър")
elif 40 <= wind_speed_km_h <= 50:
    print("силен вятър")
elif 51 <= wind_speed_km_h <= 62:
    print("доста силен вятър")
elif 63 <= wind_speed_km_h <= 75:
    print("много силен вятър")
elif 76 <= wind_speed_km_h <= 87:
    print("щорм")
elif 88 <= wind_speed_km_h <= 102:
    print("силен щорм")
elif 103 <= wind_speed_km_h <= 117:
    print("жесток щорм")
else:
    print("ураган")
