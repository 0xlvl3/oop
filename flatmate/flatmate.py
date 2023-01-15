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
