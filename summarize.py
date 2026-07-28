import os
from google import genai

def summarize_emails(email_text):
    if not email_text.strip():
        return "No new emails to summarize."
        
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY. Check your .env file.")
        
    # Initialize the official Gen AI client
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
    You are my executive assistant. Please review the following emails from the last 24 hours.
    Provide a concise summary of the key points, highlight any emails that require urgent action,
    and ignore any obvious newsletters or promotional content.
    
    Emails:
    {email_text}
    """
    
    # Generate the response using the high-volume Flash model
    response = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt
    )
    
    return response.text