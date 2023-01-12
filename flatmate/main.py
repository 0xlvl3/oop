class Bill:
    """
    Object that contains data about a bill,
    such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


# Test of Bill class
bill = Bill("test", "test")
print(f"amount: {bill.amount} period: {bill.period}")


class Flatmate:
    """
    Object a flatmate who lives in the flat,
    who pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        print("bill")


# Testing Flatmate object
flatmate = Flatmate("Test", 20)
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
