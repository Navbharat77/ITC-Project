
class University():

    def universityDetails(self):
        while True:

            print("\n" +"*******" +"University" + "******" )
            
            print("1. Select State" )   
            a = input("Please Select Your Options:  \n ")
            if (a == '1'):
                print("All State")
                print("\n" * 2)
                self.selectState()
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(a) + "). Try again!")

               
    def selectState(self):
        while True:
            print("\n" "*******" +"Select State" + "******" )
            
            print("1.  Delhi" )   
            print("2.  Jharkhand") 
            print("3.  Madhya Pradesh") 
            print("4.  Karnataka") 
            # print("5.  Gujarat") 
            # print("6.  go Back ") 
            
            state= input("Please Select Your Options:  \n ")
            if (state == '1'):
                print("\n" * 2)
                self.delhi()
            elif (state== '2'):
                print("\n" * 2)
                self.jharkhand()
            elif (state== '3'):
                print("\n" * 2)
                self.madhyapradesh()
            elif (state== '4'):
                print("\n" * 10)
                self.karnataka()
            # elif (state== '6'):
            #     print("\n" * 2)
            #     self.selectState()
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(state) + "). Try again!")
    def delhi(self):
    # print(userdetails)
        while True:
            print("\n""*******" +"Delhi" + "******" )
            
            print("1. Indra gandhi Delhi Technical University for Women" ) 
            print("2. Delhi Technological University" ) 
            print("3. National Law University") 
            print("4. Go Back ") 
            input_5 = input("Please Select Your Options:  \n ").upper()
            if (input_5 == '1'):
                print("\n" * 2)
                self.indragandhiUniversity()
            elif (input_5 == '2'):
                print("\n" *2)
                self.technologicalUniversity()
            elif (input_5 == '3'):
                print("\n" * 2)
                self.lawUniversity()
            elif (input_5 == '4'):
                print("\n" * 2)
                self.selectState()
            else:
                print("\n" *2+ "ERROR: Invalid Input (" + str(input_5) + "). Try again!")

    def indragandhiUniversity(self):
    # print(userdetails)
        while True:
            print("\n" +"*******" +"Indra gandhi Delhi Technical University for Women" + "******" )
            
            print("1. About" ) 
            print("2. Departments" )
            print("3. Course" )
            print("4. Admission")
            print("5. Faculty" )
            print("6. Go Back") 
            input_6 = input("Please Select Your Options:  \n ").upper()
            if (input_6 == '1'):
                print("Location: New Delhi")
                print("Established: 2013")
                print("Specialization: Technology")
                print("Ranking: NIRF ranked 177 among Engineering college in 2022")
                print("Facility: Computer Center, Bank ,Guest House")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.indragandhiUniversity()
                    
                else:
                    print("invalid !! Please Enter 6")
    
            elif (input_6 == '2'):
                print("-> Computer Science and Engineering")
                print("-> Electronics and Communication Engineering")
                print("-> Mechanical  and  Automation Engineering") 
                print("-> Information Technology")
                print("-> Management ")
                print("-> Applied Science & Humanities")
                print("-> Artificial Intelligence & machine learning")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.indragandhiUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '3'):
                print("1. Undergraduate \n Programme:B.Tech \n Year : 4 \n Semester :8")
                print("2. Postgraduate \n Programme:M.Tech \n Year : 2 \n Semester :4")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.indragandhiUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '4'):
                print("For Undergraduate B.tech courses based on IITJEE MAINS rank")
                print("For Postgraduate M.tech courses based on GATE scores")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.indragandhiUniversity()
                else:
                    print("invalid !! Please Enter 6:")
            if (input_6 == '5'):
                print("HOD CSE Department: Prof. Seeja. K. R. \n Qualification :Phd in Computer Science in 2010 from Jamia Hamdard University")
                print("HOD IT Department: Prof. Amar K Mohapatra \n Qualification :Phd in IT from GGSIP university")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.indragandhiUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '6'):
                    self.delhi()
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_6) + "). Try again!")
    
    def  technologicalUniversity(self):
    # print(userdetails)
        while True:
            print("\n" +"*******" +"Delhi Technological University" + "******" )
            
            print("1. About" ) 
            print("2. Departments" )
            print("3. Course" )
            print("4. Admission")
            print("5. Faculty" )
            print("6. Go Back ") 
            input_6 = input("Please Select Your Options:  \n ").upper()
            if (input_6 == '1'):
                print("Location: Delhi")
                print("Established: 2009")
                print("Specialization: Technology")
                print("Ranking: NIRF ranked 36th in the engineering college in 2020")
                print("Facility: Hostel,Cultural events")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.technologicalUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
    
            elif (input_6 == '2'):
                print("-> Computer Science and Engineering")
                print("-> Electronics and Communication Engineering")
                print("-> Mechanical Engineering") 
                print("-> Information Technology")
                print("-> Civil Engineering ")
                print("-> Artificial Intelligence & machine learning")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.technologicalUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '3'):
                print("1. Undergraduate \n Programme:B.Tech \n Year : 4 \n Semester :8")
                print("2. Postgraduate \n Programme:M.Tech \n Year : 2 \n Semester :4")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.technologicalUniversity()
                else:
                    print("invalid !! Please Enter B ")
            elif (input_6 == '4'):
                print("For Undergraduate B.tech courses based on IITJEE MAINS rank")
                print("For Postgraduate M.tech courses based on GATE scores")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.technologicalUniversity()
                else:
                    print("invalid !! Please Enter 6:")
            elif (input_6 == '5'):
                print("Chancellor: Vinai kumar Saxena ")
                print("Vice-Chancellor:Jai Prakash Saini  ")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.technologicalUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '6'):
                print("\n" * 2)
                self.delhi()
            else:
                print("\n" * 2+ "ERROR: Invalid Input (" + str(input_6) + "). Try again!")

