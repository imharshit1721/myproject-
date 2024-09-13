import mysql.connector
con  = mysql.connector.connect(host = "localhost" , user = "harshitvyas" , passwd = "12345678" , database = "harshitfriends")
cursor = con.cursor()


def add_student():
      student_name   = input("enter student name")
      student_rollno = input("enter roll number")
      branch         = input("enter branch of student")
      batch          = input("enter batch of student")
      lst = [student_name , student_rollno , branch , batch]
      insert = "insert into student_detail(s_name , s_rollno , branch ,batch )values(%s , %s  ,%s  ,%s)"
      cursor.execute(insert ,lst)
      con.commit()

class fetch_data(): #to take data from table and insert in list and categories (like student in first year , final year so he will appear in all)
      
      cursor.execute("select * from student_detail")
      lst_all_students = []
      lst_all_students = cursor.fetchall()
      
      final_year = []
      third_year = []
      second_year = []
      first_year = []
 

      for i in lst_all_students:
               if i[1][0] == "1":
                  final_year.append(i)
               elif i[1][0] == "2":
                  third_year.append(i)
               elif i[1][0] == "3":
                  second_year.append(i)
               elif i[1][0] == "4":
                  first_year.append(i)

      final_third = final_year + third_year
      second_third_final = final_year + third_year + second_year

'''
class guna(fetch_data):
    def guna1(self):
        print(fetch_data.final_third)
'''



class final_yearr(fetch_data):
      
      def marks_insert(self):
          st_detail = []
          n = input("enter the student whose you want to add marks(Roll  number)")
          for i in fetch_data.final_year:
              if (i[1] == n):   
                marks1 = int(input("enter marks in operating system"))
                marks2 = int(input("enter marks in java"))
                marks3 = int(input("enter marks in Maths4"))
                marks4 = int(input("enter marks in ADV DBMS")) 
                marks5 = int(input("enter marks in DAA"))
                st_detail.append(i[0])
                st_detail.append(i[1])
                st_detail.append(i[2])
                st_detail.append(i[3])
                #st_detail = fetch_data.final_year[i]
           #     st_name = fetch_data.final_year[i[0]]
            #    roll_no = fetch_data.final_year[i[1]]
           #     branch  = fetch_data.final_year[i[2]]
           #     batch  = fetch_data.final_year[i[3]]

              else:
               continue

          lst = [st_detail[0], st_detail[1] , st_detail[2] , st_detail[3] , marks1, marks2 , marks3 , marks4 , marks5]
          marks_insert = "insert into final_year(st_name , roll_no , branch , batch , marks1, marks2 , marks3 , marks4 , marks5) values(%s ,%s , %s , %s , %s  ,%s , %s , %s , %s )"
      
          cursor.execute(marks_insert , lst)
          con.commit()
               
'''
class final_yearr(fetch_data):
      
      marks1 = int(input("enter marks in sub1"))
      marks2 = int(input("enter marks in sub2"))
      marks3 = int(input("enter marks in sub3"))
      marks4 = int(input("enter marks in sub4")) 
      marks5 = int(input("enter marks in sub5"))
      lst = [marks1 , marks2 , marks3 , marks4 , marks5]
      marks_insert = "insert into final_year(st_name , roll_no , branch , batch , marks1, marks2 , marks3 , mark4 , marks5) values(%s ,%s , %s , %s , %s  ,%s , %s , %s , %s )"
      fourth = [fetch_data.final_year + lst]
      cursor.execute(marks_insert , fourth)
      con.commit()
'''

class third_yearr(fetch_data):
        def insert_marks(self):
           st_details = []
           n = input("enter student whose you want to add marks(roll_no)")

           for i in fetch_data.final_third:
              if (i[1] == n):
                 marks1 = int(input("enter marks in microprocessor"))
                 marks2 = int(input("enter marks in DSA"))
                 marks3 = int(input("enter marks in DBMS"))
                 marks4 = int(input("enter marks in computer network"))
                 marks5 = int(input("enter marks in Maths3"))
                 st_details.append(i[0])
                 st_details.append(i[1])
                 st_details.append(i[2])
                 st_details.append(i[3])

              else:
                  continue
           
           third = [st_details[0], st_details[1] , st_details[2] , st_details[3] ,marks1 , marks2 , marks3 , marks4 , marks5]
           marks_insert = "insert into third_year(st_name , roll_no , branch , batch , marks1, marks2 , marks3 , marks4 , marks5) values(%s ,%s , %s , %s , %s  ,%s , %s , %s , %s )"
           cursor.execute(marks_insert , third)
           con.commit()
           del st_details
           del third

