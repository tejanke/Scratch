# http://deckofcardsapi.com/
# https://pypi.org/project/emoji/

import requests
import emoji

def new_deck():
    try:
        r = requests.get("https://deckofcardsapi.com/api/deck/new/")
        if r.status_code == 200:
            return r.json()
        else:
            return "Error {}".format(r.status_code)
    except Exception as e:
        return e

def shuffle(id):
    try:
        url = "https://deckofcardsapi.com/api/deck/" + id + "/shuffle/"
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            return "Error {}".format(r.status_code)
    except Exception as e:
        return e

def draw(id, count):
    try:
        url = "https://deckofcardsapi.com/api/deck/" + id + "/draw/?count=" + str(count)
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            return "Error {}".format(r.status_code)
    except Exception as e:
        return e

def reshuffle(id):
    try:
        url = "https://deckofcardsapi.com/api/deck/" + id + "/shuffle/"
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            return "Error {}".format(r.status_code)
    except Exception as e:
        return e

deck = new_deck()
print(deck)
shuf = shuffle(deck['deck_id'])
print(shuf)
d = draw(deck['deck_id'], 2)
print(d)
print("*" * 50)
re = reshuffle(deck['deck_id'])
print(re)