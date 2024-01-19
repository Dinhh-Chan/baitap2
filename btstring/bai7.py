def thay_the_tu(xau, tu_cu, tu_moi):
    xau_moi = xau.replace(tu_cu, tu_moi)
    return xau_moi

xau = input("Nhập xâu ký tự: ")
tu_cu = input("Nhập từ cần thay thế: ")
tu_moi = input("Nhập từ thay thế: ")

xau_moi = thay_the_tu(xau, tu_cu, tu_moi)

print("Xâu sau khi thay thế:")
print(xau_moi)
