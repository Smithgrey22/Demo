import smtplib

SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 465

try:
    server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    server.login("financeoffical@yahoo.com", "plmzapspqrerxqdg")  # Replace with actual credentials
    print("✅ Yahoo SMTP connection successful!")
    server.quit()
except Exception as e:
    print(f"❌ SMTP connection error: {e}")
