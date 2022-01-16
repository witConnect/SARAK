import smtplib
def send_email(OTP,from_address,to_address):
    s = smtplib.SMTP('smtp.gmail.com', 587)  
    s.ehlo()
    s.starttls() 
    s.ehlo()
    s.login(from_address,"Gr8stofa11time") 
    sub = "Message from SARAK"
    message = f"Subject:{sub} \n\n Your OTP for reseting the password is {OTP}"
    s.sendmail(from_address, to_address, message) 
    s.quit() 
    print("Mail sent")
