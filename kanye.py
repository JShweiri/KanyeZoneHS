import requests

def findSolution(score, num_solutions=1):
    # Find (k, t) pairs that satisfy the equation 50000k + 233t + 50000 = s
    initial_score = 50000
    score_per_kanye = 50000
    score_per_tick = 233

    solutions = []
    ticks = 1  # game_time must be at least 1

    while len(solutions) < num_solutions:
        score_due_to_kanyes = (score - score_per_tick * ticks - initial_score)
        remainder = score_due_to_kanyes % score_per_kanye
        if remainder == 0:
            kanyes = score_due_to_kanyes // score_per_kanye
            solutions.append((kanyes, ticks))
        ticks += 1

    # print(solutions)
    return solutions

def send_kanye_zone_hs(name, score):

    kanyes , time = findSolution(score)[0]
    # print(score, kanyes, time)
    # print(kanyes*50000 + 50000 + time*233)

    magic_num1 = 666444222
    magic_num2 = 111333222

    encoded_score = score ^ magic_num1
    encoded_kanyes = kanyes ^ magic_num1
    encoded_time = time ^ magic_num1

    data = {
        "action": "put",
        "name": name,
        "score": encoded_score,
        "kanyes": encoded_kanyes,
        "game_time": encoded_time,
        "game_id": "_".join([requests.get("http://www.kanyezone.com/hs?action=new-game-id").json()["game_id"], str(encoded_score ^ magic_num2), str(encoded_kanyes ^ magic_num2), str(encoded_time ^ magic_num2), ])
    }
    # print(data)
    
    response = requests.post("http://www.kanyezone.com/hs", data=data)
    return response


# Score max value: 9223372036854775807 (64-bit signed integer max)
# Score min value: -9223372036854775808 (64-bit signed integer min)
# Score can't be 0
response = send_kanye_zone_hs("jason", 4891337)
print(response.text)