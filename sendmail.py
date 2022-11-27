import smtplib
 
# list of email_id to send the mail
li = ['example@gmail.com']

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("emailaddress", "password")
    message = "Renewable Energy And Electric Cars \n Welcome to FIRSTTELLING \n This site provides information about how you could save money using renewable energy.\n Discover how electric cars work n\ Learn about the benefits and future of electric car driving.\n Please visit http://firsttelling.com.\n To your success fimr"
    s.sendmail("sender_email", dest, message)
    s.quit()