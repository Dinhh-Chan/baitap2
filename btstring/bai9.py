# Nhập vào chuỗi từ người dùng
input_string = input("Nhập vào chuỗi: ")

# Kiểm tra xem chuỗi kết thúc bằng từ "end" hay không
if input_string.endswith("end"):
    print("Chuỗi kết thúc bằng từ 'end'.")

# Kiểm tra xem từ "is" có xuất hiện trong chuỗi và đếm số lần xuất hiện
count_is = input_string.count("is")
if count_is > 0:
    print(f"Từ 'is' xuất hiện đầu tiên tại vị trí {input_string.find('is')} và xuất hiện {count_is} lần trong chuỗi.")

# Thay thế các từ "is" bằng từ "are" trong chuỗi
modified_string = input_string.replace("is", "are")
print("Chuỗi sau khi thay thế 'is' bằng 'are':")
print(modified_string)
