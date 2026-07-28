import imaplib
import email
from email.header import decode_header
import os
from datetime import datetime, timedelta

def get_unread_emails():
    username = os.getenv("GMAIL_ADDRESS")
    password = os.getenv("GMAIL_APP_PASSWORD")

    if not username or not password:
        raise ValueError("Missing Gmail credentials. Check your .env file.")

    # Connect to Gmail's IMAP server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    # Fetch unread emails from the last 24 hours
    date_since = (datetime.now() - timedelta(days=1)).strftime("%d-%b-%Y")
    status, messages = mail.search(None, f'(SINCE "{date_since}" UNSEEN)')

    email_data = []
    
    if status == "OK" and messages[0]:
        for num in messages[0].split():
            res, msg = mail.fetch(num, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg_obj = email.message_from_bytes(response[1])
                    
                    # Safely decode the subject line
                    subject_header = decode_header(msg_obj.get("Subject", "No Subject"))[0]
                    subject = subject_header[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(subject_header[1] or "utf-8", errors="ignore")
                        
                    sender = msg_obj.get("From", "Unknown Sender")
                    
                    # Extract the plain text body
                    body = ""
                    if msg_obj.is_multipart():
                        for part in msg_obj.walk():
                            if part.get_content_type() == "text/plain":
                                payload = part.get_payload(decode=True)
                                if payload:
                                    body = payload.decode(errors="ignore")
                                break
                    else:
                        payload = msg_obj.get_payload(decode=True)
                        if payload:
                            body = payload.decode(errors="ignore")
                    
                    # Truncate the body to 500 characters to keep API usage efficient
                    email_data.append(f"From: {sender}\nSubject: {subject}\nBody: {body[:500]}...")

    mail.logout()
    return "\n---\n".join(email_data)