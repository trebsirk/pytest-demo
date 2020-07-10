"""
pytest test
"""

def add(hank: int, judy: int) -> int:
    """
    this performs basic addition
    :param hank: int
    :param judy: int
    :return: + of judy and judy
    """
    return hank + judy

def mult(alice: int, bob: int) -> int:
    """
    this performs basic mult
    :param alice: int
    :param bob: int
    :return: * of alice and bob
    """
    return alice * bob

def coin_change(amount, coins):
    """
        this retuns the least number of coins to make change from amount
        :param amount: int
        :param coins: list[int]
        :return: n, number of coins
        """
    n_coins = 0
    while amount > 0 and coins != []:
        if amount - coins[0] >= 0:
            amount -= coins[0]
            n_coins += 1
        else:
            coins = coins[1:]
    if amount > 0:
        return -1
    return n_coins

def coin_change_2(amount, coins):
    """
    this retuns the least number of coins to make change from amount
    :param amount: int
    :param coins: list[int]
    :return: n, number of coins
    """
    n_coins, i = 0, 0
    while amount > 0 and i < len(coins):
        if amount - coins[i] >= 0:
            amount -= coins[i]
            n_coins += 1
        else:
            i += 1
    if amount > 0:
        return -1
    return n_coins

def coin_change_3(amount, coins):
    """
    this retuns the least number of coins to make change from amount
    :param amount: int
    :param coins: list[int]
    :return: n, number of coins
    """
    n_coins, i = 0, 0
    while amount > 0 and i < len(coins):
        n_from_coin = amount // coins[i]
        if n_from_coin > 0:
            amount -= (coins[i]*n_from_coin)
            n_coins += n_from_coin
        i += 1
    if amount > 0:
        return -1
    return n_coins
