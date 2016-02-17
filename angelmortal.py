import random
import copy
import csv
import smtplib
from email.mime.text import MIMEText as text
import email.message

final = {}
hold = []
holdcpy = []
repeats = []
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
emailtemplate = \
"EMAIL CONTENT"
with open ('Desktop/angelmortal.csv', 'r') as infile:
    for line in infile:
        details = line.rsplit(',',1)
        # details[0] = name, details[1] = email
        hold.append(details[0])
        final[details[0]] = [details[1],]

for i in range(3):
    holdcpy = copy.deepcopy(hold)
    random.shuffle(holdcpy)
    for name, emailarr in final.iteritems():
        # if repeat
        if name == holdcpy[0]:
            emailarr.append(holdcpy.pop(1))
        else:
            emailarr.append(holdcpy.pop(0))

check = False
checkpoint = True
#checking
for name, emailarr in final.iteritems():
    if name in emailarr:
        checkpoint = False

if checkpoint:
    check = True
counter = 0
print check
if check:
    server.login("YOUREMAILADDRESS", "YOUREMAILPASSWORD")
    with open('Desktop/angelmortalfinal.csv' , 'w') as infile:
        writer = csv.writer(infile)
        for key, value in final.iteritems():
            temp = [el for el in value]
            temp[0] = temp[0].rstrip()
            temp.insert(0, key)
            writer.writerow(temp)

    for name, emailarr in final.iteritems():
        
        m = text(emailtemplate)
        sender = "YOUREMAILADDRESS"
        receipient = emailarr[0]
        m['From'] = sender
        m['To'] = receipient
        m['Subject'] = "Hall Production Angel-Mortal"
        server.sendmail(sender, [receipient], m.as_string())  

        print counter
        counter += 1
 
            
print "done"       
