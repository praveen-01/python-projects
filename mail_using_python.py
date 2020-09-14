import smtplib  
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
mail=input("please enter e mial id: ")
pass1=input("please enter password: ")
s.login(mail,pass1) 
message = "This mail sent using python smptplib"
user=input("Enter the senders mail id")
s.sendmail(mail, user, message) 
s.quit() 
