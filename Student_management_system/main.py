import json
import os
DATA_FILE = "students.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open("DATA_FILE", "r") as f:
            return json.load(f)
    return{}

def save_data(data):
    with open("DATA_FILE", "w")as f:
        json.dump(data,f,indent=4)

def add_student(data):
    student_id = input("Enter student Id: ")
    if student_id in data:
        print("student already exist..!")
        print("------------------------------------------------------")
        return
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")
    data[student_id] = {"name": name, "age": age, "course": course}
    print("student add successfully...!")
    print("------------------------------------------------------")


def display_students(data):
    if not data: 
        print("no data found..!")
    else:
        for sid, info in data.items():
            print(f"Id: {sid}\nName: {info['name']}\nAge: {info['age']}\nCourse: {info['course']}\n\n")


def search_student(data):
    student_Id = input("enter student id: ")
    if student_Id in data:
        info = data[student_Id]
        print(f"Id: {student_Id},Name: {info['name']}, Age: {info['age']}, Course: {info['course']}")
    print("student not found..!")
    print("------------------------------------------------------")

def update_student(data):
    student_Id = input("enter student id: ")
    if student_Id in data:
        name = input("Enter student Name: ")
        age = input("Enter student age: ")
        course = input("Enter student course: ")
        data[student_Id] = {"name": name, "age": age, "course": course}
    else: 
        print("student not found..!")
        print("------------------------------------------------------")
    pass

def delete_student(data):
    student_Id = input("enter student Id: ")
    if student_Id in data:
        del data[student_Id]
        print("student delete successfully...!")
        print("------------------------------------------------------")
    print("student not found..!")
    print("------------------------------------------------------")

    pass


def main():
    data = load_data()

    while True:
        print("Student management System.....")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice : ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            display_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            update_student(data)
        elif choice == "5":
            delete_student(data)
        elif choice == "6":
            save_data(data)
            print("data saved program exit successfully.")
            print("------------------------------------------------------")
            break;
        else:
            print("wrong choice dude...")
            print("------------------------------------------------------")



if __name__ == "__main__":
    main()