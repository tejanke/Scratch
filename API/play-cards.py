import requests

def new_deck():
    try:
        r = requests.get("https://deckofcardsapi.com/api/deck/new/")
        if r.status_code == 200:
            return r.json()
        else:
            return "Error {}".format(r.status_code)
    except:
        return "Error"

def shuffle(id):
    try:
        url = "https://deckofcardsapi.com/api/deck/" + id + "/shuffle/"
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            return "Error {}".format(r.status_code)
    except:
        return "Error"

deck = new_deck()
print(deck)
shuf = shuffle(deck['deck_id'])
print(shuf)