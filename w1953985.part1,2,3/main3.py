# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:w1953985
# Date:03/12/2022

#calling the module "functions"
import functions3

#Assigning variables
valid_credit=[0,20,40,60,80,100,120]
valid_user=True
user=""
loop=True

#finding the user
while valid_user==True:
    print("""If you are a student, please enter "s" or "student".
If you are a staff member, please enter "t" or "teacher".\n""")
    user=input("Enter the type of person using the program :")
    #finding whether the user is valid
    if user.lower()=="s" or user.lower()=="student" or user.lower()=="t" or user.lower()=="teacher":
        break
    else:
        print("\nThe input user is invalid\n")
        continue

if user.lower()=="s" or user.lower()=="student":
    #calling the function that runs the code for students
    functions3.finding_outcome_student(loop,valid_credit)

if user.lower()=="t" or user.lower()=="teacher":
    #calling the function that runs the code for teachers
    functions3.finding_outcome_teacher(loop,valid_credit)
