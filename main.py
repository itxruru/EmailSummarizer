from dotenv import load_dotenv
from fetch_emails import get_unread_emails
from summarize import summarize_emails

def main():
    # Load credentials from the .env file into the environment
    load_dotenv()
    
    print("Fetching unread emails from the last 24 hours...")
    try:
        email_content = get_unread_emails()
    except Exception as e:
        print(f"Error fetching emails: {e}")
        return
    
    if not email_content:
        print("Inbox is clear! No unread emails.")
        return
        
    print("Found emails. Sending to Gemini for summarization...\n")
    try:
        summary = summarize_emails(email_content)
    except Exception as e:
        print(f"Error communicating with Gemini API: {e}")
        return
    
    print("="*50)
    print("DAILY EMAIL SUMMARY")
    print("="*50)
    print(summary)

if __name__ == "__main__":
    main()