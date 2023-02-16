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
        print("Option not implemented yet.")
    elif (2 == choice):
        print("Option not implemented yet.")
    elif (3 == choice):
        print("Option not implemented yet.")
    elif (4 == choice):
        print("Option not implemented yet.")
    elif (5 == choice):
        print("Thank you for using the consultation system. Goodbye!")
        break
    else :
        print("Invalid choice. Please try again.")