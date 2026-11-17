#SESSION 3
courses=[ "Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Biology I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics" ]
print(courses)
sorted_units=sorted(courses)
print(sorted_units)
reverse_sorted_courses = sorted(courses, reverse=True)
print(reverse_sorted_courses) 
courses.reverse()
print(courses)
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)
courses=[ "Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Linear Algebra", "Physics I", "Chemistry I", "Biology I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics" ]
print(courses)
sorted_courses=sorted(courses)
print(sorted_courses)
sorted_courses=sorted(courses)
print("The following courses are available for expression of interest if the students meet the prerequisites:")
for course in sorted_courses:
    print(course)
withdrawn_course=courses[3]
courses[4]="Physics I"
new_course=courses[4]
print(f"\nThe course '{withdrawn_course}' is no longer available.")
print(f"It has been replaced with a new course: '{new_course}'.")
units=["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Environmental Science", "Physics I", "Chemistry I", "Biology I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics"]
print(courses)
courses.insert(0,"Software Engineering")
courses.insert(7,"Artificial Intelligence")
courses.append("Game Development")
for course in units:
    print(course)
courses=["Introduction to Programming", "Calculus I", "Data Structures and Algorithms", "Environmental Science", "Physics I", "Chemistry I", "Biology I", "Microeconomics", "Macroeconomics", "Psychology I", "History I", "English Composition I", "Introduction to Philosophy", "Calculus II", "Discrete Mathematics"]
print(courses)
print("The following courses are no longer available due to technical and room availability issues:")
removed_course_1=units.pop(1)
removed_course_2=units.pop(9)
removed_course_3=units.pop(5)
removed_course_4 = units.pop(3)
unavailable_courses=[removed_course_1,removed_course_2,removed_course_3, removed_course_4]
print("The following courses are no longer available:")
for course in unavailable_courses:
    print(f"- {course}")
print("\nUpdated list of available courses:")
for course in courses:
    print(course)
courses = [ (1, "Introduction to Programming"), (2, "Calculus I"), (3, "Data Structures and Algorithms"), (4, "Linear Algebra"), (5, "Physics I"), (6, "Chemistry I"), (7, "Biology I"), (8, "Microeconomics"), (9, "Macroeconomics"), (10, "Psychology I"), (11, "History I"), (12, "English Composition I"), (13, "Introduction to Philosophy"), (14, "Calculus II"), (15, "Discrete Mathematics") ]
course_names = []
for course in courses:
    course_id, course_name = course
    course_names.append(course_name)
print("List of Course Names:")
for name in course_names:
    print(name)
course_data=[ (1, "Introduction to Programming"), (2, "Calculus I"), (3, "Data Structures and Algorithms"), (4, "Linear Algebra"), (5, "Physics I"), (6, "Chemistry I"), (7, "Biology I"), (8, "Microeconomics"), (9, "Macroeconomics"), (10, "Psychology I"), (11, "History I"), (12, "English Composition I"), (13, "Introduction to Philosophy"), (14, "Calculus II"), (15, "Discrete Mathematics") ]
course_names = []
for course_id, course_name in course_data:
    course_names.append(course_name)
print("Course Information:")
for name in course_names:
    	print(f"- {name}")

#SESSION 4
courses=[[1, "Computer Science"], [2, "Mathematics"], [3, "Computer Science"], [4, "Mathematics"], [5, "Physics"], [6, "Chemistry"], [7, "Biology"], [8, "Economics"], [9, "Economics"], [10, "Psychology"], [11, "History"], [12, "English"], [13, "Philosophy"], [14, "Mathematics"], [15, "Computer Science"]]
while True:
    num = input("Enter course ID to search for its department, 'quit' or '0' to stop: ")
    if num.lower() == 'quit' or num == '0':
        print("Exiting the program...")
        break
    if num.isdigit():
        num = int(num)
        found = False
        for course in courses:
            if course[0] == num:
                print(f"Course with ID {num} is in the {course[1]} department.")
                found = True
                break
        if not found:
            print(f"Course with ID {num} not found.")
    else:
        print("Please enter a valid course ID, 'quit', or '0'.")

courses=[ [1, "Computer Science"], [2, "Mathematics"], [3, "Computer Science"], [4, "Mathematics"], [5, "Physics"], [6, "Chemistry"], [7, "Biology"], [8, "Economics"], [9, "Economics"], [10, "Psychology"], [11, "History"], [12, "English"], [13, "Philosophy"], [14, "Mathematics"], [15, "Computer Science"] ]
courses = [
    [1, "Computer Science"], [2, "Mathematics"], [3, "Computer Science"],
    [4, "Mathematics"], [5, "Physics"], [6, "Chemistry"],
    [7, "Biology"], [8, "Economics"], [9, "Economics"],
    [10, "Psychology"], [11, "History"], [12, "English"],
    [13, "Philosophy"], [14, "Mathematics"], [15, "Computer Science"]
]
 
