import requests
from bs4 import BeautifulSoup
import json
from twilio.rest import Client

def get_latest_chapter(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    latest_chapter = soup.find('div', class_='elementor-post__text').text.strip()
    return latest_chapter

def load_last_seen():
    try:
        with open('last_seen.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_last_seen(data):
    with open('last_seen.json', 'w') as f:
        json.dump(data, f)

def send_sms_notification(chapter, phone_number):
    # Twilio credentials
    account_sid = 'your_twilio_sid'
    auth_token = 'your_auth_token'
    twilio_number = 'twilio_number'
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=f"A new chapter {chapter} is available!",
        from_=twilio_number,
        to=phone_number
    )
    print(f"Message sent: {message.sid}")

def main():
    url = 'https://w54.overgeared.club/' #you can use any other website, just make sure to update class in latest_chapter accordingly 
    phone_number = 'your_number'
    
    last_seen = load_last_seen()
    latest_chapter = get_latest_chapter(url)
    
    if latest_chapter != last_seen.get(url):
        send_sms_notification(latest_chapter, phone_number)
        last_seen[url] = latest_chapter
        save_last_seen(last_seen)

if __name__ == '__main__':
    main()