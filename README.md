📚 Manhwa Updater
Manhwa Updater is a Python-based automation tool that monitors your favorite manhwa series and sends you instant text message notifications when new chapters are released. Perfect for staying up-to-date without checking sites manually.

🚀 Features
✅ Scrapes chapter updates from manhwa websites (like Manhuascan/Kaliscan).

✅ Sends SMS notifications using Twilio (or any other messaging service).

✅ Configurable list of manhwa series to track.

✅ Easy to set up and run periodically (cron, task scheduler).

🔧 Tech Stack
Python 3.x

Selenium (web scraping)

Twilio API (for SMS)

BeautifulSoup4 (optional, if parsing HTML)

⚙️ Installation
1️⃣ Clone the repository:

git clone https://github.com/AnkitAnandNIT/Manhw_Updater.git
cd Manhw_Updater

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Set up Twilio (or your SMS provider):

Sign up for Twilio and get your ACCOUNT_SID, AUTH_TOKEN, and a Twilio phone number.

Add your config in a .env file or directly in the script (if needed).

Example .env:

ini:

TWILIO_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE=+1234567890
TARGET_PHONE=+0987654321

🛠️ Usage
bash:
python manhwa_updater.py


The script will:

Scrape the configured manhwa sites.

-Check for new chapter releases.

-Send you an SMS if a new chapter is found.

📅 Automation Tip
-Set it up as a cron job (Linux/macOS) or a Scheduled Task (Windows) to check for updates regularly:

bash:

0 */6 * * * /usr/bin/python /path/to/Manhw_Updater/manhwa_updater.py


📝 Configuration
The list of manhwa series & URLs can be customized in the script (or ideally, in a separate config file—consider adding one if not already).

You can change the scraping frequency as per your need.


🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

🙌 Acknowledgments
Twilio


