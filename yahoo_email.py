import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Yahoo SMTP Configuration
SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 465  # Use SSL
EMAIL_ADDRESS = "financeoffical@yahoo.com"
EMAIL_PASSWORD = "plmzapspqrerxqdg"  # Use Yahoo App Password

def send_email(to_email, subject, message):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject  # ✅ Correct
    msg.attach(MIMEText(message, "plain"))

    try:
        # Connect to Yahoo SMTP Server
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)  # Use SSL
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())  # Send email
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

# Example Usage
send_email("gaboy4553@gmail.com", "Test Email", "Hello, this is a test email from Yahoo Mail SMTP!")
