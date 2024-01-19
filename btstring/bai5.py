def tach_tu_theo_ky_tu(cau, ky_tu_tach):
    tu = cau.split(ky_tu_tach)
    return tu

cau = input("Nhập một câu: ")
ky_tu_tach = input("Nhập ký tự để tách từ: ")

tu_tach = tach_tu_theo_ky_tu(cau, ky_tu_tach)

print("Các từ sau khi tách:")
for tu in tu_tach:
    print(tu)
