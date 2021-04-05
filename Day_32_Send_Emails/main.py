import smtplib
import ssl
import datetime as dt
import random



my_email = "louiseuy015@gmail.com"
password = "bhosxzcheng_015"

# Generating a Quote message from the quotes.txt
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quote= quote_file.readlines()
        quote = random.choice(all_quote)
    
# Sending email with the message as the Quote
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="chellesea.uy@gmail.com", 
            msg= f"Subject: Monday Motivation\n\n {quote}"
            )


