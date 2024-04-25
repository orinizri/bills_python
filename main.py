from classes.bill import Bill
from classes.flatmate import FlatMate
from classes.pdf_report import PdfReport


# Asking for bill amount and period
bill_amount = float(input("Please enter the bill amount: "))
period = input("Please enter the period of the bill: ")

# Creating the bill with amount and period
bill = Bill(amount=bill_amount, period=period)

# Asking for flatmates' names and days in house
flatmate1_name = input("Please enter the name of the first flatmate: ")
flatmate1_days = int(input(f"Number of days {flatmate1_name} stayed in the house: "))
flatmate2_name = input("Please enter the name of the second flatmate: ")
flatmate2_days = int(input(f"Number of days {flatmate2_name} stayed in the house: "))

# Creating the flatmate instances
flatmate1 = FlatMate(name=flatmate1_name, days_in_house=flatmate1_days)
flatmate2 = FlatMate(name=flatmate2_name, days_in_house=flatmate2_days)

# calculation of each flatmate payment relatively to their stay in the house
flatmate1_bill_amount = flatmate1.pays(bill=bill, days_in_house2=flatmate2.days_in_house)
flatmate2_bill_amount = flatmate2.pays(bill=bill, days_in_house2=flatmate1.days_in_house)

# Generating the PDF report with the period, flatmate names and relative payment
pdf_report = PdfReport(file_name=bill.period)
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=bill)
