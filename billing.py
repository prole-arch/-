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
        return f"Money {self.amount},{self.currency}"



m1=Money(101,"usd")
print(str(m1))