#***********************************  National Law University   ********************************
    def  lawUniversity(self):
    # print(userdetails)
        while True:
            print("\n" +"*******" +" National Law University " + "******" )
            
            print("1. About" ) 
            print("2. Departments" )
            print("3. Course" )
            print("4. Admission")
            print("5. Faculty" )
            print("6.  Go Back ") 
            input_6 = input("Please Select Your Options:  \n ").upper()
            if (input_6 == '1'):
                print("Location: New Delhi")
                print("Established: 2008")
                print("Specialization: Legal")
                print("Ranking: NIRF ranked 2nd among Law college in 2020")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.lawUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
    
            elif (input_6 == '2'):
                print("-> English")
                print("-> Political science")
                print("-> Economics") 
                print("-> Law and society")
                print("-> admistrative Law ")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.lawUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '3'):
                print("1. Undergraduate \n Programme: B.A LL.B \n Year : 5 \n Semester :10")
                print("2. Postgraduate \n Programme:LL.M \n Year : 1 \n Semester :1")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.lawUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '4'):
                print("For Undergraduate B.A LL.B courses based on AILET rank")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.lawUniversity()
                else:
                    print("invalid !! Please Enter 6:")
            elif (input_6 == '5'):
                print("Professor of law & register : Prof.Dr. Harpreet kaur \n Qualification :M.Sc ,LL.B,LL.M(Commercial law),LL.D(company law)")
                print("Professor pf political science : Prof. Dr. Maheshwar Singh \n Qualification : M.A ,PhD in JNU")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.lawUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '6'):
                print("\n" * 2)
                self.delhi()
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(input_6) + "). Try again!")

#********************************* JHARKHAND *************************************
    def jharkhand(self):
        while True:
            print("\n""*******" +"Jharkhand" + "******" )
            
            print("1. Binod Bihari Mahto Koyalanchal University" ) 
            print("2. Jharkhand Raksha  Shakti University" ) 
            print("3. Go Back ") 
            input_5 = input("Please Select Your Options:  \n ").upper()
            if (input_5 == '1'):
                print("\n" * 2)
                self.binodUniversity()
            elif (input_5 == '2'):
                print("\n" * 2)
                self.rakshaUniversity()
            elif (input_5 == '3'):
                print("\n" * 2)
                self.selectState()
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_5) + "). Try again!")

