import smtplib

senderEmail = "youremail@email.com"
receiverEmail = "receiveremail@email.com"
key = "yourkey"
message = "Hello World"
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(senderEmail, key)
s.sendmail(receiverEmail, senderEmail, message)
print('Email Sent')