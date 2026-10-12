contacts={}
while True:
    print("\n contact management system")
    print("1.Add contact")
    print("2.search contact")
    print("3.upadate contact")
    print("4.delete contact")
    print("5.display contact")
    print("6.Exit")
    options=int(input("Enter you are option"))
    if(options==1):
        name=input("Enter your name")
        phone=input("Enter your number")
        contacts[name]=phone
        print("contact added successfuly!")
    elif(options==2):
        name=input("Enter Your name:")
        if name in contacts:
            print("phone:",contacts[name])
        else:
             print("contact not found")
    elif (option==3):
           name=intput("Enter Your name:")
           if name in contacts:
               phone=intput("Enter Your new phone:")
               contacts[name]=phone
               print("updated Your new contact successfully")
           else:
               print("contact not found")
    elif (option==4):
            name=input("Enter Your name:")
            if name in contacts:
                del contacts[name]
                print("Deleted Your contact successflly")
            else:
                  print("contact not found")
    elif(option==5):
              name=input("enter Your name")
              for  name,phone in contacts.items():
               print(name,"\t",phone)
    elif (option==6):
            print("Thankyou")
    else:
            print("Invalid")
             
