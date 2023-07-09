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
