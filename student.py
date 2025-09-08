#dictionary meh kaam krna h isme
'''
Dictionary 
collection - key+value = pair = data 1
left-side = key 
right-side = value 
{Key1:Value1, Key2:value2}

# '''

# var = {'key1': 100, 'key2':200}
# print(var)

#Create a Dictonary 
# student = {
#     'Paras': 100,
#     'Gopal': 200,
    
# }

# #Accesing a element 
# print(student['Gopal'])

# #Update 
# student['Gopal'] = 300
# print(student)


# delete 
# del student['Paras']
# print(student)



# <<----Main Project----->>

#Initializing dictionary
student_grades = {}

#Add a new student 
def add_student(name, grade):
    student_grades[name] = grade 
    #[sagar] = 100
    print(f"Added {name} with a {grade}")
    #Added sagar with a 100
    
#Update a student 
def update_student(nam, grade):
    if name in student_grades:
        student_grades[name] = grade 
        #sagar = 200
        print(f"{name} with marks are updated {grade}")
    
    else:
        print(f"{name} is not found!")
        
#Delete a student 
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    
    else:
        print(f"{name} is not found!")
        

#view all the stidents 
def display_all_student():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
            
    else:
        print("NO student found")
        

def mamin():
    while True:
        print('\n Student Grades Management System')
        print("1. Add Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. exit")  
        
        
    choice = int(input("Enter your choice = "))
    if choice == 1:
        name = input("Enter the name of the stuent:- ")
        grade = int(input("Enter the grade of the student :- "))
        add_student(name, grade)
        
     
              
        


