import smtplib
def sendMail(subject,body,recipient_email):
        
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Log in to your Gmail account
        server.login('sabilhasan2018@gmail.com', 'apppassword')

        # Compose your email message

        message = f'Subject: {subject}\n\n{body}'

        # Sender and recipient email addresses
        sender_email = 'sabilhasan2018@gmail.com'
        recipient_email = 'it18021@mbstu.ac.bd'

        # Send the email
        server.sendmail(sender_email, recipient_email, message)
        print("Email sent successfully.")

        # Close the connection
        server.quit()
    except Exception as e:
        print("Error:", str(e))
if __name__=="__main__":
    sendMail("Account verify","This is a testing","it18021@mbstu.ac.bd")