class second_year():
    def insert_marks_second(self):
        st_details = []
        n = input("enter roll no whose you want to add marks")
        for i in fetch_data.second_third_final:
            if (i[1] == n):
                marks1 = int(input("enter marks in oops"))
                marks2 = int(input("enter marks in digital electronics"))
                marks3 = int(input("enter marks in physics"))
                marks4 = int(input("enter marks in maths2"))
                marks5 = int(input("enter marks in economics"))
                st_details.append(i[0])
                st_details.append(i[1])
                st_details.append(i[2])
                st_details.append(i[3])
            else:
                continue

        second = [st_details[0], st_details[1] , st_details[2] , st_details[3] , marks1 , marks2 , marks3 , marks4 , marks5]
        marks_insert = "insert into second_year(st_name , roll_no , branch , batch , marks1  ,marks2  ,marks3  ,marks4 , marks5) values(%s ,%s  ,%s  , %s , %s , %s , %s , %s , %s)"
        cursor.execute(marks_insert , second)
        con.commit()


class first_year():
    def insert_marks_first(self):
        st_details = []
        n = input("enter roll no you want to add marks")
        for i in fetch_data.lst_all_students:
            if(i[1] == n):
                marks1 = int(input("enter marks in computer programming"))
                marks2 = int(input("enter marks in basic electronics"))
                marks3 = int(input("enter marks in english"))
                marks4 = int(input("enter marks in Maths1"))
                marks5 = int(input("enter marks in environment"))
                st_details.append(i[0]) 
                st_details.append(i[1]) 
                st_details.append(i[2]) 
                st_details.append(i[3]) 
        first = [st_details[0] , st_details[1] , st_details[2] , st_details[3] ,  marks1 , marks2 , marks3 , marks4 , marks5]
        marks_insert = "insert into first_year(st_name , roll_no , branch , batch , marks1 , marks2 , marks3 , marks4 , marks5) values(%s , %s , %s  ,%s , %s, %s , %s , %s  ,%s)"
        cursor.execute(marks_insert , first)
        con.commit()



