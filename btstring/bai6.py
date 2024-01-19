def tach_chu_so_chu_cai_ki_tu_dac_biet(xau):
    chu_so = ''
    chu_cai = ''
    ki_tu_dac_biet = ''

    for ky_tu in xau:
        if ky_tu.isnumeric():
            chu_so += ky_tu
        elif ky_tu.isalpha():
            chu_cai += ky_tu
        else:
            ki_tu_dac_biet += ky_tu

    return chu_so, chu_cai, ki_tu_dac_biet

xau = input("Nhập xâu ký tự: ")

chu_so, chu_cai, ki_tu_dac_biet = tach_chu_so_chu_cai_ki_tu_dac_biet(xau)

print("Chữ số trong xâu:", chu_so)
print("Chữ cái trong xâu:", chu_cai)
print("Kí tự đặc biệt trong xâu:", ki_tu_dac_biet)
