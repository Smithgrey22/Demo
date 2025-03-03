from flask import Flask, request, render_template
import smtplib

app = Flask(__name__)

# Yahoo SMTP Configuration
SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 465
EMAIL_ADDRESS = "financeoffical@yahoo.com"  # Replace with your Yahoo email
EMAIL_PASSWORD = "plmzapspqrerxqdg"  # Use Yahoo App Password!

def send_email(to_email, subject, message):
    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        email_body = f"Subject: {subject}\n\n{message}"
        server.sendmail(EMAIL_ADDRESS, to_email, email_body)
        server.quit()
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        recipient_email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        success = send_email(recipient_email, subject, message)
        if success:
            return "✅ Email sent successfully!"
        else:
            return "❌ Failed to send email. Check your settings."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
