code = 1234
i = 1

while i < 3:
    password = int(input("Enter your 4-digit password: "))

    if password == code:
        print ("Wellcome!")
        break
       

    elif password == 4321:
        print("police is here :)")
        break
        

    elif i < 3 :
        print ("Error! please try again.")
        

    elif i == 3:
        print(" Your account have been locked!")
        


    else:
        i = i + 1