import random
import smtplib
# import unittest


# smptlib Gmail PORT
PORT = 587

# Importing my Email and Password
file = open("confidentialtxt.py", "r")
myEmail = ""
myPass = ""
for data in file:
    value = data.split(",")
    myEmail = value[0]
    myPass = value[1]

# Input of User Email Id
userEmail = input("Enter you Email id : ")

# Text message to be send
message = "Otp to login is "

try:
    # Validating the Email
    validated_email = validate_email(userEmail)
except:
    print("valid Email");


# Function for sending email to user
def sendEmailtoUser():
    server.sendmail(myEmail , userEmail , message + str(otp) )

    # Quiting the server after sending email
    server.quit();

def generateOtp():
    otp = random.randrange(1000,10000)
    return otp

try:
    server = smtplib.SMTP('smtp.gmail.com', PORT)
    server.starttls()
    server.login(myEmail,myPass)
    otp = generateOtp()
    
    # sending Email to User
    sendEmailtoUser()

    #Input from user to validate OTP
    isCorrectOtp = int(input(("Enter your Otp : ")))

    # Validating entered Otp
    if(isCorrectOtp == otp):
        print("Logged in Successfully!")
    else:
        print("Invalid Otp!")
except:
    print("An Exception occured!")