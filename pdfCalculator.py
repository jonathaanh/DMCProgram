#!/usr/bin/env python3

import numpy as np
from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size=16)
    
pdf.cell(200,10, "a = 1", ln=1, align='C')

pdf.cell(200,10, "b = 2", ln=2, align='C')

pdf.cell(200,10, "a+b = 3", ln=3, align='C')

pdf.output("output.pdf")
