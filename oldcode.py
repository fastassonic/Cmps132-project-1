students = {"Stephanie": [], "David": [], "Terry": [],"Sherry":[],"Sylvia":[]}
courses = {"Test class 1": "Test teacher1", "Test class 2": "Test teacher 2", "Test class 3": "Test teacher 3","Test class 4": "Test teacher 4", "Test class 5":"Test teacher"}
avaliablebooks = {"Harry potter": ["j.k. Rowling", 3], "Lord of the rights":["J.r.r Tolkien",2], "Lord of the flies":["William Golding",7],"Stacy's book":["Stacy",10],"To kill a mocking bird": ["F. Scott Fitzgerald",80]}
takenbooks = []

def GradeToLetter(num):
    if num >= 95:
        return ("A")
    elif num >= 86:
        return ("B")
    elif num >= 76:
        return ("C")
    elif num >= 61:
        return ("D")
    else:
        return ("F")

def findtopandlowestforclass(Temp_class):
    topint = 0
    topstudent = ""
    bottomint = float('inf')
    bottomstudent = ""
    for i in students.keys():
        for x in students[i]:
            if x[0] == Temp_class:
                if x[1] > topint:
                    topint = x[1]
                    topstudent = i
                if x[1] < bottomint:
                    bottomint = x[1]
                    bottomstudent = i

    return [[topstudent, topint], [bottomstudent, bottomint]]

def add_student(i=1):
    name = "Add-Student"

    while name == "Add-Student":
        name = input("What's the " + str(i + 1) + " student's name. (Note cannot name the student \"Add-Student\")")
    students.update({name: []})


def add_class():
    # Note: Does not add more swagger
    coursename = input("What's the courses name")
    courseinstructor = input("Whom teaches " + coursename)
    courses.update({coursename: courseinstructor})

def add_book(i=1):
    print("Book number " + str(i + 1))
    bookname = input("What's the books name?: ")
    bookauthor = input("Who wrote " + bookname + ": ")
    booknumber = ""

    while not booknumber.isdigit():
        booknumber = input("How many copies: ")
    booknumber = int(booknumber)

    # Instead of manually keeping tracks of how many copies
    if booknumber < 1:
        print("Invalid number. Only putting in a single copy ")
        booknumber = 1

    avaliablebooks.update({bookname: [bookauthor, booknumber]})


def selection_from_dict(temp_dict):
    temp_list = []
    classchoice = ""
    for key in temp_dict.keys():
        temp_list.append(key)

    for i in range(len(temp_list)):
        print("(" + str(i) + "):" + temp_list[i])
    validchoice = False

    while not validchoice:
        classchoice = ""

        while not classchoice.isdigit():
            classchoice = input("Please enter the number next to the course:")

        if int(classchoice) < len(courses) and int(classchoice) >= 0:
            validchoice = True

    return (temp_list[int(classchoice)])
#God i dislike polymorphism 
def selection_from_list(temp_list, bookstoreflag=False):
    if bookstoreflag == False:
        for i in range(len(temp_list)):
            print("(" + str(i) + "):" + temp_list[i][0])
    else:
        for i in range(len(temp_list)):
            print("(" + str(i) + "):" + temp_list[i][0] + " Checked out by " + temp_list[i][2] + " To be returned by " +
                  temp_list[i][1])

    validchoice = False
    classchoice = -1

    while not validchoice:
        classchoice = ""
        while not classchoice.isdigit():
            classchoice = input("Please enter the number next to the course:")
        if int(classchoice) < len(courses) and int(classchoice) >= 0:
            validchoice = True

    return (int(classchoice))




for i in range(1):

    add_student(i)




for i in range(1):

    add_class()


for i in range(1):

    add_book(i)



def search_student (name):
    # Searching for student
    if name.lower() == "add-student":
        add_student()

    for i in students.keys():
        if i.lower() == name.lower():
            choice = i
            return choice
    return "None"

def display_student_record(numerical = True):
    for i in students[choice]:
        if numerical:
            print(i[0] + ": " + str(i[1]))
        else:
            print(i[0] + ": " + GradeToLetter(i[1]))

def editing ():
    print("What course are you adding to " + choice + "'s roster ")
    classchoice = selection_from_dict(courses)
    basegrade = ""
    while not basegrade.isdigit():
        basegrade = input("What's their base grade for this class? ")
    basegrade = int(basegrade)
    baseattendence = ""

    while not baseattendence.isdigit():
        baseattendence = input("And what percentage of the time did they show up? (Note: Do not include the % ) ")

    baseattendence = int(baseattendence)
    if baseattendence < 95:
        basegrade -= 5
    students[choice].append([classchoice, basegrade, baseattendence])

