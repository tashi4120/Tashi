student_name={'Alice Smith','Bob Johnson','Charlie Brown','David Lee','Emily Davis','Frank Wilson','Grace Taylor','Henry Anderson','Isabella Thomas','Jack Hill','Kate Baker','Liam Carter','Maria Evans','Noah Robinson','Olivia Lewis','Parker Allen','Quinn Williams','Riley Jones','Sophia Clark','Tyler Brown'}
print(student_name)
# Student Course Enrollment
course_enrollments={'1001':['CS101','MATH101'],'1002':['CS101','MATH102'],'1003':['CS202', 'PHY101'],'1004':['CS202','CHEM101'],'1005':['BIO101','HIST101'],'1006':['BIO102','ENGL101 '],'1007':['ECON101','PSY101'],'1008':['ECON102','SOC101'],'1009':['PSY102','SOC102'],'101 0':['CS101','MATH101']}
print("Student Course Enrollment:")
for student_id,courses in course_enrollments.items():
    print(f"Student ID: {student_id}, Enrolled Courses: {courses}")

#Class Schedule
departments={'Computer Science':[('CS101','Introduction to Computer Science'),('CS202','Data Structures and Algorithms')],'Mathematics':[('MATH101','Calculus I'),('MATH102','Calculus II')],'Physics':[('PHY101','General Physics I'),('PHY102','General Physics II')],'Chemistry':[('CHEM101','General Chemistry I'),('CHEM102','General Chemistry II')],'Biology':[('BIO101','Biology I'),('BIO102','Biology II')],'History':[('HIST101','American History I'),('HIST102','American History II')],'English':[('ENGL101','English Composition I'),('ENGL102','English Composition II')],'Economics':[('ECON101','Principles of Economics'),('ECON102','Intermediate Microeconomics')],'Psychology':[('PSY101','Introduction to Psychology'),('PSY102','Developmental Psychology')],'Sociology':[('SOC101','Introduction to Sociology'),('SOC102','Social Problems')]}
print("Class Schedule:") 
for department,courses in departments.items():
    print(f"Department: {department}") 
    for course_id,course_name in courses:
        print(f"- Course ID: {course_id}, Course Name: {course_name}")

#Lecturer Assignments
lecturer_assignments={'Dr. John Doe':['CS101'],'Prof. Jane Smith':['CS202'],'Mr. Michael Johnson':['PHY102'],'Dr. Emily Brown':['CS101','MATH102'],'Prof. David Lee':['PHY101'],'Asst. Prof. Olivia Taylor':['MATH101','CHEM101'],'Dr. Noah Wilson':['CHEM102'],'Miss. Sophia Carter':['BIO101','BIO102'],'Asst. Prof. Jacob Miller':[],'Dr. Emma Davis':[],'Mrs. Ethan Jones':[],'Asst. Prof. Ava Martinez':[],'Dr. Oliver Hernandez':['HIST101','HIST102','ENGL101'],'Prof. Isabella Garcia':['ENGL102','SOC101'],'Asst. Prof. Liam Lopez':['SOC102'],'Dr. Mia Gonzalez':[],'Prof. Elijah Rodriguez':[],'Asst. Prof. Amelia Perez':[],'Dr. Lucas Sanchez':['PSY101','PSY102'],'Prof. Evelyn Russell':['ECON101','ECON102']}
print("Lecturer Assignments:")
for lecturer,courses in lecturer_assignments.items():
    print(f"Lecturer: {lecturer}, Courses: {courses}")

class_list = []
#User Input Loop
while True:
    student_name=input("Enter student name (or type 'done' to finish): ")
    if student_name.lower()=='done':
         break 
    class_list.append(student_name) 
    print(f"Added '{student_name}' to the class list.")
print("Class List:")
for student in class_list: 
    print(student) 

#Locating rooms
rooms={'101':{'Capacity':15,'Floor':'Ground Floor','Building':'A'},'102':{'Capacity':15,'Floor':'Ground Floor','Building':'A'},'103':{'Capacity':20,'Floor':'Ground Floor','Building':'A'},'104':{'Capacity':20,'Floor':'Ground Floor','Building':'A'},'105':{'Capacity':25,'Floor':'Ground Floor','Building':'A'},'106':{'Capacity':25,'Floor':'Ground Floor','Building':'A'},'107':{'Capacity':30,'Floor':'Ground Floor','Building':'A'},'108':{'Capacity':30,'Floor':'Ground Floor','Building':'A'},'109':{'Capacity':30,'Floor':'Ground Floor','Building':'A'},'110':{'Capacity':10,'Floor':'Ground Floor','Building':'A'},'201':{'Capacity':10,'Floor':'1st Floor','Building':'A'},'202':{'Capacity':10,'Floor':'1st Floor','Building':'A'},'203':{'Capacity':25,'Floor':'1st Floor','Building':'A'},'204':{'Capacity':25,'Floor':'1st Floor','Building':'A'},'205':{'Capacity':30,'Floor':'1st Floor','Building':'A'},'206':{'Capacity':40,'Floor':'1st Floor','Building':'A'},'207':{'Capacity':40,'Floor':'1st Floor','Building':'A'},'208':{'Capacity':40,'Floor':'1st Floor','Building':'A'}}
min_capacity=int(input("Enter the minimum number of seats required: ")) 
suitable_rooms=[] 
for room,details in rooms.items(): 
    if details['Capacity']>=min_capacity: 
        suitable_rooms.append((details['Capacity'],details['Floor'],details['Building'],room)) 
        suitable_rooms.sort() 
        if suitable_rooms:
            capacity,floor,building,room=suitable_rooms[0] 
            print(f"Suitable room: {room}, Capacity: {capacity}, Floor: {floor}, Building: {building}") 
        else: 
            print("No suitable room found.")

