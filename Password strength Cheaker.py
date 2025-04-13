print("Welcome to password strength checker:")

#Input from user
password=input("Enter your password:")

#Initial score
score=0

#Check Length
if len(password) >=8:
    print(f"len of password:{len(password)} ")
    score+=1

#Check for number
if(
    "0" in password or
    "1" in password or
    "3" in password or
    "4" in password or
    "5" in password or
    "6" in password or
    "7" in password or
    "8" in password or
    "9" in password 
    
):
    score +=1
        
