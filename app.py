from flask import Flask, request, render_template, jsonify
import sendgrid
import os
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# SendGrid API Key
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

def send_email(to_email, amount, sender_name):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    subject = "Bank Account Credit Notification"
    content = f"Dear Customer,\n\nYour account has been credited with ${amount} from {sender_name}.\n\nThis is a simulated transaction."

    mail = Mail(from_email=SENDER_EMAIL, to_emails=to_email, subject=subject, plain_text_content=content)
    response = sg.send(mail)
    return response.status_code

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        recipient_email = request.form["email"]
        amount = request.form["amount"]
        sender_name = request.form["name"]
        
        send_email(recipient_email, amount, sender_name)
        return jsonify({"message": "Transaction successful! Email sent."})
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
