#AUTHENTICATE LOGIN PASSWORD

    
def checkLoginPassword(email,password):

    f = open("data.csv","r")
    count = 0
    for line in f.read():
        if email in line:
            break
        count = count + 1

    if password in f.read():
        print("")
    else:
        return False
    
    print("Recognizes Password in Database")
    count2 = 0

    for line in f.read():
        if password in line:
            break
        count2 = count2 + 1

        
    if count2 == count:
        return True
    else:
        return False

    f.close()


        
#AUTHENTICATE EMAIL

def checkEmail(email):

    #opens file
    f = open("data.csv","r")
    
    if email in f.read():
        return 3
    if "@" not in email:
        return False
    if "." not in email.split('@')[1]:
        return False

    return True

    f.close()
        
#CONDITIONS LIST



def conditionList():
    #opens file
    f= open("data.csv","r")

    conditions = []

    #reads file and creates list of unique conditions
    for line in f:
        cells = line.split(",")
        if cells[5] not in conditions:
            conditions.append(cells[5])
    f.close()

    return conditions[1:-1]

    #CREATE NEW ACCOUNT

def createnewaccount():
    firstName = raw_input("Enter First Name:")
    while(firstName.isalpha() == False):
            firstName = raw_input("Please enter a valid name. No numbers allowed!")
    lastName = raw_input("Enter Last Name:")
    while(lastName.isalpha() == False):
            lastName = raw_input("Please enter a valid name. No numbers allowed!")

    name = firstName + " " + lastName


    age = raw_input("Enter Age:")

    while (age.isdigit() == False):
            print("Please enter a valid age")
            age = raw_input("Enter Age:")


    zipcode = (raw_input("Enter your Zip Code:"))

    while (zipcode.isdigit() == False or len(zipcode) != 5):
            zipcode = raw_input("Please enter a valid zipcode:")
        


    typeChoice = int(input("Choose a type for your account: \n1.) Coping \n2.) Educator \n3.) Learner\n"))

    while (typeChoice > 3 or typeChoice < 1):
            typeChoice = int(input("Please enter a valid input: "))



    if (typeChoice == 1):
            accountType = "Coping"
            ageMax = int(input("What is your maximum desired age for a partner? "))
            ageMin = int(input("What is your minimum desired age for a partner? "))
            #distPref = 1 if state is desired range and 2 if region is desired range
            while(ageMax<ageMin):
                ageMin = int(input("Incorrect value. Please try again: "))
            while ageMax <= 0:
                ageMax = int(input("Incorrect value. Please try again: "))
            while ageMin < 0:
                ageMin = int(input("Incorrect value. Please try again: "))
                
            distPref = int(input("What is your desired range for a partner?\n1.)State\n2.)Immediate Region\n"))

            print("What is your condition/disability?")
            conLength = len(conditionList())
            conditions = conditionList()
            for i in range(1, conLength):
                print(i,"-", conditions[i])
            conChoice = int(input())
            condition = conditions[conChoice]
        
    if (typeChoice == 2):
            accountType = "Educator"
            
            print("What is your condition/disability?")
            conLength = len(conditionList())
            conditions = conditionList()
            for i in range(1, conLength):
                print(i,"-", conditions[i])
            conChoice = int(input())
            condition = conditions[conChoice]
                
            
    if (typeChoice == 3):
            accountType = "Learner"

            print("What condition/disability would you like to learn about?")
            conLength = len(conditionList())
            conditions = conditionList()
            for i in range(1, conLength):
                print(i,"-", conditions[i])
            conChoice = int(input())
            condition = conditions[conChoice]

    email = raw_input("Please enter your email: ")

    #Checks to see if input is both valid and not already taken
    check = 0
    while check == 0:
        if checkEmail(email)==False:
            email = raw_input( "Invalid email. Please try again: " )
        if checkEmail(email)==3:
            email = raw_input( "Email already taken. Please try again: ")
        if checkEmail(email)==True:
            check = 1
    password = raw_input("Enter your password:\n")

    f = open("data.csv","a")
    f.write("\n" + email + "," + password + "," + name + "," + age + "," + zipcode + "," + condition + "," + accountType)

createnewaccount()




