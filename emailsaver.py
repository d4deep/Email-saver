def log():
    count=0
    while True:
        email_id=input("Email Id: ")
        passwd=input("Password: ")
        count+=1
        with open("mail.txt","a") as m:
            m.write("Email Id: " + email_id + "\n")
            m.write("Password: " + "(" + passwd + ")" + "\n")
        print("saved Successfully!")
        ans=input("Do you want to add more details\nY\nN: ")
        if ans=='n':
            break

def retrieve():
    while True:
        with open("mail.txt") as m:
            for item in m:
                print(item)
        ans = input("Do you want to View details again\nY\nN: ")
        if ans == 'n':
            break

while True:
    print("Welcome to Email Saver\nYou save Your Emails and password safely with the help of this tool")
    print('''  ______                _ __   _____                      
   / ____/___ ___  ____ _(_) /  / ___/____ __   _____  _____
  / __/ / __ `__ \/ __ `/ / /   \__ \/ __ `/ | / / _ \/ ___/
 / /___/ / / / / / /_/ / / /   ___/ / /_/ /| |/ /  __/ /    
/_____/_/ /_/ /_/\__,_/_/_/   /____/\__,_/ |___/\___/_/     
~~~~~~~~~~~~~~~~~Created By Deep Verma~~~~~~~~~~~~~~~~~~''')
    x=int(input("Type 1 for log and 2 for retrieve: "))
    if x==1:
        log()
    elif x==2:
        retrieve()
    else:
        print("Something Wrong!")
    ans=input("Do want to Again Log or Retrieve\nY\nN: ")
    if ans=='n':
        print("Good Bye!")
        break
