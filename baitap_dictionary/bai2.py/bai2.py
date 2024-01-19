# Khởi tạo danh sách sinh viên cho hai lớp và lưu chúng trong từ điển
students = {
    "class_01": [
        {"student_id": "B23DCCC8749", "first_name": "John", "last_name": "Doe", "age": 20, "gpa": 8.5, "hometown": "Ha Noi"},
        {"student_id": "B23DCCC54215", "first_name": "Jane", "last_name": "Smith", "age": 21, "gpa": 7.8, "hometown": "Ha Noi"},
        {"student_id": "B23DCSD51", "first_name": "Alice", "last_name": "Johnson", "age": 22, "gpa": 9.0, "hometown": "Thai Binh"},
        {"student_id": "B23DCCC84561", "first_name": "Bob", "last_name": "Brown", "age": 20, "gpa": 8.7, "hometown": "Thai Binh"},
    ],
    "class_02": [
        {"student_id": "B23DCCC12345", "first_name": "Charlie", "last_name": "Wilson", "age": 19, "gpa": 8.0, "hometown": "HCMC"},
        {"student_id": "B23DCCC67890", "first_name": "David", "last_name": "Lee", "age": 22, "gpa": 7.5, "hometown": "HCMC"},
        {"student_id": "B23DCCC98765", "first_name": "Eva", "last_name": "Miller", "age": 21, "gpa": 9.2, "hometown": "Da Nang"},
        {"student_id": "B23DCCC54321", "first_name": "Frank", "last_name": "Davis", "age": 20, "gpa": 8.9, "hometown": "Da Nang"},
    ]
}

# a. In ra số lượng sinh viên trong mỗi lớp
for class_name, student_list in students.items():
    print(f"Số lượng sinh viên trong {class_name}: {len(student_list)}")

# b. In ra danh sách quê quán khác nhau trong mỗi lớp
for class_name, student_list in students.items():
    hometowns = set(student["hometown"] for student in student_list)
    print(f"Quê quán khác nhau trong {class_name}: {', '.join(hometowns)}")

# c. In ra danh sách sinh viên tương ứng với mỗi quê quán
for class_name, student_list in students.items():
    hometowns = set(student["hometown"] for student in student_list)
    for hometown in hometowns:
        students_with_hometown = [student["student_id"] for student in student_list if student["hometown"] == hometown]
        print(f"{hometown} trong {class_name}: {', '.join(students_with_hometown)}")

# Tiếp tục thực hiện các yêu cầu khác tương tự.
# ... (Đoạn mã trước)

# d. Tính và in ra điểm số trung bình mỗi lớp và so sánh
for class_name, student_list in students.items():
    avg_gpa = sum(student["gpa"] for student in student_list) / len(student_list)
    print(f"Điểm trung bình của {class_name}: {avg_gpa}")

# So sánh điểm trung bình của hai lớp
avg_gpa_class_01 = sum(student["gpa"] for student in students["class_01"]) / len(students["class_01"])
avg_gpa_class_02 = sum(student["gpa"] for student in students["class_02"]) / len(students["class_02"])

if avg_gpa_class_01 > avg_gpa_class_02:
    print("Lớp 01 có điểm trung bình cao hơn.")
elif avg_gpa_class_02 > avg_gpa_class_01:
    print("Lớp 02 có điểm trung bình cao hơn.")
else:
    print("Cả hai lớp có điểm trung bình bằng nhau.")

# e. In ra sinh viên điểm cao nhất và thấp nhất mỗi lớp
def get_highest_lowest_gpa_students(student_list):
    highest_gpa_student = max(student_list, key=lambda x: x["gpa"])
    lowest_gpa_student = min(student_list, key=lambda x: x["gpa"])
    return highest_gpa_student, lowest_gpa_student

highest_lowest_class_01 = get_highest_lowest_gpa_students(students["class_01"])
highest_lowest_class_02 = get_highest_lowest_gpa_students(students["class_02"])

print(f"Sinh viên điểm cao nhất trong lớp 01: {highest_lowest_class_01[0]['first_name']} {highest_lowest_class_01[0]['last_name']}, Điểm: {highest_lowest_class_01[0]['gpa']}")
print(f"Sinh viên điểm thấp nhất trong lớp 01: {highest_lowest_class_01[1]['first_name']} {highest_lowest_class_01[1]['last_name']}, Điểm: {highest_lowest_class_01[1]['gpa']}")
print(f"Sinh viên điểm cao nhất trong lớp 02: {highest_lowest_class_02[0]['first_name']} {highest_lowest_class_02[0]['last_name']}, Điểm: {highest_lowest_class_02[0]['gpa']}")
print(f"Sinh viên điểm thấp nhất trong lớp 02: {highest_lowest_class_02[1]['first_name']} {highest_lowest_class_02[1]['last_name']}, Điểm: {highest_lowest_class_02[1]['gpa']}")

# f. Thống kê tỉ lệ (phần trăm) số sinh viên có điểm Xuất sắc (>8)
excellent_students_class_01 = [student for student in students["class_01"] if student["gpa"] > 8]
excellent_students_class_02 = [student for student in students["class_02"] if student["gpa"] > 8]

percentage_excellent_class_01 = (len(excellent_students_class_01) / len(students["class_01"])) * 100
percentage_excellent_class_02 = (len(excellent_students_class_02) / len(students["class_02"])) * 100

print(f"Tỉ lệ sinh viên Xuất sắc trong lớp 01: {percentage_excellent_class_01:.2f}%")
print(f"Tỉ lệ sinh viên Xuất sắc trong lớp 02: {percentage_excellent_class_02:.2f}%")

# In ra danh sách top 10 sinh viên xuất sắc có điểm cao nhất
top_10_excellent_students_class_01 = sorted(excellent_students_class_01, key=lambda x: x["gpa"], reverse=True)[:10]
top_10_excellent_students_class_02 = sorted(excellent_students_class_02, key=lambda x: x["gpa"], reverse=True)[:10]

print("Top 10 sinh viên Xuất sắc trong lớp 01:")
for student in top_10_excellent_students_class_01:
    print(f"{student['first_name']} {student['last_name']}, Điểm: {student['gpa']}")

print("Top 10 sinh viên Xuất sắc trong lớp 02:")
for student in top_10_excellent_students_class_02:
    print(f"{student['first_name']} {student['last_name']}, Điểm: {student['gpa']}")
