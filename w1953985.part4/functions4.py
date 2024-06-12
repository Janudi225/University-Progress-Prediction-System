# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:w1953985
# Date:03/12/2022

def getting_credits(loop,valid_credit,credit_type):
    "This will get credits and check if they are valid"
    while loop:
        try:
            credit=int(input("Please enter credits at " +credit_type+ ":"))
            #checking whether the input is valid
            if credit in valid_credit:
                loop=False
                return credit
            else:
                print("Out of range\n")
                continue
        except ValueError:
            print("Integer required\n")

def student_id(loop,keys_dict):
    "This will get the student id and check if it is valid"
    while loop:
        stu_id=input("Please enter the student ID :")
        #cheking whether the id is correct
        if stu_id not in keys_dict:
            if len(stu_id)==8 and stu_id[0]=="w" and stu_id[1:].isdigit():
                loop=False
                return stu_id
            else:
                print("Invalid student ID")
                continue
        else:
            print("You have already added this ID. Enter another.")
        
def need_to_continue(error_repeat=True):
    "This will find out if the user wants input more students"
    while error_repeat:
        input_again=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        print(" ")
        #cheking whether the user needs to repeat
        if input_again.lower()=="y" or input_again.lower()=="q":
            loop=False
            if input_again.lower()=="y":
                return True
            elif input_again.lower()=="q":
                return False
        else:
            print("Invalid input. Please enter again.")

def progression(pass_credit, fail_credit):
    if  pass_credit==120:
        result="Progress"
    elif pass_credit==100:
        result="Progress(module trailer)"
    elif fail_credit>=80:
        result="Exclude"
    else:
        result="module retriever"
    return result
    

def finding_outcome_student(loop,valid_credit):
    "This will determine the result of the student"
    while loop:
        #calling functions to get the input values
        pass_credit=getting_credits(loop,valid_credit,"pass")
        defer_credit=getting_credits(loop,valid_credit,"defer")
        fail_credit=getting_credits(loop,valid_credit,"fail")
        tot_credit=pass_credit+defer_credit+fail_credit
        #finding the progression outcome
        if tot_credit !=120:
            print("Total incorrect\n")
            continue
        else:
            result=progression(pass_credit, fail_credit)
            loop=False
            print(result)
        
def finding_outcome_teacher(loop,valid_credit):
    "This will determine the result of the student"
    progress_num=0
    trailer_num=0
    retriever_num=0
    exclude_num=0
    need_to_repeat=True
    result=""
    resultdict={}
    while need_to_repeat:
        #calling function to get the student id
        keys_dict=list(resultdict.keys())
        stu_id=student_id(loop,keys_dict)       
        #calling functions to get the input values
        pass_credit=getting_credits(loop,valid_credit,"pass")
        defer_credit=getting_credits(loop,valid_credit,"defer")
        fail_credit=getting_credits(loop,valid_credit,"fail")
        tot_credit=pass_credit+defer_credit+fail_credit
        #finding the progression outcome
        if tot_credit !=120:
            print("Total incorrect\n")
            continue
        else:
            result=progression(pass_credit, fail_credit)
            need_to_repeat=False
            print(result)
        #adding results to the dictionary
        resultdict[stu_id]=[result,"-",pass_credit,",",defer_credit,",",fail_credit]
        #calling the function to find if the user needs to repeat
        need_to_repeat=need_to_continue(error_repeat=True)

    #displaying outcome using dictionaries
    print("Part 4:")
    for (key,value) in resultdict.items():
        print(key," :",end="")
        for data in value:
            print(data,end="")
        print(sep="\n")
    
