from fpdf import FPDF


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


class Flatmate:
    """
    Object a flatmate who lives in the flat,
    who pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        user_weight = self.days_in_house / (
            self.days_in_house + flatmate2.days_in_house
        )
        friend_weight = flatmate2.days_in_house / (
            flatmate2.days_in_house + self.days_in_house
        )
        user_pay = round(bill.amount * user_weight, 2)
        friend_pay = round(bill.amount * friend_weight, 2)
        return f"""
{self.name} will pay {user_pay} for the {bill.period} period 
while {flatmate2.name} will pay {friend_pay} for the {bill.period} period
    """


# Testing Flatmate object

# flatmate = Flatmate(name="Mary", days_in_house=20)
# print(f"name: {flatmate.name}, days_in_house: {flatmate.days_in_house}")


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmate
    such as their names, their due amount and
    the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        # Variables used.
        flatmate1_pay = flatmate1.pays(bill=the_bill, flatmate2=flatmate2)
        flatmate2_pay = flatmate2.pays(bill=the_bill, flatmate2=flatmate1)

        # Initialising PDF.
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add image.
        pdf.image("house.png", w=30, h=30)

        # Insert title.
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period: ", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Font for flatmates
        pdf.set_font(family="Times", size=12)

        # Insert and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(
            w=150,
            h=40,
            txt=flatmate1_pay,
            border=0,
            ln=1,
        )

        # Insert and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(
            w=150,
            h=40,
            txt=flatmate2_pay,
            border=0,
            ln=1,
        )

        pdf.output(self.filename)


# john = Flatmate(name="John", days_in_house=20)
# mary = Flatmate(name="Mary", days_in_house=25)
# print(john.pays(bill=the_bill, flatmate2=mary))
# print(mary.pays(bill=the_bill, flatmate2=john))


# pdf_report = PdfReport(filename="Report1.pdf")
# pdf_report.generate(flatmate1=john, flatmate2=mary, bill=the_bill)

print(
    """
Welcome to the flatmate split app; This app is a CLI based application,
follow the input directions to get a assessment for how much you owe.
      """
)

# User and flatmate details.
user = input("Hello what is your name: ")
print(f"Welcome {user}")
friend = input("What is your friends name: ")
print(f"Friend name is {friend}")

# Days in house for the users.
user_days = int(input(f"{user} how many days did you stay in the house: "))
friend_days = int(input(f"How many days was {friend} in the house: "))

user_class = Flatmate(name=user, days_in_house=user_days)
friend_class = Flatmate(name=friend, days_in_house=friend_days)

bill_amount = int(input("Hey user enter the bill amount: "))
print(f"Bill amount is {bill_amount}")
user_period = input("What period was this in: ")

the_bill = Bill(amount=bill_amount, period=user_period)
print(the_bill.amount, the_bill.period)

print(user_class.pays(bill=the_bill, flatmate2=friend_class))
