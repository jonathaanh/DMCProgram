#!/usr/bin/env python3

import numpy as np
from fpdf import FPDF

#create pdf file with 8.5x11 size
pdf = FPDF('P','mm', (215.9,279.4))
pdf.add_page()
pdf.set_font("Arial", size=16)

#add images and text 
pdf.image("logo.jpeg")
pdf.cell(200,10, "a = 1", ln=1, align='C')
pdf.cell(200,10, "b = 2", ln=2, align='C')
pdf.cell(200,10, "a+b = 3", ln=3, align='C')

#output to the file name 
pdf.output("output.pdf")
