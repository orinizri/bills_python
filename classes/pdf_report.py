from fpdf import FPDF


class PdfReport:
    """
    Create a pdf that contains data about the flat mates
    - name
    - amount
    - period of the bill
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pays = str(round(flatmate1.pays(bill, flatmate2.days_in_house), 2))
        flatmate2_pays = str(round(flatmate1.pays(bill, flatmate1.days_in_house), 2))
        
        pdf = FPDF(orientation="portrait", unit="pt", format="A4")
        pdf.add_page()
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=0, h=40, txt=bill.period, border=1, ln=1)
        pdf.cell(w=150, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=0, h=40, txt=flatmate1_pays, border=1, ln=1)
        pdf.cell(w=150, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=0, h=40, txt=flatmate2_pays, border=1, ln=1)
        pdf.output(f'{self.file_name}.pdf')