#*********************************    Binod Bihari Mahto Koyalanchal University   **************************

    def binodUniversity(self):
    # print(userdetails)
        while True:
            print("\n" +"*******" +" Binod Bihari Mahto Koyalanchal University" + "******" )
            
            print("1. About" ) 
            print("2. Departments" )
            print("3. Course" )
            print("4. Admission")
            print("5. Faculty" )
            print("6. Go Back ") 
            input_6 = input("Please Select Your Options:  \n ").upper()
            if (input_6 == '1'):
                print("Location: Dhanbad")
                print("Established: 2017")
                print("Specialization: General")
                print("Affilited colleges: as of 2021 ,the university has 10 consituent colleges ,20 affiliated colleges and 26 B.Ed colleges")
                print("Facility: Computer Center, Bank ,Library")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.binodUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
    
            elif (input_6 == '2'):
                print("-> Department of education")
                print("-> Mass communication")
                print("-> Art & culture") 
                print("-> Law")
                print("-> Foreign languages ")
                print("-> Disaster management")
                print("-> Enviromental science")
                print("-> Computer science")

                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.binodUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '3'):
                print("1. Undergraduate \n Programme: B.Sc ,B.A,B.ComYear : 3, Semester :6 \n Programme:B.A L.LB ,Year : 5, Semester :10\n Programme:BBA ,Year : 3, Semester :6  ")
                print("2. Postgraduate \n Programme:M.sc,M.A \n Year : 2 \n Semester :4")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.binodUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '4'):
                print("For Undergraduate B.sc ,L.LB,BBA ,BA courses based on entrance rank and intermediate result")
                print("For Postgraduate M.sc,M.A courses based on entrance test")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.binodUniversity()
                else:
                    print("invalid !! Please Enter 6:")
            if (input_6 == '5'):
                print("Head of math deaprtment: Dr. Rajesh kumar tiwari \n Qualification :Phd in Mathematics")
                print("HOD of Department of foreign languages:Dr. Hiamanshu shekhar choudhary \n course offered: M.A in French/German/japanese studies")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.binodUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '6'):
                print("\n" * 2)
                self.jharkhand()
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(input_6) + "). Try again!")

#****************************    Jharkhand Raksha  Shakti University  *************************

    def  rakshaUniversity(self):
    # print(userdetails)
        while True:
            print("\n" +"*******" +"  Jharkhand Raksha  Shakti University " + "******" )
            
            print("1. About" ) 
            print("2. Departments" )
            print("3. Course" )
            print("4. Admission")
            print("5. Faculty" )
            print("6. Go Back ") 
            input_6 = input("Please Select Your Options:  \n ").upper()
            if (input_6 == '1'):
                print("Location: Ranchi")
                print("Established: 2016")
                print("Specialization: Police science,internal security")
                print("Facility: Bank, Ground ,Library")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.rakshaUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
    
            elif (input_6 == '2'):
                print("-> Department of Criminology")
                print("-> Department of Forensic science")
                print("-> Department of Cyber security") 
                print("-> Department of Police Science")
                print("-> Department of Security Management")
                print("-> Department of Disaster management")
            
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.rakshaUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '3'):
                print("1. Undergraduate \n Programme: B.Sc ,B.B.A \n Year : 3 \n Semester :6   ")
                print("2. Postgraduate \n Programme:M.sc,M.A \n Year : 2 \n Semester :4")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.rakshaUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '4'):
                print("For Undergraduate  B.Sc ,B.B.A courses based on entrance test and intermediate result")
                print("For Postgraduate M.sc,M.A courses based on entrance test ranked")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.rakshaUniversity()
                else:
                    print("invalid !! Please Enter 6:")
            if (input_6 == '5'):
                print("Assistent professor department in computer science : Dr. Prabhash kumar  \n Qualification :Phd in IT from BRABU")
                print("Assistent professor department in police science: prof. Rohit Raj \n Qualification : completed his master's degree in public adminstration frpm political science from new delhi")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.rakshaUniversity()
                else:
                    print("invalid !! Please Enter 6")
            elif (input_6 == '6'):
                print("\n" * 2)
                self.jharkhand()
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(input_6) + "). Try again!")

#**************************** madhya pradesh ****************

    def madhyapradesh(self):
    # print(userdetails)
        while True:
            print("\n""*******" +" Madhyapradesh" + "******" )
            
            print("1. Dr. B. R Ambedkar University of Social sciences" ) 
            print("2. Sachi University of Buddhist-Indic Studies" ) 
            print("3. Go Back ") 
            input_5 = input("Please Select Your Options:  \n ").upper()
            if (input_5 == '1'):
                print("\n" * 2)
                self.ambedkarUniversity()
            elif (input_5 == '2'):
                print("\n" * 2)
                self.sachiUniversity()
            elif (input_5 == '3'):
                print("\n" * 2)
                self.selectState()
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(input_5) + "). Try again!")

