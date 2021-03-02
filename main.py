import json
import urllib
import requests
import telebot
from datetime import datetime, date, timedelta


def main():
    # Get the json file
    url = "https://join.gov.tw/toOpenData/ey/idea"
    response = requests.get(url)
    data = response.json()

    # Keep only the petition created yesterday
    target_date = date.today() - timedelta(days=1)
    petitions = []
    for i in range(-1, -1000, -1):
        petition_date = datetime.strptime(
            data[i]["提送日期"][0:10], "%Y-%m-%d").date()

        # If it's not yesterday's petition
        if(petition_date != target_date):
            break

        # Add to petitions (ready to post to telegram)
        petitions.append(data[i])

    # Initialize Telegram bot
    bot = telebot.TeleBot(
        "1641231483:AAG2Az4ZLh6QcbNNmOif5jOuMH4WO31o390", parse_mode=None)

    # Send posts
    for i in petitions:
        title = i["標題"]
        context = i["提議內容"]
        url = i["網址"]
        bot.send_message("@votetw", f"#{title}\n\n {context}\n\n {url}", )


if __name__ == "__main__":
    main()
