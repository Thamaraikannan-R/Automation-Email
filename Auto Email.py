import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#return redirect(url_for('success',name = user))
me = "rtkcse2@gmail.com"
you = "rtkcse@gmail.com"

       # Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Subject"
msg['From'] = me
msg['To'] = you
html = """\
welcome
"""
part1 = MIMEText(html,'html')
msg.attach(part1)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('rtkcse2@gmail.com', 'kannankannan')
mail.sendmail(me, you, msg.as_string())
print("Sucessfully email Sent")