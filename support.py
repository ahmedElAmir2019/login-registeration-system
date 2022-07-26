import re
dic = {}

def user_email():
    valid_email = re.compile(r"\.\+\,")
    with open('credenials.txt', 'r') as wf:
        for line in wf:
            email = line
            passw = email[line.find(',')+1:-1]
            email = email[:email.find(",")]
            dic[email] = passw
    wf.close()

def login():
    user_email()
    counter = 3
    while counter>0:
        email = input("please enter your mail :")
        password = input("please enter your password :")
        if email in dic:
            if password == dic[email]:
                print("welcome" + email)
                break
            else:
                counter = counter - 1
                print("try again.")
        else:
            counter = counter - 1
            print("try again.")
    if counter ==0:
        print("the service is blocked temporarily.")

def writing(email,password):
    lis=[]
    lis.append(email+","+password+"\n")
    with open('credenials.txt', 'r') as wf:
       for line in wf :
           lis.append(line+"\n")
    wf.close()
    with open('credenials.txt','w') as wf:
        for i in lis:
            wf.write(i)
    wf.close()
def mail_checker(email):
    chek=False
    if (re.search(r"\!|\#|\$|\%|\^|\&|\*|\(|\)|\"|\'|\:|\;|\{|\}|\\|\||\?|\/|\>|\<|\,|\/|\*|\-|\+|\~", email) != None):
        chek=False
    valid_emai=re.compile(r"[A-z0-9\._]+@[A-z0-9]+\.(com|net)")
    if(re.search(valid_emai,email)!=None):
        chek = True
    return chek
def password_checker(password):
    valid_password=re.compile(r"^[A-Z]+[A-z0-9\!|\#|\$|\%|\^|\&|\|\?|\'|\"]*")
    if(re.search(valid_password,password)!=None and re.search(r"[\!|\#|\$|\%|\^|\&|\|\?|\'|\]|\@]",password)!=None and re.search(r"[0-9]",password)!=None):
        return True
    else: return False
def sign_up(email,password):
    email_valid=mail_checker(email.lower())
    password_valid=password_checker(password)
    if email_valid and password_valid :
        print("Welcom"+email)
        writing(email,password)
def registeration():
    email = input('please enter your mail :')
    password = input("please enter your password :")
    sign_up(email,password)
while True:
    choice = input("please enter your choice login press 1 registeration press 2 exit press 3")
    if int(choice)==1:
        login()
    elif int(choice)==2:
        registeration()
    elif int(choice)==3:
        break
    else:
        print("try again")