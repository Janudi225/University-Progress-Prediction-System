# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:w1953985
# Date:03/12/2022

def getting_credits(loop,valid_credit,credit_type):
    "This will get pass credits and check if it is valid"
    while loop:
        try:
            #inputting data
            credit=int(input("Please enter credits at " +credit_type+ ":"))
            #checking whether the input is valid
            if credit in valid_credit:
                bloop=False
                return credit
            else:
                print("Out of range\n")
                continue
        except ValueError:
            print("Integer required\n")

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
        elif pass_credit==120:
            result="Progress"
            loop=False
        elif pass_credit==100:
            result="Progress(module trailer)"
            loop=False
        elif fail_credit>=80:
            result="Exclude"
            loop=False
        else:
            result="module retriever"
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
    list2=[]
    fo=0
    while need_to_repeat:
        #calling functions to get the input values
        pass_credit=getting_credits(loop,valid_credit,"pass")
        defer_credit=getting_credits(loop,valid_credit,"defer")
        fail_credit=getting_credits(loop,valid_credit,"fail")
        tot_credit=pass_credit+defer_credit+fail_credit
        #finding the progression outcome
        if tot_credit !=120:
            print("Total incorrect\n")
            continue
        elif pass_credit==120:
            result="Progress"
            progress_num+=1
            need_to_repeat=False
        elif pass_credit==100:
            result="Progress(module trailer)"
            trailer_num+=1
            need_to_repeat=False
        elif fail_credit>=80:
            result="Exclude"
            exclude_num+=1
            need_to_repeat=False
        else:
            result="module retriever"
            retriever_num+=1
            need_to_repeat=False
        print(result)
        #adding marks to lists
        list1=[result,"-",pass_credit,",",defer_credit,",",fail_credit]
        list2.append(list1)
        #calling the function to find if the user needs to repeat
        need_to_repeat=need_to_continue(error_repeat=True)
        
    #displaying the histogram
    print("-"*50)
    print("Histogram")
    print("Progress ",progress_num," :","*"*progress_num)
    print("Trailer ",trailer_num,"  :","*"*trailer_num)
    print("Retriever ",retriever_num,":","*"*retriever_num)
    print("Exclude ",exclude_num,"  :","*"*exclude_num)
    print("\n",progress_num+trailer_num+exclude_num+retriever_num,"outcomes in total")
    print("-"*50)

    #displaying progression outcome and marks of each student
    print("Part 2:")
    for value in list2:
        for data in value:
            print(data,end="")
        print(sep="\n")
    print(" ")
    
    #writing progression outcome and marks of each student in "marks.txt"
    fo=open("marks.txt","w")
    fo.write("Part 3:\n")
    for value in list2:
        for data in value:
            fo.write(str(data))
        fo.write("\n")
    fo.close()
             
    #getting the outcome and marks from "marks.txt"
    fo1=open("marks.txt","r")
    print(fo1.read())
    fo1.close()
    
