import webbrowser
import os
from fpdf import FPDF


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
        flatmate1_pay = flatmate1.pays(bill, flatmate2=flatmate2)
        flatmate2_pay = flatmate2.pays(bill, flatmate2=flatmate1)

        # Initialising PDF.
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add image.
        pdf.image("files/house.png", w=30, h=30)

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

        # Save PDF, then cd to files and open via webbrowser.
        pdf.output(f"files/{self.filename}")
        os.chdir("files")
        webbrowser.open(self.filename)
