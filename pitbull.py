import requests

def send_pitbull_hs(name, score):
    data = {
        "action": "put",
        "name": name,
        "score": score,
        "game_id": "_".join([requests.get("http://www.pitbullparty.com/hs?action=new-game-id").json()["game_id"], str(score)])
    }
    return requests.post("http://www.pitbullparty.com/hs", data=data)

response = send_pitbull_hs('drater', 100)
print(response.text)