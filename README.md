# AI Daily Email Summarizer

An automated Python script that connects to a Gmail inbox, retrieves unread emails from the last 24 hours, and generates a concise, actionable summary using the Google Gemini AI API. It then automatically emails the final summary back to you.

## Features
* **Automated Email Fetching:** Uses IMAP to securely parse recent, unread emails.
* **AI-Powered Summarization:** Leverages the Gemini API to filter out newsletters and highlight urgent messages.
* **Daily Automation (Serverless):** Fully automated via GitHub Actions to run on a daily schedule, requiring no always-on local server.
* **Automated Delivery:** Uses `smtplib` to send the generated summary directly to your inbox.
* **Secure Credential Management:** Implements `python-dotenv` for local testing and GitHub Secrets for cloud deployment to keep API keys safely hidden.

## Tech Stack
* **Language:** Python 3
* **Libraries:** `imaplib`, `email`, `smtplib`
* **AI Engine:** Google Generative AI SDK (`google-genai`)
* **Infrastructure:** GitHub Actions (cron scheduling)

---

## Local Setup & Testing

**1. Clone the repository**
> git clone https://github.com/itxruru/EmailSummarizer.git
> cd EmailSummarizer

**2. Install dependencies**
> pip install -r requirements.txt

**3. Configure local credentials**
Create a `.env` file in the root directory (this file is ignored by Git). Add your details:
> GMAIL_ADDRESS=your.email@gmail.com
> GMAIL_APP_PASSWORD=your_16_character_app_password
> GEMINI_API_KEY=your_gemini_api_key

**4. Test the script locally**
> python main.py

---

## Cloud Deployment (GitHub Actions)

To make this script run automatically every day in the background for free:

**1. Push your code to GitHub**
Ensure your repository includes the `.github/workflows/daily_summary.yml` file.

**2. Add Repository Secrets**
On your GitHub repository page, go to **Settings** > **Secrets and variables** > **Actions**.
Click **New repository secret** and add your credentials exactly like this (do not use quotes or spaces):

* **Name:** `GMAIL_ADDRESS` 
  **Secret:** your_actual_email@gmail.com

* **Name:** `GMAIL_APP_PASSWORD`
  **Secret:** your_16_character_password

* **Name:** `GEMINI_API_KEY`
  **Secret:** your_gemini_api_key

**3. The Schedule**
The workflow is set to automatically run every day at 8:00 AM (UTC+3 / Saudi Arabia Time) and email you the summary. 

*(Note: To change the time the email sends, edit the `cron` schedule inside the `.github/workflows/daily_summary.yml` file. GitHub Actions uses UTC time, so subtract 3 hours from your local time).*