class student():
    def final_year_result(self, roll_number):

        list_of_pass = []
        count = 0
        cursor.execute("select * from final_year")
        student_final_year = []
        student_final_year = cursor.fetchall()
        for e in student_final_year:
            if (e[1] == roll_number):
                print(f"student name  = {e[0]}")
                print(f"student roll number = {e[1]}")
                print(f"student branch = {e[2]}")
                print(f"student batch = {e[3]}")
                print(f"marks1 = {e[4]}") 
                print(f"marks2 = {e[5]}") 
                print(f"marks3 = {e[6]}")
                print(f"marks4 = {e[7]}")
                print(f"marks5 = {e[8]}")
                total = (float(e[4]) + float(e[5]) + float(e[6]) + float(e[7]) + float(e[8]))//6
                print("average =" ,total)

                if (total >= 90):
                    print("Grade A")
                elif (total <= 89 and total >= 80):
                    print("grade B")
                elif (total >=70 and total <=79):
                    print("grade c")
                elif (total >=60 and total <=69):
                    print("grade D")
                elif (total >=40 and total <=59):
                    print("grade E")
                else:
                    print("F")

                list_of_pass.append(int(e[4]))    
                list_of_pass.append(int(e[5])) 
                list_of_pass.append(int(e[6])) 
                list_of_pass.append(int(e[7])) 
                list_of_pass.append(int(e[8])) 

                for i in list_of_pass:
                    if (i < 42):
                        count += 1
                    else:
                        continue

                if count > 0:
                    print("number of backslogs =" , count)
                elif count == 0:
                    print("pass")

                del student_final_year
                del list_of_pass
                count = 0

    def third_year_student(self , roll_number):
        list_of_pass = []
        count   =  0
        cursor.execute("select * from third_year")
        student_third_year = []
        student_third_year = cursor.fetchall()
        for e in student_third_year:
            if (e[1] == roll_number):
                print(f"student name  = {e[0]}")
                print(f"student roll number = {e[1]}")
                print(f"student branch = {e[2]}")
                print(f"student batch = {e[3]}")
                print(f"marks1 = {e[4]}") 
                print(f"marks2 = {e[5]}") 
                print(f"marks3 = {e[6]}")
                print(f"marks4 = {e[7]}")
                print(f"marks5 = {e[8]}")
                total = (float(e[4]) + float(e[5]) + float(e[6]) + float(e[7]) + float(e[8]))//6
                print("average =" ,total)

                if (total >= 90):
                    print("Grade A")
                elif (total <= 89 and total >= 80):
                    print("grade B")
                elif (total >=70 and total <=79):
                    print("grade c")
                elif (total >=60 and total <=69):
                    print("grade D")
                elif (total >=40 and total <=59):
                    print("grade E")
                else:
                    print("F")


                list_of_pass.append(int(e[4]))    
                list_of_pass.append(int(e[5])) 
                list_of_pass.append(int(e[6])) 
                list_of_pass.append(int(e[7])) 
                list_of_pass.append(int(e[8])) 

                for i in list_of_pass:
                    if (i < 42):
                        count += 1
                    else:
                        continue

                if count > 0:
                    print("number of backslogs =" , count)
                elif count == 0:
                    print("pass")


                
                del student_third_year
                del list_of_pass
                count = 0

    def second_year_student(self , roll_number):

        list_of_pass = []
        count = 0
        cursor.execute("select * from second_year")
        student_second_year = []
        student_second_year = cursor.fetchall()
        for e in student_second_year:
            if (e[1] == roll_number):
                print(f"student name  = {e[0]}")
                print(f"student roll number = {e[1]}")
                print(f"student branch = {e[2]}")
                print(f"student batch = {e[3]}")
                print(f"marks1 = {e[4]}") 
                print(f"marks2 = {e[5]}") 
                print(f"marks3 = {e[6]}")
                print(f"marks4 = {e[7]}")
                print(f"marks5 = {e[8]}")
                total = (float(e[4]) + float(e[5]) + float(e[6]) + float(e[7]) + float(e[8]))//6
                print("average = " ,total)

                if (total >= 90):
                    print("Grade A")
                elif (total <= 89 and total >= 80):
                    print("grade B")
                elif (total >=70 and total <=79):
                    print("grade c")
                elif (total >=60 and total <=69):
                    print("grade D")
                elif (total >=40 and total <=59):
                    print("grade E")
                else:
                    print("F")

                
                list_of_pass.append(int(e[4]))    
                list_of_pass.append(int(e[5])) 
                list_of_pass.append(int(e[6])) 
                list_of_pass.append(int(e[7])) 
                list_of_pass.append(int(e[8])) 

                for i in list_of_pass:
                    if (i < 42):
                        count += 1
                    else:
                        continue

                if count > 0:
                    print("number of backslogs =" , count)
                elif count == 0:
                    print("pass")



                del student_second_year
                del list_of_pass
                count = 0

    def first_year_student(self , roll_number):
        list_of_pass = []
        count = 0
        cursor.execute("select * from first_year")
        student_first_year = []
        student_first_year = cursor.fetchall()
        for e in student_first_year:
            if(e[1] == roll_number):
                print(f"student name  = {e[0]}")
                print(f"student roll number = {e[1]}")
                print(f"student branch = {e[2]}")
                print(f"student batch = {e[3]}")
                print(f"marks1 = {e[4]}") 
                print(f"marks2 = {e[5]}") 
                print(f"marks3 = {e[6]}")
                print(f"marks4 = {e[7]}")
                print(f"marks5 = {e[8]}")
                total = (float(e[4]) + float(e[5]) + float(e[6]) + float(e[7]) + float(e[8]))//6
                print("average" , total)

                if (total >= 90):
                    print("Grade A")
                elif (total <= 89 and total >= 80):
                    print("grade B")
                elif (total >=70 and total <=79):
                    print("grade c")
                elif (total >=60 and total <=69):
                    print("grade D")
                elif (total >=40 and total <=59):
                    print("grade E")
                else:
                    print("F")

                
                list_of_pass.append(int(e[4]))    
                list_of_pass.append(int(e[5])) 
                list_of_pass.append(int(e[6])) 
                list_of_pass.append(int(e[7])) 
                list_of_pass.append(int(e[8])) 

                for i in list_of_pass:
                    if (i < 42):
                        count += 1
                    else:
                        continue

                if count > 0:
                    print("number of backslogs =" , count)
                elif count == 0:
                    print("pass")



                del student_first_year
                del list_of_pass
                count = 0

