from flask.views import MethodView
from wtforms import Form
from wtforms import StringField
from wtforms import SubmitField
from flask import Flask
from flask import render_template
from flask import request

# How we create our Flask app
app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html", bill_form=bill_form)


class ResultsPage(MethodView):

    # Notice here we use post instead of get.

    def post(self):

        # Here we get data using Flask request from our BillFormPage widget.

        bill_form = BillForm(request.form)
        amount = bill_form.amount.data
        return amount


class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")

    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in the house: ")

    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in the house: ")

    button = SubmitField("Calculate")


# Pages.

# How we add our urls.
# <insert_class>.as_view.
app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill", view_func=BillFormPage.as_view("bill_form_page"))
app.add_url_rule("/results", view_func=ResultsPage.as_view("results_page"))

app.run()
