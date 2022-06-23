from bs4 import BeautifulSoup
import requests
import lxml

html_texts = requests.get("https://www.emojimeanings.net/list-smileys-people-whatsapp").text
soup = BeautifulSoup(html_texts, "lxml")
cards = soup.find_all("div", class_="card")

for card in cards[1:]:

    try:
        my_data = {}
        my_data["emoji"] = card.find_all("div", class_="card-body")[0].find_all("span", class_="emoji")[0].text
        my_data["name"] = card.find_all("div", class_="card-body")[0].find_all("div", class_="card-title")[0].text[2:]
        my_data["meaning"] = card.find_all("div", class_="card-body")[0].find_all("p", class_="card-text")[0].text

        url = 'http://127.0.0.1:8000/emoji/emoji/'

        x = requests.post(url, json=my_data)

        print(x.text)

    except Exception as e:
        pass
