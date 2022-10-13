userlist = []
class Registration():
    def register(self):
        self.name = input("Enter Name: ")
        self.PhoneNumber = input("Enter your Phone Number: ")
        self.Email = input("Enter your Email Id: ")
        self.Password = input("Create password: ")
        self.Password1 = input("Confirm password: ")

    # userdetails.append([Fullname,PhoneNumber,AdharNumber,PanNumber,Email,Address])


#------------------Phone Number-----------------------
        if len(self.PhoneNumber) != 10:
            print("Please Enter valid Phone Number")
            self.register()
        
    #------------------Password---------------------------     
        if self.Password != self.Password1:
            print("Passwords don't match, Please Re-Enter")
            self.register()
        else:
            try:
                if len(self.Password)<=6:
                    print("Password too short, restart: ")
                    self.register()
            except:
                print("correct password !! \n")
            else:
                print(" Registered successfully!! \n")
        userlist.append([self.name,self.Password])
        # print(userlist)
       

r1 =  Registration()
# r1.register()
