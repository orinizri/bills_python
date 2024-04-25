from classes.bill import Bill
from classes.flatmate import FlatMate
from classes.pdf_report import PdfReport

# Creating the bill with amount and period
bill = Bill(amount=120, period="April 2024")

# Creating the flatmate instances 
adam = FlatMate(name="Adam", days_in_house=20)
john = FlatMate(name="John", days_in_house=30)

# calculation of each flatmate payment relatively to their stay in the house
johns_bill_amount = john.pays(bill=bill, days_in_house2=adam.days_in_house)
adam_bill_amount = adam.pays(bill=bill, days_in_house2=john.days_in_house)

# Generating the PDF report with the period, flatmate names and relative payment
pdf_report = PdfReport(file_name=bill.period)
pdf_report.generate(flatmate1=adam, flatmate2=john, bill=bill)