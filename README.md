# send_mail
A simple but, I think useful, sending emails using Python and SMTP project
In the first file you will install SMTP, protocol to used for sending emails.
import smtplib
 
# list of email_id to send the mail
li = ['peerbrw@gmail.com',]
In the second line I inserted a list(li) of email addresses where you have to send the messages. The list has no number limit.

The second file of project called sendmail.py  is a foor loop:

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("emailaddress", "password")
    message = "Renewable Energy And Electric Cars \n Welcome to FIRSTTELLING \n This site provides information about how you could save money using renewable energy.\n Discover how electric cars work n\ Learn about the benefits and future of electric car driving.\n Please visit http://firsttelling.com.\n To your success fimr"
    s.sendmail("sender_email", dest, message)
    s.quit()
    
    The domain name for the SMTP server will usually be the name of your email provider’s domain name, with smtp. in front of it.(Gmail*

smtp.gmail.com). The port is an integer value and will almost always be 587. You need to calls starttls() method next.
For login insert your address and password(I use gmail app password). 
The message is mine, you need to change it. It is possible to use text file insted of string text but I have used a link here. 
Finally, you call sendmail() method, and the message is sending to the number of addresses from li list.

Bonus:To generate plenty of gmail addresses use the bellow Python code. Insert different names and you will receive dozen of dates
from itertools import combinations

first_name =''
last_name = ''
name = first_name + last_name


for ea in combinations(name, 7):
    print(''.join(ea) + '@gmail.com', end=' ')
    
    
    Mircea
