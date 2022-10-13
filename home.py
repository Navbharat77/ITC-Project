from Reg import *
from log  import *
from university import *

class Homepage():
    def __init__(self):
        while True:
            print("\n" +"*******" +"home page" + "******" )
            
            print("1. University details " )   
            print("2. Contact us for equiry") 
            print("3. Exit ")
            input_2 = input("Please Select Your Options: ").upper()
            if (input_2 == '1'):
                print("\n" * 2)
                u1 = University()
                u1.universityDetails()
                u1.selectState()
                u1.delhi()
                u1.indragandhiUniversity()
                u1.technologicalUniversity()
                u1.lawUniversity()
                u1.jharkhand()
                u1.binodUniversity()
                u1.rakshaUniversity()
                u1.madhyapradesh()
                u1.ambedkarUniversity()
                u1.sachiUniversity()
                u1.karnataka()
                u1.northUniversity()
                u1.karnatakaUniversity()
                
            if (input_2 == '2'):
                f = open("file.txt","r")
                print(f.read())
                input_n = input("1. Go back to main page: ")
                if(input_n == '1'):
                    break

            #     ContactDetails()
            #     break
            elif (input_2 == '3'):
                print("*" * 32 + "THANK YOU FOR VISIT" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 2 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
        
        
    
while True:
    print("********" + "login page of University site" + "*********" "\n"    
        "\t 1. REGISTER\n"                             
        "\t 2. LOGIN\n"
        "\t 3. EXIT\n" +
        "")
    input_1 = (input("Please Select Your Options: ")).upper()
    if (input_1 == '1'):
        print("welcome to registration page")
        r1 = Registration() 
        r1.register()
        #m1 = Homepage()
    elif (input_1 == '2'):
        print("welcome to Login page")
        login1 = Login()
        login1.login()
        m1 = Homepage()   
        
    elif (input_1 == '3'):
        print("Thank you \n")
        # break


# m1 = Homepage()

