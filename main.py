import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from fetch_emails import get_unread_emails
from summarize import summarize_emails

def send_email(summary_text):
    sender_email = os.getenv("GMAIL_ADDRESS")
    app_password = os.getenv("GMAIL_APP_PASSWORD")

    # Create the email format
    msg = MIMEText(summary_text)
    msg["Subject"] = "Your Daily AI Email Summary"
    msg["From"] = sender_email
    msg["To"] = sender_email  # Sending it to yourself

    # Connect to Gmail's Outgoing server and send
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

def main():
    load_dotenv()
    
    print("Fetching unread emails...")
    email_content = get_unread_emails()
    
    if not email_content:
        print("No new emails.")
        return
        
    print("Summarizing with Gemini...")
    summary = summarize_emails(email_content)
    
    print("Sending summary email...")
    send_email(summary)
    print("Done! Email sent.")

if __name__ == "__main__":
    main()