#********************   Dr. B. R Ambedkar University of Social sciences  ************************
    def  ambedkarUniversity(self):
    # print(userdetails)
        while True:
            print("\n" +"*******" +"  Jharkhand Raksha  Shakti University " + "******" )
            
            print("1. About" ) 
            print("2. Departments" )
            print("3. Course" )
            print("4. Admission")
            print("5. Faculty" ) 
            print("6. Go Back") 
            input_6 = input("Please Select Your Options:  \n ").upper()
            if (input_6 == '1'):
                print("Location: Indore")
                print("Established: 2016")
                print("Specialization: Social science")
                print("Facility:  Ground ,Library,cafe")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.ambedkarUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
    
            elif (input_6 == '2'):
                print("-> Department of Social science")
                print("-> Department of Management")
                print("-> Department of English") 
                print("-> Department of History")
                print("-> Department of Economics")
                print("-> Department of Enviromental science")
            
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.ambedkarUniversity() 
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '3'):
                print("1. Undergraduate \n Programme: B.com ,B.A \n Year : 3 \n Semester :6   ")
                print("2. Postgraduate \n Programme:M.A \n Year : 2 \n Semester :4")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.ambedkarUniversity()
                else:
                    print("invalid !! Please Enter 6")
            elif (input_6 == '4'):
                print("For Undergraduate B.com ,B.A courses based on entrance test")
                print("For Postgraduate M.sc,M.A courses based on entrance test of university")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.ambedkarUniversity()
                else:
                    print("invalid !! Please Enter 6:")
            if (input_6 == '5'):
                print("Assistent professor & HOD ofdepartment in Philosophy : Dr. Kaushlendra Verma \n Qualification :Phd in Philoshapy")
                print("Assistent professor department in agriculture:Dr. Arun kumar \n Qualification : Gold medialist,Phd from BHU,Varanas")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.ambedkarUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '6'):
                print("\n" * 2)
                self.madhyapradesh()
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_6) + "). Try again!")

#**************************** Sachi University of Buddhist-Indic Studies ****************
    def  sachiUniversity(self):
    # print(userdetails)
        while True:
            print("\n" +"*******" +"   Sachi University of Buddhist-Indic Studies " + "******" )
            
            print("1. About" ) 
            print("2. Departments" )
            print("3. Course" )
            print("4. Admission")
            print("5. Faculty" )
            print("6. Go Back ") 
            input_6 = input("Please Select Your Options:  \n ").upper()
            if (input_6 == '1'):
                print("Location: Sanchi")
                print("Established: 2013")
                print("Specialization:Buddhism")
                print("Facility: Ground ,Library,hostel,guest house")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.sachiUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
    
            elif (input_6 == '2'):
                print("-> Department of Buddhism Studies")
                print("-> Department of Hindi")
                print("-> Department of English") 
                print("-> Department of indian painting")
                print("-> Department of Sanskrit & chinese language")
                print("-> Department of Yoga & Ayurveda")
            
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.sachiUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '3'):
                print("1. Diploma \n Programme: Diploma,Pg diploma \n Year : 2 \n Semester :4   ")
                print("2. Postgraduate \n Programme:M.sc,M.A \n Year : 2 \n Semester :4")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.sachiUniversity() 
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '4'):
                print("For  Diploma,Pg diploma courses based on entrance test ")
                print("For Postgraduate M.sc,M.A courses based on entrance test ranked")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.sachiUniversity()
                else:
                    print("invalid !! Please Enter 6:")
            if (input_6 == '5'):
                print("Assistent professor department in English : Dr. Navin kumar mehta \n Qualification :He is UGC-NET & SLET qualified")
                print("Head & Assistent professor department in Buddism:Dr. Santosh Proyadarshi \n Qualification :  Ph.D in Pali")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.sachiUniversity()
                else:
                    print("invalid !! Please Enter B ")
            elif (input_6 == '6'):
                print("\n" * 2)
                self.madhyapradesh()
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(input_6) + "). Try again!")    
 #   **************************** KARNATAKA ****************

    def karnataka(self):
    # print(userdetails)
        while True:
            print("\n""*******" +"  KARNATAKA " + "******" )
            
            print("1. Bengaluru North University" ) 
            print("2. Karnataka Sanskrit University" ) 
            print("3. Go Back ") 
            input_5 = input("Please Select Your Options:  \n ").upper()
            if (input_5 == '1'):
                print("\n" * 2)
                self.northUniversity()
            elif (input_5 == '2'):
                print("\n" * 2)
                self.karnatakaUniversity()
            elif (input_5 == '3'):
                print("\n" * 2)
                self.selectState()
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(input_5) + "). Try again!")