#Exit Program (quit, exit, or 0)
while True: 
    student_name=input("Enter student name (or type 'quit','exit', or'0'to finish):") 
    if student_name.lower() in ['quit','exit','0']: 
        exit_param=student_name.lower() 
        break
    class_list.append(student_name)
    print(f"Added'{student_name}'to the class list.") 
    
    print("Class List:") 
    for student in class_list: 
        print(student) 
        print(f"Total students:{len(class_list)}") 
        print(f"Exit parameter:{exit_param}") 

#Exit using active variable
active=True 
while active: 
    student_name=input("Enter student name (or type 'done' to finish): ") 
    if student_name.lower()=='done': 
        active=False 
    else:
        class_list.append(student_name) 
        print(f"Added '{student_name}' to the class list.") 
        
    print("Class List:") 
    for student in class_list: 
        print(student)

#Exit based on room capacity
max_capacity=int(input("Enter maximum room capacity:"))
while len(class_list)<max_capacity:
     student_name=input("Enter student name: ")
     class_list.append(student_name)
     print(f"Added '{student_name}' to the class list.") 
     if len(class_list)==max_capacity: 
        print("Maximum capacity reached.") 
        break 
     print("Class List:") 
     for student in class_list:
         print(student) 
         print(f"Maximum capacity: {max_capacity}") 
    
#Controlling how long the loop runs with an active variable
active=True
while active:
    student_name=input("Enter student name (or type 'done' to finish): ") 
    if student_name.lower()=='done': 
        active=False 
    else:
        class_list_b.append(student_name) 
        print(f"Added '{student_name}' to the class list.") 
        print("\n--- Class List ---") 
        if class_list_b: 
            for student in class_list_b: 
                print(student) 
                total_students=len(class_list_b) 
                print(f"\nTotal number of students entered: {total_students}") 
        else:
                print("No students entered.") 

#Set a variable based on the room capacity
try: max_capacity=int(input("Enter the maximum room capacity:"))
except ValueError: 
    print("Invalid input for capacity.Exiting.") 
else: 
    print(f"Maximum room capacity set to:{max_capacity}") 
    while len(class_list)<max_capacity: 
        student_name=input("Enter student name:") 
        class_list.append(student_name) 
        print(f"Added '{student_name}' to the class list.Current count:{len(class_list)}") 
        if len(class_list)==max_capacity: 
            print("\nMaximum capacity reached.Exiting.") 
            break
        print("\n---Class List---") 
        if class_list: 
            for student in class_list: 
                print(student) 
                print(f"\nMaximum room capacity:{max_capacity}")

#Infinite Loop
students={"1001":{"StudentFirstname":"Alice","StudentLastname":"Smith","Email":"sd1001@ uni123st.edu.au"},"1002":{"StudentFirstname":"Bob","StudentLastname":"Johnson","Email":" sd1002@uni123st.edu.au"},"1003":{"StudentFirstname":"Charlie","StudentLastname":"Brown ","Email":"sd1003@uni123st.edu.au"},"1004":{"StudentFirstname":"David","StudentLastname ":"Lee","Email":"sd1004@uni123st.edu.au"},"1005":{"StudentFirstname":"Emily","StudentLas tname":"Davis","Email":"sd1005@uni123st.edu.au"},"1006":{"StudentFirstname":"Frank","Stu dentLastname":"Wilson","Email":"sd1006@uni123st.edu.au"},"1007":{"StudentFirstname":"G race","StudentLastname":"Taylor","Email":"sd1007@uni123st.edu.au"},"1008":{"StudentFirst name":"Henry","StudentLastname":"Anderson","Email":"sd1008@uni123st.edu.au"},"1009":{" StudentFirstname":"Isabella","StudentLastname":"Thomas","Email":"sd1009@uni123st.edu. au"},"1010":{"StudentFirstname":"Jack","StudentLastname":"Hill","Email":"sd1010@uni123st. edu.au"},"1011":{"StudentFirstname":"Kate","StudentLastname":"Baker","Email":"sd1011@u ni123st.edu.au"},"1012":{"StudentFirstname":"Liam","StudentLastname":"Carter","Email":"sd 1012@uni123st.edu.au"},"1013":{"StudentFirstname":"Maria","StudentLastname":"Evans","E mail":"sd1013@uni123st.edu.au"},"1014":{"StudentFirstname":"Noah","StudentLastname":"R obinson","Email":"sd1014@uni123st.edu.au"},"1015":{"StudentFirstname":"Olivia","StudentL astname":"Lewis","Email":"sd1015@uni123st.edu.au"},"1016":{"StudentFirstname":"Parker"," StudentLastname":"Allen","Email":"sd1016@uni123st.edu.au"},"1017":{"StudentFirstname":" Quinn","StudentLastname":"Williams","Email":"sd1017@uni123st.edu.au"},"1018":{"StudentF irstname":"Riley","StudentLastname":"Jones","Email":"sd1018@uni123st.edu.au"},"1019":{"S tudentFirstname":"Sophia","StudentLastname":"Clark","Email":"sd1019@uni123st.edu.au"}," 1020":{"StudentFirstname":"Tyler","StudentLastname":"Brown","Email":"sd1020@uni123st.e du.au"}}
line_count=0 
try: 
    while True: 
        student_id=input("Enter Student ID (or press Ctrl+C to exit):") 
        if student_id in students: 
            print(f"Student Details:{students[student_id]}") 
        else:
             print("Student ID not found.") 
        line_count+=1 
except KeyboardInterrupt: 
        print(f"\nTotal student IDs entered:{line_count}") 

print("The world is mine")