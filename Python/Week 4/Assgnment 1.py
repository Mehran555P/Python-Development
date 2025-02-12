students = {
    "Ali": {"last_name": "Ahmadi", "class": "101"},
    "Sara": {"last_name": "Mohammadi", "class": "102"},
    "Reza": {"last_name": "Hosseini", "class": "103"},
    "Niloofar": {"last_name": "Karimi", "class": "201"}
}

def search_student(first_name):
    student_info = students.get(first_name)
    if student_info:
        print(f"Name: {first_name}")
        print(f"Last name: {student_info['last_name']}")
        print(f"Class: {student_info['class']}")
    else:
        print("Student not found.")


name = input("Enter student name:")
search_student(name)
