def chuan_hoa_xau(xau):
    # Loại bỏ các double space "  " và "??" trong xâu
    xau = xau.replace("  ", " ")
    xau = xau.replace("??", "?")

    # Chia xâu thành các câu
    cau = xau.split(". ")
    cau = [cau.strip() for cau in cau]

    xau_chuan_hoa = ""
    for i, cau in enumerate(cau):
        # In hoa các từ đầu câu hoặc đứng sau dấu "." hoặc "?"
        cau = cau.capitalize()
        if i > 0:
            xau_chuan_hoa += ". "
        xau_chuan_hoa += cau

    return xau_chuan_hoa

xau = input("Nhập xâu ký tự: ")
xau_chuan_hoa = chuan_hoa_xau(xau)
print("Xâu sau khi chuẩn hoá:")
print(xau_chuan_hoa)
