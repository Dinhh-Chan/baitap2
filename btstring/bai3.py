def kiem_tra_bat_dau(xau_ky_tu, chuoi_con):
    if xau_ky_tu.startswith(chuoi_con):
        return True
    else:
        return False

xau_ky_tu = input("Nhập xâu ký tự: ")
chuoi_con = input("Nhập chuỗi con: ")

if kiem_tra_bat_dau(xau_ky_tu, chuoi_con):
    print(f"{xau_ky_tu} bắt đầu bằng {chuoi_con}")
else:
    print(f"{xau_ky_tu} không bắt đầu bằng {chuoi_con}")
