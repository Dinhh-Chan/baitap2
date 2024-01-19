class Student:
    def __init__(self, student_id, first_name, last_name, age, gpa, hometown):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gpa = gpa
        self.hometown = hometown

# Khởi tạo danh sách sinh viên cho hai lớp
class_01 = [
    Student("B23DCCC8749", "John", "Doe", 20, 8.5, "Ha Noi"),
    Student("B23DCCC54215", "Jane", "Smith", 21, 7.8, "Ha Noi"),
    Student("B23DCSD51", "Alice", "Johnson", 22, 9.0, "Thai Binh"),
    Student("B23DCCC84561", "Bob", "Brown", 20, 8.7, "Thai Binh"),
]

class_02 = [
    Student("B23DCCC12345", "Charlie", "Wilson", 19, 8.0, "HCMC"),
    Student("B23DCCC67890", "David", "Lee", 22, 7.5, "HCMC"),
    Student("B23DCCC98765", "Eva", "Miller", 21, 9.2, "Da Nang"),
    Student("B23DCCC54321", "Frank", "Davis", 20, 8.9, "Da Nang"),
]

# a. In ra số lượng sinh viên trong mỗi lớp
print(f"Số lượng sinh viên trong lớp 01: {len(class_01)}")
print(f"Số lượng sinh viên trong lớp 02: {len(class_02)}")

# b. In ra danh sách quê quán khác nhau trong mỗi lớp
hometowns_class_01 = set(student.hometown for student in class_01)
hometowns_class_02 = set(student.hometown for student in class_02)
print(f"Quê quán khác nhau trong lớp 01: {', '.join(hometowns_class_01)}")
print(f"Quê quán khác nhau trong lớp 02: {', '.join(hometowns_class_02)}")

# c. In ra danh sách sinh viên tương ứng với mỗi quê quán
for hometown in hometowns_class_01:
    students_with_hometown = [student.student_id for student in class_01 if student.hometown == hometown]
    print(f"{hometown}: {', '.join(students_with_hometown)}")

for hometown in hometowns_class_02:
    students_with_hometown = [student.student_id for student in class_02 if student.hometown == hometown]
    print(f"{hometown}: {', '.join(students_with_hometown)}")

# d. Tính và in ra điểm số trung bình mỗi lớp và so sánh
avg_gpa_class_01 = sum(student.gpa for student in class_01) / len(class_01)
avg_gpa_class_02 = sum(student.gpa for student in class_02) / len(class_02)

print(f"Điểm trung bình của lớp 01: {avg_gpa_class_01}")
print(f"Điểm trung bình của lớp 02: {avg_gpa_class_02}")

if avg_gpa_class_01 > avg_gpa_class_02:
    print("Lớp 01 có điểm trung bình cao hơn.")
elif avg_gpa_class_02 > avg_gpa_class_01:
    print("Lớp 02 có điểm trung bình cao hơn.")
else:
    print("Cả hai lớp có điểm trung bình bằng nhau.")

# e. In ra sinh viên điểm cao nhất và thấp nhất mỗi lớp
def get_highest_lowest_gpa_students(student_list):
    highest_gpa_student = max(student_list, key=lambda x: x.gpa)
    lowest_gpa_student = min(student_list, key=lambda x: x.gpa)
    return highest_gpa_student, lowest_gpa_student

highest_gpa_class_01, lowest_gpa_class_01 = get_highest_lowest_gpa_students(class_01)
highest_gpa_class_02, lowest_gpa_class_02 = get_highest_lowest_gpa_students(class_02)

print(f"Sinh viên điểm cao nhất trong lớp 01: {highest_gpa_class_01.first_name} {highest_gpa_class_01.last_name}, Điểm: {highest_gpa_class_01.gpa}")
print(f"Sinh viên điểm thấp nhất trong lớp 01: {lowest_gpa_class_01.first_name} {lowest_gpa_class_01.last_name}, Điểm: {lowest_gpa_class_01.gpa}")
print(f"Sinh viên điểm cao nhất trong lớp 02: {highest_gpa_class_02.first_name} {highest_gpa_class_02.last_name}, Điểm: {highest_gpa_class_02.gpa}")
print(f"Sinh viên điểm thấp nhất trong lớp 02: {lowest_gpa_class_02.first_name} {lowest_gpa_class_02.last_name}, Điểm: {lowest_gpa_class_02.gpa}")

# f. Thống kê tỉ lệ (phần trăm) số sinh viên có điểm Xuất sắc (>8)
excellent_students_class_01 = [student for student in class_01 if student.gpa > 8]
excellent_students_class_02 = [student for student in class_02 if student.gpa > 8]

percentage_excellent_class_01 = (len(excellent_students_class_01) / len(class_01)) * 100
percentage_excellent_class_02 = (len(excellent_students_class_02) / len(class_02)) * 100

print(f"Tỉ lệ sinh viên Xuất sắc trong lớp 01: {percentage_excellent_class_01:.2f}%")
print(f"Tỉ lệ sinh viên Xuất sắc trong lớp 02: {percentage_excellent_class_02:.2f}%")

# In ra danh sách top 10 sinh viên xuất sắc có điểm cao nhất
top_10_excellent_students_class_01 = sorted(excellent_students_class_01, key=lambda x: x.gpa, reverse=True)[:10]
top_10_excellent_students_class_02 = sorted(excellent_students_class_02, key=lambda x: x.gpa, reverse=True)[:10]

print("Top 10 sinh viên Xuất sắc trong lớp")
