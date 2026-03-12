students = {}

def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        if student_id in students:
            print("Student already exists!")
            return

        grade = float(input("Enter Grade: "))
        students[student_id] = grade
        print("Student added successfully!")

    except ValueError:
        print("Invalid input! ID must be integer and Grade must be number.")
    except Exception as e:
        print("Error:", e)


def update_grade():
    try:
        student_id = int(input("Enter Student ID to update: "))

        if student_id not in students:
            raise KeyError("Student ID not found!")

        grade = float(input("Enter new Grade: "))
        students[student_id] = grade
        print("Grade updated successfully!")

    except ValueError:
        print("Invalid grade or ID format!")
    except KeyError as e:
        print(e)


def delete_student():
    try:
        student_id = int(input("Enter Student ID to delete: "))

        if student_id not in students:
            raise KeyError("Student ID does not exist!")

        del students[student_id]
        print("Student deleted successfully!")

    except ValueError:
        print("Student ID must be a number!")
    except KeyError as e:
        print(e)


def view_students():
    try:
        if not students:
            raise Exception("No student records found!")

        print("\nStudent Records:")
        for sid, grade in students.items():
            print("Student ID:", sid, " Grade:", grade)

    except Exception as e:
        print(e)


while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Delete Student")
    print("4. View Students")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            update_grade()
        elif choice == 3:
            delete_student()
        elif choice == 4:
            view_students()
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please select 1-5.")

    except ValueError:
        print("Please enter a valid number!")