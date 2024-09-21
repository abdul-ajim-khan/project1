st_id   =  []
st_list =  []
st_PhNum = []
st_Email = []

St_id_num = 0

del_Ids = []
del_Names = []
del_Emails = []
del_Phones = []
# 1
def ShowStudentList(st_list, St_id_num, st_Email, st_PhNum):
    for name in st_list:
        St_id_num += 1
        st_id.append(St_id_num)
        print(f"ID-{St_id_num}, Name-{name}, Ph-{st_PhNum[St_id_num-1]}, Email-{st_Email[St_id_num-1]}")
# ShowStudentList(st_list, St_id_num, st_Email, st_PhNum)



# 2
def ShowDetails(st_list, St_id_num, st_Email, st_PhNum):
    print("Enter id to search student Details: \nEnter '0' To Quit")
    sch_id = (input("Enter Your choice: "))
    if(sch_id=="0"):
        exit
    else:
        b=True
        for a in st_id:
            if(int(sch_id)==(a)):
                # print(a)
                print("Student found")
                print(f"ID-{a}, Name-{st_list[a-1]}, Ph-{st_PhNum[a-1]}, Email-{st_Email[a-1]}")
                b=False
                break
        if(b==True):
            print("Student Not found")
# ShowDetails(st_list, St_id_num, st_Email, st_PhNum)



# 3
def addStudent(st_list, St_id_num, st_Email, st_PhNum, st_id):
    print("press '0'=> To Quit")
    st_name = input("Enter student's name: \n")
    if(st_name == '0'):
        return 0
    else:
        st_list.append(st_name)
        # St_id_num += 1
        # st_id.append(St_id_num)
        print("press '0'=> To Quit")
        st_EmInput = input("Enter student's Email: \n")
        if(st_EmInput == '0'):
            st_Email.append("")
            exit
        else:
            if(("." in st_EmInput) and ("@" in st_EmInput)):
                c=1
                for a in st_Email:
                    if(a==st_EmInput):
                        c=0
                if(c):
                    st_Email.append(st_EmInput)      
                    print("press '0'=> To Quit")
                    st_phone = input("Enter student's Phone num: \n")
                    if(st_phone == '0'):
                        st_Email.append("")
                        exit
                    else:
                        if(st_PhNum not in st_PhNum):
                            st_PhNum.append(st_phone)
                        else:
                            print("Please Enter Valied & Unique data")
                            print(st_PhNum)
                            addStudent(st_list, St_id_num, st_Email, st_PhNum, st_id)
# print(st_list, St_id_num, st_Email, st_PhNum, st_id)
# addStudent(st_list, St_id_num, st_Email, st_PhNum, st_id)
            





def update(st_list, st_Email, st_PhNum, st_id):
    print("press '0'=> To Quit")
    student_id = int(input("Enter Student's Id :"))
    if(student_id==0):
        exit
    else:
        if(student_id in st_id):
            print(f"Choose what would you want to update?\n1) Name\n2) Email\n3) Phone num")
            choice = int(input("Enter choice: "))
            if(choice==1):
                name = input("Enter New Name: ")
                st_list[student_id-1] = name
            elif(choice==2):
                def Emails(st_Email):
                    Email = input("Enter New Email: ")
                    if(Email in st_Email):
                        Emails(st_Email)
                    st_Email[student_id-1] = Email
                Emails(st_Email)
            elif(choice==3):
                def phones(st_PhNum):
                    Phone = input("Enter New Phone: ")
                    if(Phone in st_PhNum):
                        print("Invalied input")
                        phones(st_PhNum)
                    st_PhNum[student_id-1] = Phone
                phones(st_PhNum)
        else:
            print("This student not found")
# update(st_list, st_Email, st_PhNum, st_id)



    





def delete(del_Ids, del_Names, del_Emails, del_Phones, st_id, st_list, st_Email, st_PhNum):
    print("press '0'=> To Quit")
    id_num = int(input("To Remove The student Enter Id: "))
    if(id_num in st_id):
        del_Ids.append(id_num)
        del_Emails.append(st_Email[id_num-1])
        del_Names.append(st_list[id_num-1])
        del_Phones.append(st_PhNum[id_num-1])
# delete(del_Ids, del_Names, del_Emails, del_Phones, st_id, st_list, st_Email, st_PhNum)



def showDeleted(del_Ids, del_Names, del_Emails, del_Phones):
    count=-1
    while(del_Ids):
        count+=1
        print(f"ID-{del_Ids[count]}, Name-{del_Names[count]}, Ph-{del_Phones[count]}, Email-{del_Emails[count]}")
# showDeleted(del_Ids, del_Names, del_Emails, del_Phones)







def studentList():
    print("All Options:\n1) Show student list\n2) Show student details\n3) Add new student\n4) Update a student Details\n5) Remove a student\n6) Show Deleted Students\n0) QUIT")
    choice= input("Enter the option number: ")
    print()
    if(choice=="1"):
        ShowStudentList(st_list, St_id_num, st_Email, st_PhNum)
        print()
        studentList()
    elif(choice=="2"):
        ShowDetails(st_list, St_id_num, st_Email, st_PhNum)
        print()
        studentList()
    elif(choice=="3"):
        addStudent(st_list, St_id_num, st_Email, st_PhNum, st_id)
        print()
        studentList()
    elif(choice=="4"):
        update(st_list, st_Email, st_PhNum, st_id)
        print()
        studentList()
    elif(choice=="5"):
        delete(del_Ids, del_Names, del_Emails, del_Phones, st_id, st_list, st_Email, st_PhNum)
        print()
        studentList()
    elif(choice=="6"):
        showDeleted(del_Ids, del_Names, del_Emails, del_Phones)
        print()
        studentList()
    else:
        exit
studentList()
