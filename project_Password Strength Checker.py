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

#Cheak for Uppercase
if(
    "A" in password or
    "B" in password or
    "C" in password or
    "D" in password or
    "E" in password or
    "F" in password or
    "G" in password or
    "H" in password or
    "I" in password or
    "J" in password or
    "K" in password or
    "L" in password or
    "M" in password or
    "N" in password or
    "O" in password or
    "P" in password or
    "Q" in password or
    "R" in password or
    "S" in password or
    "T" in password or
    "U" in password or
    "V" in password or
    "W" in password or
    "X" in password or
    "Y" in password or
    "Z" in password 
):
    score=score+1

#Cheak forlowercase
if(
    "a" in password or
    "b" in password or
    "c" in password or
    "d" in password or
    "e" in password or
    "f" in password or
    "g" in password or
    "h" in password or
    "i" in password or
    "j" in password or
    "k" in password or
    "l" in password or
    "m" in password or
    "n" in password or
    "o" in password or
    "p" in password or
    "q" in password or
    "r" in password or
    "s" in password or
    "t" in password or
    "u" in password or
    "v" in password or
    "w" in password or
    "x" in password or
    "y" in password or
    "z" in password  
):

    score=score+1

#Cheak for special Character
if(
    "/" in password or
    "?" in password or
    "@" in password or
    "!" in password or
    "<" in password or
    ">" in password or
    "," in password or
    "." in password or
    "|" in password or
    "-" in password or
    "_" in password or
    "+" in password or
    "=" in password or
    "*" in password or
    "#" in password or
    "$" in password or
    "%" in password or
    "^" in password or
    "&" in password or
    "()" in password or
    "{}" in password or
    "[]" in password or
    "'" in password or
    ":" in password or
    ";" in password
    
):
    score=score+1

if score ==5:
    print("Password is 🔒 strong")

elif score >=3:
    print("The password is ⚠ medium")

else:
    print("The password is ❌ Weak")


     
        