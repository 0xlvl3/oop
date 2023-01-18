from bill import Bill
from flatmate import Flatmate
from pdf_report import PdfReport
from file_stack import file_link


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

input_bill = Bill(amount=bill_amount, period=user_period)
print(input_bill.amount, input_bill.period)

print(user_class.pays(bill=input_bill, flatmate2=friend_class))

print("We have also created a PDF report for you")
pdf_report = PdfReport(filename="report.pdf")
pdf_report.generate(flatmate1=user_class, flatmate2=friend_class, bill=input_bill)
file_link("report.pdf")