#********************  Bengaluru North University  ************************

    def  northUniversity(self):
    # print(userdetails)
        while True:
            print("\n" +"*******" +"  Bengaluru North University " + "******" )
            
            print("1. About" ) 
            print("2. Departments" )
            print("3. Course" )
            print("4. Admission")
            print("5. Faculty" )
            print("6. Go Back ") 
            input_6 = input("Please Select Your Options:  \n ").upper()
            if (input_6 == '1'):
                print("Location: Kolar")
                print("Established: 2017")
                print("Specialization: General")
                print("Facility: sports ,Library,park")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.northUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
    
            elif (input_6 == '2'):
                print("-> Department of Social science")
                print("-> Department of Management")
                print("-> Department of English") 
                print("-> Department of History")
                print("-> Department of Economics")
                print("-> Department of Enviromental science")
            
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.northUniversity() 
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '3'):
                print("1. Undergraduate \n Programme:B.sc B.com ,B.A \n Year : 3 \n Semester :6   ")
                print("2. Postgraduate \n Programme:M.sc,M.A \n Year : 2 \n Semester :4")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.northUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '4'):
                print("For Undergraduate B.sc,B.com ,B.A courses based on entrance test")
                print("For Postgraduate M.sc,M.A courses based on entrance test of university")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.northUniversity()
                else:
                    print("invalid !! Please Enter 6:")
            if (input_6 == '5'):
                print(" HOD of department in History : Dr. Rajesh ray\n Qualification :Phd in History")
                print("Assistent professor department in Hindi:Dr. Suraj kumar \n Qualification : Gold medialist,Phd from JNU")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.northUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '6'):
                print("\n" * 2)
                self.karnataka()
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(input_6) + "). Try again!")

#******************  karnataka samskrit University  ***********************
    def  karnatakaUniversity(self):
    # print(userdetails)
        while True:
            print("\n" +"*******" +" karnataka samskrit University " + "******" )
            
            print("1. About" ) 
            print("2. Departments" )
            print("3. Course" )
            print("4. Admission")
            print("5. Faculty" )
            print("6. Go Back ") 
            input_6 = input("Please Select Your Options:  \n ").upper()
            if (input_6 == '1'):
                print("Location:Bangalore")
                print("Established: 2011")
                print("Specialization:Sanskrit")
                print("Facility: sports ,Library,ground")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.karnatakaUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
    
            elif (input_6 == '2'):
                print("-> Department of Vyakarana")
                print("-> Department of Yogashastra")
                print("-> Department of Nyaya and Vaisheshika")
            
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.karnatakaUniversity() 
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '3'):
                print("1. Undergraduate \n Programme:,B.A \n Year : 3 \n Semester :6   ")
                print("2. Postgraduate \n Programme:M.A \n Year : 2 \n Semester :4")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.karnatakaUniversity() 
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '4'):
                print("For UndergraduateB.A courses based on entrance test")
                print("For Postgraduate M.A courses based on entrance test of university")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.karnatakaUniversity() 
                else:
                    print("invalid !! Please Enter 6:")
            if (input_6 == '5'):
                print(" HOD of department in Vyakarana : prof. Shivani V. \n Qualification :Phd in Sanskrit")
                print("Assistent professor department in Alankara:prof. Bheemanaik S \n Qualification :Phd in sanskrit")
                input_n= input("6. Go Back: \n ").upper()
                if(input_n == '6'):
                    self.karnatakaUniversity()
                else:
                    print("invalid !! Please Enter 6 ")
            elif (input_6 == '6'):
                print("\n" * 2)
                self.karnataka()
            else:
                print("\n" *2 + "ERROR: Invalid Input (" + str(input_6) + "). Try again!")



u1 = University()
# u1.universityDetails()
# u1.selectState()
# u1.delhi()
# u1.indragandhiUniversity()
# u1.technologicalUniversity()
# u1.lawUniversity()
# u1.jharkhand()
# u1.binodUniversity()
# u1.rakshaUniversity()
# u1.madhyapradesh()
# u1.ambedkarUniversity()
# u1.sachiUniversity()
# u1.karnataka()
# u1.northUniversity()
# u1.karnatakaUniversity()