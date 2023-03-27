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
    x=int(input("Type 1 for log and 2 for retrieve: "))
    if x==1:
        log()
    elif x==2:
        retrieve()
    else:
        print("Something Wrong!")
    ans=input("Do want to Again Log or Retrieve\nY\nN: ")
    if ans=='n':
        break
