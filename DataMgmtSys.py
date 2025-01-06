# DataMgmtSys.py


def Fill_Student():
    try:
        StuName = input("Enter Student Name: ")
        StuRollNo = input("Enter Student's Roll Number: ")
        StuAge = input("Enter Student's Age: ")
        StuCollege = input("Enter College name: ")

        with open("StudentData.txt", "a") as file:
            file.write(StuName + "\t|" + StuCollege + "\t\t|" + StuRollNo + "\t\t|" + StuAge + "\t\t|\n")
    except ValueError:
        print("Enter valid information.")
    except IOError as e:
        print(f"Error writing to file: {e}")


def View_Student():
    with open("StudentData.txt", "r") as file:
        data = file.read()
        print(data)


def Fill_Faculty():
    try:
        FName = str(input("Enter Faculty Name: "))
        FSub = str(input("Enter Faculty's Subject: "))
        FAge = int(input("Enter Faculty's Age: "))
        FCollege = str(input("Enter College name: "))
        with open("FacultyData.txt", "a") as file:
            file.write(FName + "\t\t|" + FSub + "\t\t|" + str(FAge) + "\t\t|" + FCollege + "\t\t|\n")
    except ValueError:
        print("Enter valid information.")
    except IOError as e:
        print(f"Error writing to file: {e}")


def View_Faulty():
    with open("FacultyData.txt", "r") as file:
        data = file.read()
        print(data)


# Main Program
Loop = True
while Loop:
    print("\nSelect any of the one option available :")
    print("1\tFill Student Information ")
    print("2\tView all Student Information ")
    print("3\tFill Faculty Information ")
    print("4\tView Faculty Information ")
    print("5\tTo Exit")

    try:
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                Fill_Student()
            case 2:
                View_Student()
            case 3:
                Fill_Faculty()
            case 4:
                View_Faulty()
            case 5:
                print("Thank You!")
                Loop = False
            case _:
                print("Provide choice in range(1, 5)")
    except ValueError:
        print("Invalid type of choice, only numbers allowed to write.")
