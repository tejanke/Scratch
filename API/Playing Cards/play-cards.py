# http://deckofcardsapi.com/
# https://pypi.org/project/emoji/

from emoji.core import emojize
import requests
import emoji

card_emoji_values = {
    "1" : ":one:",
    "2" : ":two:",
    "3" : ":three:",
    "4" : ":four:",
    "5" : ":five:",
    "6" : ":six:",
    "7" : ":seven:",
    "8" : ":eight:",
    "9" : ":nine:",
    "10" : ":keycap_ten:",
    "JACK" : ":jack_o_lantern:",
    "KING" : ":santa:",
    "QUEEN" : ":bride_with_veil:",
    "ACE" : ":a:"
}

card_emoji_suits = {
    "DIAMONDS" : ":diamonds:",
    "CLUBS" : ":clubs:",
    "HEARTS" : ":hearts:",
    "SPADES" : ":spades:"
}

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
print(emoji.emojize(':thumbs_up:'))
d = draw(deck['deck_id'], 1)
print(d)
for k,v in d.items():
    print(k, v)
for card in d['cards']:
    val = card_emoji_values[card['value']]
    sui = card_emoji_suits[card['suit']]
    print(val, type(val))
    print(sui, type(sui))
    print(card['value'], card_emoji_values[card['value']])
    print(card['suit'], card_emoji_suits[card['suit']])
    print(emoji.emojize(val, use_aliases=True))
    print(emoji.emojize(sui, use_aliases=True))