while True:
    num = input("Enter course ID to search for its department, 'quit' or '0' to stop: ")
   
    if num.lower() == 'quit' or num == '0':
        print("Exiting the program...")
        break
   
    if num.isdigit():
        num = int(num)
        found = False
 
        for course in courses:
            if course[0] == num:
                print(f"Course ID {num} is in the {course[1]} department.")
                found = True
                break
        if found:
            break
        else:
            print(f"Course with ID {num} not found.")
    else:
        print("Please enter a valid course ID, 'quit', or '0'.")

courses = [ [1, "Computer Science"], [2, "Mathematics"], [3, "Computer Science"], [4, "Mathematics"], [5, "Physics"], [6, "Chemistry"], [7, "Biology"], [8, "Economics"], [9, "Economics"], [10, "Psychology"], [11, "History"], [12, "English"], [13, "Philosophy"], [14, "Mathematics"], [15, "Computer Science"] ]
while True:
    num = input("Enter course ID to search for its department, 'quit' or '0' to stop: ")
    if num == 'quit' or num == '0':
        print("Exiting the program...")
        break
    elif num.isdigit():
        num = int(num)
        if 1 <= num <= 15:
            for course in courses:
                if course[0] == num:
                    print(f"Course ID {num} is in the {course[1]} department.")
                    break
        else:
            print("Course ID is out of range (1-15), try again.")
    else:
        print("Invalid input. Please enter a valid course ID, 'quit', or '0'.")

courses=[ [1, "Computer Science", "Engineering", ["Mathematics", "Physics"]], [2, "Mathematics", "Science", ["None"]], [3, "Physics", "Science", ["Mathematics"]], [4, "Chemistry", "Science", ["None"]], [5, "Biology", "Science", ["Chemistry"]], [6, "Economics", "Arts", ["None"]], [7, "Psychology", "Arts", ["None"]], [8, "History", "Arts", ["None"]], [9, "English", "Arts", ["None"]], [10, "Philosophy", "Arts", ["None"]], [11, "Law", "Law", ["None"]], [12, "Medicine", "Health", ["Biology", "Chemistry"]], [13, "Engineering", "Engineering", ["Mathematics", "Physics"]], [14, "Architecture", "Engineering", ["Mathematics", "Physics"]], [15, "Sociology", "Social Sciences", ["None"]] ]
def get_course_info(course_id):
    for course in courses:
        if course[0] == course_id:
            return course
    return None
while True:
    num = input("Enter course ID to retrieve course information, or 'quit' or '0' to exit: ")
    if num.lower() == 'quit' or num == '0':
        print("Exiting the program...")
        break
    if num.isdigit():
        course_id = int(num)
        if 1 <= course_id <= 15:
            course_info = get_course_info(course_id)
            if course_info:
                print(f"Course ID: {course_info[0]}")
                print(f"Course Name: {course_info[1]}")
                print(f"Department: {course_info[2]}")
                print(f"Prerequisites: {', '.join(course_info[3])}")
                break
            else:
                print(f"Course with ID {course_id} not found. Please try again.")
        else:
            print("Course ID is out of range (1-15), try again.")
    else:
        print("Invalid input! Please enter a valid course ID or 'quit' or '0' to exit.")

courses=[1, "Computer Science", "Engineering",["Mathematics", "Physics"]], [2, "Mathematics", "Science", ["None"]], [3, "Physics", "Science", ["Mathematics"]], [4, "Chemistry", "Science", ["None"]], [5, "Biology", "Science", ["Chemistry"]], [6, "Economics", "Arts", ["None"]], [7, "Psychology", "Arts", ["None"]], [8, "History", "Arts", ["None"]], [9, "English", "Arts", ["None"]], [10, "Philosophy", "Arts", ["None"]], [11, "Law", "Law", ["None"]], [12, "Medicine", "Health", ["Biology", "Chemistry"]], [13, "Engineering", "Engineering", ["Mathematics", "Physics"]], [14, "Architecture", "Engineering", ["Mathematics", "Physics"]], [15, "Sociology", "Social Sciences", ["None"]] 
while True:
    user_input = input("Enter course ID (1-15) to search, 'quit' or '0' to exit: ")
    if user_input == "quit" or user_input == "0":
        print("Exiting the program...")
        break
    if user_input.isdigit():
        course_id = int(user_input)
    if 1 <= course_id <= 15:
            course_found = False
            for course in courses:
                if course[0] == course_id:
                    print(f"Course ID {course_id} is {course[1]} in the {course[2]} department.")
                    print(f"Prerequisites: {course[3]}")
                    course_found = True
                    break
            if not course_found:
                print(f"Course with ID {course_id} not found.")
    else:
         print("Course ID is out of range (1-15), try again.")
else:
   print("Invalid input. Please enter a valid course ID (1-15) or 'quit' or '0' to exit.")
