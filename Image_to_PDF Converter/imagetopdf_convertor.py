from fpdf import FPDF
import sys

image = sys.argv[1]
pdf = FPDF("P", "mm", "A4")
x = 0
y = 0
w = 210
h = 297
pdf.add_page()
pdf.image(image, x,y,w,h)
pdf.output("My_pic_pdf.pdf", "F")
