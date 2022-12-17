#We are creating a python script that helps us to simulate a dice
#PRO-C101 -- Projct made by Avinash Kumar
import random
consentFromUser = "y"
def rollthedice(consentFromUser):
    while consentFromUser == "y":
        #The code is a little diffrenet from the code provided in the project cause its, my style
        randomedicenumber = random.randint(1,6)
        if randomedicenumber == 1:
            print("---")
            print("   ")
            print(" 0 ")
            print("   ")
            print("---")
        elif randomedicenumber == 2:
            print("---")
            print("0  ")
            print("   ")
            print("  0")
            print("---")
        elif randomedicenumber == 3:
            print("---")
            print("0  ")
            print(" 0 ")
            print("  0")
            print("---")
        elif randomedicenumber == 4:
            print("---")
            print("0 0")
            print("   ")
            print("0 0")
            print("---")
        elif randomedicenumber == 5:
            print("---")
            print("0 0")
            print(" 0 ")
            print("0 0")
            print("---")
        elif randomedicenumber == 6:
            print("---")
            print("0 0")
            print("0 0")
            print("0 0")
            print("---")
        consentFromUser = input("Write y to roll dice and n to exit")
rollthedice(consentFromUser)
