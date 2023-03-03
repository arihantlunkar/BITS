from patientRecord import PatientRecord
from os.path import exists as file_exists

patientRecordObj = PatientRecord()

# This function registers the name and age of the patient entering the hospital and assigns 
# them an ID that is returned to the calling function. When the program is executed for the first time, 
# the patient details are loaded from an input file. This is analogous to the list of patients present at 
# the hospital before the registration counter opens. Thereafter, new patients will be input with the 
# help of menu options and console-based input. 
def registerPatient(name, age):
    return patientRecordObj.registerPatient(name, age)

# This function prints the patient_ID and name of the patient that is next in line to meet the 
# doctor. This function is called either through a menu option of every time a new patient registers and 
# the patient is added to the queue. 
def nextPatient():
    patient = patientRecordObj.nextPatient()
    if patient is None:
        print("No more patient in the consultation queue")
    else:
        print("Next patient for consultation is", patient)

# This function removes the patient ID from the queue that has consulted the doctor and 
# updates the queue. The function is called from the nextPatient function itself after the next patients 
# name is displayed. 
def displayQueue():  
    patientRecordObj.displayQueue()

def importPatientsFromFile():
    while True:
        print("Enter file name to proceed or back to go to main menu:")
        text = input()
        file = "input.txt"
        # If input is back go back to main menu
        if "back" in text:
            break
        elif file_exists(text):
            file = text
        if file_exists(file):
            if file == "input.txt" and len(text) == 0:
                print("Importing from input.txt as discarding empty file name")
            elif file == "input.txt":
                print("Importing from input.txt as", text, "does not exist")
            else:
                print("Importing from", text, "as it takes precedence over input.txt")
            with open(file) as f:
                count = 0
                for line in f:
                    name, age = line.strip().split(", ")
                    age = age.strip()
                    if 0 == age.isdigit() or int(age) <= 0:
                        continue
                    registerPatient(name, int(age))
                    count = count + 1
                print("Imported", count, "patients from", file)
            break
        # Else throw error
        else:
            print("File does not exist or invalid input")

def registerNewPatient():
    while True:
        name = input("Enter patient name: ")
        if len(name) == 0:
            print("Invalid name")
            continue
        age = 0
        while True:
            age = input("Enter patient age: ")
            if 0 == age.isdigit() or int(age) <= 0:
                print("Invalid age")
                continue
            break
        index = registerPatient(name, int(age))
        print("Patient",name, "added to the queue, current position is", index)
        break

# infinite while loop
print("Welcome to Dr. Kumar's hospital for senior citizens.")

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
        importPatientsFromFile()
    elif (2 == choice):
        registerNewPatient()
    elif (3 == choice):
        nextPatient()
    elif (4 == choice):
        displayQueue()
    elif (5 == choice):
        print("Thank you for using the consultation system. Goodbye.")
        break
    else :
        print("Invalid choice. Please try again.")