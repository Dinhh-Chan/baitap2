#Nhap vao mot chuoi ky tu. Kiem tra chuoi co thoa man dieu kien sau khong:
str = input()
#chi chua so 0-9
def is_number(str):
    for i in range(0, len(str)):
        if str[i].isnumeric() == False:
            return "NO"
        return "YES"
print(is_number(str))


#chi chua ky tu alpabet
def is_alphabet(str):
    for i in range(0, len(str)):
        if str[i].isalpha() == False:
            return "NO"
        return "YES"
print(is_alphabet(str))
#chi chua so va ky tu alphabet
def is_alphanumeric(str):
    for i in range(0, len(str)):
        if str[i].isalnum() == False:
            return "NO"
        return "YES"
print(is_alphanumeric(str))
#tat ca ky tu deu viet hoa
def is_upper(str):
    for i in range(0, len(str)):
        if str[i].isupper() == False:
            return "NO"
        return "YES"
print(is_upper(str))
#tat ca ky tu deu viet thuong
def is_lower(str):
    for i in range(0, len(str)):
        if str[i].islower() == False:
            return "NO"
        return "YES"
print(is_lower(str))
