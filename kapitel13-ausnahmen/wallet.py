#!/usr/bin/env python3
"""
Eigene Ausnahmen
================

Verwenden Sie Ausnahmen, um fehlgeschlagene Annahmen an den aufrufenden Code
zu vermitteln.
"""


class NotEnoughMoney(Exception):
    def __init__(self, price, money_available):
        self.price = price
        self.money_available = money_available

    def __str__(self):
        return (
            f"You can't spend {self.price} because you have only "
            f"{self.money_available} left"
        )


class Wallet:
    def __init__(self, money):
        self._money = money

    def spend(self, amount):
        if amount > self._money:
            raise NotEnoughMoney(amount, self._money)
        return Wallet(self._money - amount)


if __name__ == '__main__':
    try:
        wallet = Wallet(15).spend(20)
    except NotEnoughMoney as money:
        short = money.price - money.money_available
        print(money)
        print(f'You need some extra {short} €')
