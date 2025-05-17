# RPS.py

def player(prev_play, opponent_history=[]):
    # Remember opponent's last move
    if prev_play:
        opponent_history.append(prev_play)

    # Simple strategy: if opponent played R most, play P
    if len(opponent_history) < 3:
        return "R"

    last_three = opponent_history[-3:]
    most_common = max(set(last_three), key=last_three.count)

    guess = {"R": "P", "P": "S", "S": "R"}
    return guess[most_common]
