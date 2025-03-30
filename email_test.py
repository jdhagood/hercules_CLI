import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Outlook SMTP settings
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587  # TLS

EMAIL_ADDRESS = "jdhagood@mit.edu"
EMAIL_PASSWORD = "PagePlan99"  # Preferably use an app password

# List of recipients
recipients = ["jdhagood104@gmail.com"]

# Email content
subject = "Hello from Python"
body = "This is a test email sent using Python via Outlook SMTP!"

# Function to send email
def send_email(to_email):
    try:
        # Create MIME message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to Outlook SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login

        # Send email
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        print(f"Email sent to {to_email}")

        # Close the connection
        server.quit()

    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

# Send emails to all recipients
for email in recipients:
    send_email(email)
