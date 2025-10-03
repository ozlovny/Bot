def check_win(bet: str, roll: int) -> bool:
    if bet == "чет":
        return roll % 2 == 0
    elif bet == "нечет":
        return roll % 2 == 1
    elif bet == "больше":
        return roll > 3
    elif bet == "меньше":
        return roll < 4
    elif bet.startswith("число:"):
        try:
            num = int(bet.split(":")[1])
            return roll == num
        except:
            return False
    return False

def get_multiplier(bet: str) -> float:
    return 5.0 if bet.startswith("число:") else 1.85