# from utils import greet
# from utils import add_student, view_students

# name = input("Enter your name: ")
# greet(name)


# while True:
#     print("\n--- Student Management System ---")
#     print("1. Add Student")
#     print("2. View Students")
#     print("3. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         name = input("Enter student name: ")
#         marks = input("Enter marks: ")
#         add_student(name, marks)

#     elif choice == "2":
#         view_students()

#     elif choice == "3":
#         print("Exiting...")
#         break

#     else:
#         print("Invalid choice!")

from utils import add_student, view_students, search_student, delete_student

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        add_student(name, marks)

    elif choice == "2":
        view_students()

    elif choice == "3":
        name = input("Enter name to search: ")
        search_student(name)

    elif choice == "4":
        name = input("Enter name to delete: ")
        delete_student(name)

    elif choice == "5":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Try again.")

print("umesh")