def editing_grades():
    print("What course are you changing for " + choice + "'s roster")
    classchoice = selection_from_list(students[choice])
    basegrade = input("What's their new grade for this class? ")
    baseattendence = input("Whats their base attendence for this class? ")
    basegrade = int(basegrade)

    if students[choice][classchoice][2] < 95 and int(baseattendence) > 95:
        basegrade += 5
    if students[choice][classchoice][2] > 95 and int(baseattendence) < 95:
        basegrade -= 5
    students[choice][classchoice][2] = int(baseattendence)
    students[choice][classchoice][1] = int(basegrade)

def deleting_course():
    print("What course are you dropping for " + students[choice][0] + "'s roster")
    classchoice = selection_from_list(students[choice])
    students[choice].pop(classchoice)

def list_courses():
    for i in courses:
        print(i)

def drop_courses():
    classchoice = selection_from_dict(courses)
    courses.pop(classchoice)

def show_teacher():
    classchoice = selection_from_dict(courses)
    print(courses[classchoice])

def top_and_bottom():
    classchoice = selection_from_dict(courses)
    temp_lists = findtopandlowestforclass(classchoice)
    print(f"The Top performer was {temp_lists[0][0]} who scored {temp_lists[0][1]}")
    print(f"The Bottom perfomer was {temp_lists[1][0]} who scored {temp_lists[1][1]}")


def list_book():
    for i in avaliablebooks.keys():
        print(str(avaliablebooks[i][1]) + " copies of " + i + " by " + avaliablebooks[i][0])


def borrow_books():
    userchoice = selection_from_dict(avaliablebooks)

    if avaliablebooks[userchoice][1] > 0:
        avaliablebooks[userchoice][1] -= 1
        responsiblestudent = input("Who is checking this out? ")
        returndate = input("When are you returning this? ")
        takenbooks.append((userchoice, returndate, responsiblestudent))
        print("You have checked out this book! ")

    else:
        print("I'm sorry but we don't have that in stock")

def return_books():
    if len(takenbooks) != 0:
        booktobereturned = selection_from_list(takenbooks, True)
        avaliablebooks[takenbooks[booktobereturned][0]][1] += 1
        takenbooks.pop(booktobereturned)

    else:
        print("Every book is returned!")
def particular_book():
    print("Which book do you want to see the author of ")
    userchoice = selection_from_dict(avaliablebooks)
    print(userchoice + " by " + avaliablebooks[userchoice][0])

def title_and_date_of_taken_book():
    for i in takenbooks:
        print(i[0] + " Checked out by " + i[2] + " To be returned by  " + i[1])


done = False
while not done:
    access = input("Access a menu: (0 for students, 1 for courses, 2 for books, and 3 to be done.)")
    if access == '0':
        print("valid students")
        for i in students.keys():
            print(i)


        name = input("Which student are you searching for? (Enter Add-Student to add new students) ")

        choice = search_student(name)
        # Searching for student
        """if name.lower() == "add-student":
            add_student()

        for i in students.keys():

            if i.lower() == name.lower():
                choice = i"""
        if choice != 'None':
            function = input("What would you like to do? (1 for displaying student records, 2 for editing, 3 for editing grades, or 4 for deleting a course, 5 for deleting entire student,and 6 for showcasing final grades)")

            if function == '1':
                display_student_record()

            elif function == '2':
                editing()

            elif function == '3':
                editing_grades()

            elif function == '4':
                deleting_course()

            elif function == '5':
                display_student_record(False)
            elif function == '6':
                if input("Are you sure? enter TRUE in all caps if you are") == "TRUE":
                    students.pop(choice)
                else:
                    print("Canceled deletion")

    elif access == '1':
        function = input("(0 to list courses, 1 to add courses, 2 to drop courses, 3 to show attached teacher to course, or 4 to show the top and bottom students in the class)")

        if function == '0':
            list_courses()

        elif function == '1':
            add_class()

        elif function == '2':
            drop_courses()

        elif function == '3':
            show_teacher()

        elif function == '4':
            top_and_bottom()

    elif access == "2":

        function = input("(0 to list books, 1 to borrow books, 2 to return books, 3 to look at a particular book, 4 to list books that have been taken out and when they're going")

        if function == '0':
            list_book()

        if function == "1":
            borrow_books()

        if function == "2":
            return_books()

        if function == "3":
            particular_book()

        if function == '4':
            title_and_date_of_taken_book()

    elif access == "3":
        done = True

print(students)
print(courses)
print(avaliablebooks)
print(takenbooks)