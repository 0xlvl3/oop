class Bill:
    """
    Object that contains data about a bill,
    such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


# Test of Bill class
the_bill = Bill(amount=50, period="test")
print(f"amount: {the_bill.amount} period: {the_bill.period}")


class Flatmate:
    """
    Object a flatmate who lives in the flat,
    who pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        return the_bill.amount / 2


# Testing Flatmate object
flatmate = Flatmate(name="Test", days_in_house=20)
print(f"name: {flatmate.name}, days_in_house: {flatmate.days_in_house}")
flatmate.pays("test")  # Test of method.


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmate
    such as their names, their due amount and
    the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        print("Generate")


print(flatmate.pays(bill=the_bill))
