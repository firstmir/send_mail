# send_mail
#A simple but, I think useful, sending emails using Python and SMTP project


#In the first file you will install SMTP, protocol to used for sending emails.


import smtplib
 

# list of email_id to send the mail


li = ['example.@gmail.com',]



#In the second line I inserted a list(li) of email addresses where you have to send the messages. The list has no number limit.

#The second file of project called sendmail.py  is a foor loop:



for dest in li:

#The domain name for the SMTP server will usually be the name of your email provider’s domain name, with smtp. in front of it.(Gmail*

smtp.gmail.com). 


    s = smtplib.SMTP('smtp.gmail.com', 587)
	
#The port is an integer value and will almost always be 587.
    
	s.starttls()
	

# You need to calls starttls method next.
   
   
   s.login("emailaddress", "password")


#For login insert your address and password(I use gmail app password). 

   
   message = " "
    

#The message is mine, you need to change it. It is possible to use text file insted of string text but I have used a link here.	
	
	
	s.sendmail("sender_email", dest, message)


#Finally, you call sendmail() method, and the message is sending to the number of addresses from li list.
    
	s.quit()
    
    
	
	
	




Bonus:To generate plenty of gmail addresses use the bellow Python code. Insert different names and you will receive dozen of dates
#generator

from itertools import combinations

#insert firstname

first_name =''

#insert lastname

last_name = ''

#define name

name = first_name + last_name

#generate

for ea in combinations(name, 7):

#call
    
	print(''.join(ea) + '@gmail.com', end=' ')
    
    
    Mircea!
