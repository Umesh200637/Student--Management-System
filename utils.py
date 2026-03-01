def greet(name):
    print("Hello", name)
    
# def add_student(name, marks):
#     with open("data.txt", "a") as file:
#         file.write(name + "," + marks + "\n")


# def view_students():
#     with open("data.txt", "r") as file:
#         data = file.readlines()
#         for line in data:
#             name, marks = line.strip().split(",")
#             print("Name:", name, "| Marks:", marks)


def add_student(name, marks):
    with open("data.txt", "a") as file:
        file.write(name + "," + marks + "\n")


def view_students():
    try:
        with open("data.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("\nNo records found.\n")
                return

            print("\n{:<20} {:<10}".format("Name", "Marks"))
            print("-" * 30)

            for line in data:
                name, marks = line.strip().split(",")
                print("{:<20} {:<10}".format(name, marks))

    except FileNotFoundError:
        print("No data file found.")


def search_student(search_name):
    found = False
    with open("data.txt", "r") as file:
        for line in file:
            name, marks = line.strip().split(",")
            if name.lower() == search_name.lower():
                print("\nStudent Found:")
                print("Name:", name)
                print("Marks:", marks)
                found = True
                break

    if not found:
        print("Student not found.")


def delete_student(delete_name):
    lines = []
    found = False

    with open("data.txt", "r") as file:
        lines = file.readlines()

    with open("data.txt", "w") as file:
        for line in lines:
            name, marks = line.strip().split(",")
            if name.lower() != delete_name.lower():
                file.write(line)
            else:
                found = True

    if found:
        print("Student deleted successfully.")
    else:
        print("Student not found.")