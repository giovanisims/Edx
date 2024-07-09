from fpdf import FPDF


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# CS50 Shirtificate text
text = "CS50 Shirtificate"
pdf.set_font("helvetica", "B", 50)
pdf.cell(190, 45, "CS50 Shirtificate", align="C")

# CS50 shirt image
image_width = 200
page_width = 210 
x = (page_width - image_width) / 2
pdf.image("shirtificate.png", x=x, y=80, w=image_width, h=190)

# CS50 shirt text
name = input("Name: ")
pdf.set_font("helvetica", "B", 25)
pdf.set_text_color(255,255,255)
pdf.set_xy(10, 120)  
pdf.cell(190, 45,f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")