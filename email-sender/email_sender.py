import smtplib # Import the smtplib module for sending emails

to = input("Enter the recipient's email address:\n ")  # Get the recipient's email address from user input
content = input("Enter the content of the email:\n ")  # Get the content of the email from user input

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the Gmail SMTP server
    server.ehlo() # Make the communication with the SMTP server of the Gmail
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login('senderemail@gmail.com', 'password')  # Log in to the sender's email account
    server.sendmail('senderemail@gmail.com', to, content)  # Send the email from the sender to the recipient
    server.close()  # Close the connection to the SMTP server

sendEmail(to, content)  # Call the function to send the email with the provided recipient and content