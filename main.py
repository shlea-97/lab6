#Ariana Lea

def encoder():
    password = input()
    #password into list of integers
    password =[int(i) for i in password]
    code = 0
    coded_password=[]
    for i in password:
        code = i+3
        coded_password.append(code)
    #coded_password list into string
    coded_password =[str(i) for i in coded_password]
    #connect strings
    coded_password = "".join(coded_password)
    print(coded_password)
    
encoder()
