from Reg import *

class Login(Registration):
    def login(self):
        self.name = input("Please enter Name: ")
        for user in userlist:
            if self.name in user:
                self.Password = input("Please enter password: ")
                if self.Password in user:
                    print(" password matched ")
                    print(" Successfully login!!")
                    # self.homepage()
                else:
                    print("Incorrect password")
                
# r1 =  Registration()       
login1 = Login()
# r1.register()
# login1.login()
 