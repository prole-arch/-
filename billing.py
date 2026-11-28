from decimal import *
class Money:
    def __init__(self, amounnt, currency):
        self.amount = Decimal(amounnt)
        self.currency = currency
        self.amount = self.amount.quantize(Decimal("1.00"))
        self.amount = self.amount.quantize(Decimal("1.00"), ROUND_HALF_UP)
        if len(self.currency)!=3:
            print("Erorr")

    def __str__(self):
        return f"{self.amount},{self.currency}"
    def __repr__(self):
        return f"Money {self.amount},{self.currency}"
    def __add__(self, other):
        if other.currency == self.currency:
            return Money(other.amount + self.amount, self.currency)
        if  other.currency != self.currency:
            raise NotImplemented("типы валют не совпадают")
    def __sub__(self, other):
        if other.currency == self.currency:
            return Money(self.amount - other.amount , self.currency)
        if other.currency != self.currency:
            raise NotImplemented("типы валют не совпадают")
m1=Money(101,"RUB")
m2 = Money(15,"usd")

m3 = m1 - m2
print(m3)