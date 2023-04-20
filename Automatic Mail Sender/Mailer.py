import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set your message
mesg = "Hi, Please find my new blog post about Exploratory Data Analysis of Zomato Dataset. " \
       "\n\nhttps://journeytotheai.wordpress.com/2023/04/04/exploratory-data-analysis-of-zomato-dataset-using-pandas/" \
       "\n\nThanks,\nPriya."

# Add your to and from mail addresses
from_mail = "<from_email_address>"
to_mail = ["<to_email_address1>", "<to_email_address2>"]

# Structuring the email using MIME
msg = MIMEMultipart()
msg["From"] = from_mail
msg["To"] = ', '.join(to_mail)
msg["Subject"] = "Exploratory Data Analysis of Zomato Dataset"
msg.attach(MIMEText(mesg, "plain"))

# Connecting to our Gmail using Smtplib

s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
s.starttls()
s.login('<from_email_address>', '<app_password>')
s.sendmail(from_mail, to_mail, msg.as_string())
s.quit()