class backs():
    def backlogs(self , roll_number):
         sem11 = {}
         sem22  = {}
         sem33 = {}
         sem44 = {}
         sem_1 = []
         cursor.execute("select * from first_year")
         sem1 = cursor.fetchall()
         for i in sem1:
            if(i[1] == roll_number):
                sem11 = {
                    "compute_programming" : int(i[4]),
                    "basic electronics" : int(i[5]),
                    "english" : int(i[6]),
                    "maths1"   : int(i[7]),
                    "enviornment" : int(i[8]) 

                }


         sem2 = []
         cursor.execute("select * from second_year")
         sem2 = cursor.fetchall()
         for i in sem2:
            if(i[1] == roll_number):
                sem22 = {
                    "oops" : int(i[4]),
                    "digital_electronics" : int(i[5]),
                    "physics" : int(i[6]),
                    "maths2" : int(i[7]),
                    "economics" : int(i[8])
 }
         sem3 = []
         cursor.execute("select * from third_year")
         sem3 = cursor.fetchall()
         for i in sem3:
            if(i[1] == roll_number):
                sem33 = {
                    "microprocessor" : int(i[4]),
                    "DSA"             : int(i[5]),
                    "DBMS"           : int(i[6]),
                    "Computer_network" : int(i[7]),
                    "Maths3"             : int(i[8])
                }
         sem4 = []
         cursor.execute("select * from final_year")
         sem4 = cursor.fetchall()
         for i in sem4:
            if(i[1] == roll_number):
                sem44 = {
                    "operating_system": int(i[4]),
                    "java"            : int(i[5]),
                    "maths4"           : int(i[6]),
                    "ADV DBMS"         : int(i[7]),
                    "DAA"          : int(i[8])
                }

         sem = sem11 | sem22  | sem33 | sem44
         #print(sem)

         
         backlogs_lst = []
         for i in sem:
            if(int(sem[i]) < 42):
                backlogs_lst.append(i)

         length_lst = len(backlogs_lst)
         if(length_lst > 0 ):
            print("""
            backlogs subjcets ::         
            """)
            for i in backlogs_lst:
                print("\t\t\t",i)
         elif(length_lst == 0):
            print("no backlogs")

         del backlogs_lst
        



objfinal = final_yearr()
objthird = third_yearr()
objsecond = second_year()
objfirst = first_year()
objstudent = student()
objback = backs()
#g = guna()



#g.guna1()
user_input = input("""enter 1 for principle section 2 for studentsection(to see the result) , 
                       enter 3 for see backlogs       """)
if user_input == "1":
    user_input = input("""
               enter 1 for add student
               enter 2 for insert marks for student                       
""")
    
    match user_input:
       case "1":
         add_student()
         #print("add students")

       case "2":
         principle_choice = input("""
                             
                                    enter 4 for final year
                                    enter 3 for third year
                                    enter 2 for second year
                                    enter 1 for first year

               
                                  """)
         #print("insert marks")
         match principle_choice:
             case "4":
                objfinal.marks_insert()
             case "3":
                objthird.insert_marks()
             case "2":
                 objsecond.insert_marks_second()
             case "1":
                  objfirst.insert_marks_first()
                 
                 
                 
             

                 
                 
                 

elif user_input == "2":
    print("this is for student secton to see result ")
    roll_number = input("enter the roll number of student to see result")
    see_result = input("""     
                                  enter 4 to see result of final year
                                  enter 3 to see result of third year
                                  enter 2  to see result of second year
                                  enter 1  to see result of first year
                       """)
    
    match see_result:
        case "4":
            objstudent.final_year_result(roll_number)
               
        case "3":
            objstudent.third_year_student(roll_number)

            #print("third year")
        case "2":
            objstudent.second_year_student(roll_number)

            #print("second year")

        case "1":
            objstudent.first_year_student(roll_number)
            #print("first year")

elif user_input == "3":
    roll_number = input("enter roll number of whose you want to see backlogs")
    objback.backlogs(roll_number)
    




























      
          
      
    
         


      







        
       

      
      


      
      
      
      
      
    
       
      

      
       
























