def chuoi_con_lon_nhat(s):
    do_dai_lon_nhat = 0
    chuoi_lon_nhat = ""

    current_length = 0
    current_substring = ""

    for char in s:
        if char.isalpha() or char.isdigit():
            current_length += 1
            current_substring += char
        else:
            if current_length >= do_dai_lon_nhat:
                do_dai_lon_nhat = current_length
                chuoi_lon_nhat = current_substring
            elif current_length == do_dai_lon_nhat:
                chuoi_lon_nhat = current_substring
            current_length = 0
            current_substring = ""
    if current_length > do_dai_lon_nhat:
        chuoi_lon_nhat = current_substring
    elif current_length == do_dai_lon_nhat:
        chuoi_lon_nhat = current_substring

    return chuoi_lon_nhat
chuoi = input()

ket_qua = chuoi_con_lon_nhat(chuoi)
print(ket_qua)
