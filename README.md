# AI Daily Email Summarizer

An automated Python script that connects to a Gmail inbox, retrieves unread emails from the last 24 hours, and generates a concise, actionable summary using the Google Gemini AI API. 

## Features
* **Automated Email Fetching:** Uses IMAP to securely parse recent, unread emails.
* **AI-Powered Summarization:** Leverages the Gemini API to filter out newsletters and highlight urgent messages.
* **Secure Credential Management:** Implements `python-dotenv` to keep passwords and API keys safely hidden from version control.

## Tech Stack
* Python 3
* `imaplib` & `email` (Standard Libraries)
* Google Generative AI SDK (`google-genai`)

## Setup Instructions

**1. Clone the repository**
git clone https://github.com/itxruru/EmailSummarizer.git
cd EmailSummarizer

**2. Install dependencies**
pip install -r requirements.txt

**3. Configure credentials**
* Create a `.env` file in the root directory.
* Add your details based on the `.env.example` file:
  * `GMAIL_ADDRESS`: Your email address.
  * `GMAIL_APP_PASSWORD`: Your 16-character Google App Password.
  * `GEMINI_API_KEY`: Your Google AI Studio key.

**4. Run the summarizer**
python main.py
