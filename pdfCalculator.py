#!/usr/bin/env python3

import numpy as np
from fpdf import FPDF

class pdfCalculator(object):

    def add(self,a,b):
        #create pdf file with 8.5x11 size
        pdf = FPDF('P','mm', (215.9,279.4))
        pdf.add_page()
        pdf.set_font("Arial", size=16)
        #add images and text 
        pdf.image("logo.jpeg")
        pdf.cell(200,10, "a = " + str(a), ln=1, align='C')
        pdf.cell(200,10, "b = " + str(b), ln=1, align='C')
        math = int(a)+int(b)
        pdf.cell(200,10, "a+b = "+ str(math), ln=1, align='C')

        #output to the file name 
        return pdf.output("templates/output.pdf", 'F')
