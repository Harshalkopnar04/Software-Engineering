import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('harshalkopnar222@gmail.com','yrcgcsrscfliihzb')
otp = random.randrange(100000, 1000000)

message = "OTP for login is "+str(otp)
server.sendmail('harshalkopnar222@gmail.com','chhaya102@gmail.com',message)
server.quit()
user = int(input("Enter the OTP: "))
if(user == otp):
    print("Access granted!")
else:
    print("Access Denied!")
