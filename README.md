# Kanye Zone High Score Script

## Overview

This repository contains a Python script to automate the process of sending a high score to the "Kanye Zone" game website. The primary objective is to find integer pairs `(k, t)` that satisfy the equation: 

\[ 50000k + 233t + 50000 = s \]

where:
- `k` represents the number of Kanyes.
- `t` represents normalized game time.
- `s` is the desired score.

The script then encodes this information and sends it to the game server as a high score entry.

## Functions

1. `findSolution(score, num_solutions=1)`: 
   - Finds pairs `(k, t)` for a given score `s` that satisfy the equation.
   - `num_solutions` parameter determines the number of solutions to return.

2. `send_kanye_zone_hs(name, score)`:
   - Encodes the score and related game details.
   - Sends the encoded high score details to the game server.

## Encoding

The script uses predefined "magic numbers" and the XOR operation to encode game details:

   - Score, number of Kanyes, and game time are encoded using `magic_num1` and sent in the request.
   - The `game_id` combines a game ID from the server with the encoded values encoded once more with `magic_num2`.

## Usage

To send a high score to the "Kanye Zone" game:

```python
response = send_kanye_zone_hs("player_name", desired_score)
```

Replace `"player_name"` with the desired player name and `desired_score` with the score you want to send. The server response will be printed.

## Important Notes

- Maximum allowed score value: `9223372036854775807` (64-bit signed integer max)
- Minimum allowed score value: `-9223372036854775808` (64-bit signed integer min)
- The score value can't be `0`.

## Dependencies

- The script requires the `requests` library. You can install it using:

```
pip install requests
```

## Disclaimer

This script and its functionality are provided for educational purposes only. Misusing the script to exploit or cheat on the game website is discouraged. Always respect the terms of service of any platform you interact with.
