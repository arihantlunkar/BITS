from patientRecord import PatientRecord

# TODO : handle duplicate entry
#TODO: what if DLL and Heap empty
#TODO: Bug in MaxHeap

patientRecordObj = PatientRecord()

def registerPatient(name, age):
    patientRecordObj.add_patient(name, age)


# infinite while loop
print("Welcome to Dr. Kumar's hospital for senior citizens!")

while True:
    print("Choose a +ve integer from below menu items :-")
    print("1. Import patients from file")
    print("2. Enter new patient information")
    print("3. Display next patient in line")
    print("4. Output current patient waiting list")
    print("5. Exit")

    # take input from user
    choice = input("Enter your choice (1-5):")

    if (0 == choice.isdigit()):
        print("Invalid choice")
        continue

    choice = int(choice)

    if (1 == choice):
        with open("input.txt") as f:
            for line in f:
                name, age = line.strip().split(", ")
                age = age.strip()
                if 0 == age.isdigit() or int(age) <= 0:
                    continue
                registerPatient(name, int(age))
    elif (2 == choice):
        name = input("Enter patient name: ")
        age = 0
        while True:
            age = input("Enter patient age: ")
            if 0 == age.isdigit() or int(age) <= 0:
                print("Invalid age!")
                continue
            break
        registerPatient(name, int(age))
    elif (3 == choice):
        print("Next patient is ", patientRecordObj.next_patient().name)
    elif (4 == choice):
        patientRecordObj.print_list()
    elif (5 == choice):
        print("Thank you for using the consultation system. Goodbye!")
        break
    else :
        print("Invalid choice. Please try again.")