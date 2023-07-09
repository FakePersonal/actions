sections = open("section.txt", "w")
sections.close()

while True:
    student = input("Enter the student name,ID,level: ")

    result = ""
    studentsDetails = []
    for letters in student:
        if letters == ",":
            studentsDetails.append(result)
            result = ""
        else:
            result += letters
    studentsDetails.append(result)
    break

DATABASE = {studentsDetails[0]: studentsDetails}

while True:
    userInput = input("\t\t**User Menu**\n1-view all sections\n2-search by CRN\n\t\tEnter the mode you need or 'quit' "
                      "to exit: ")

    if userInput.isdigit():
        if userInput == "1":
            for i in range(len(DATABASE)):
                print("%20d" % i)
        elif userInput == "2":
            CRN = input("enter the CRN : ")
            for keys in DATABASE:
                if keys == CRN:
                    print(DATABASE)
                else:
                    print("CRN is not available!")
    elif userInput == "quit":
        break
    else:
        print("Error:please enter a valued input!")
