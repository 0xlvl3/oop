class Bill:
    """
    Object that contains data about a bill,
    such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


# Test of Bill class

# the_bill = Bill(amount=120, period="March 2022")
# print(f"amount: {the_bill.amount} period: {the_bill.period}")
