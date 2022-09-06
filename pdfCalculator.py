#!/usr/bin/env python3

import numpy as np
from fpdf import FPDF
import sys

def addline(text):
    pdf.cell(200,10, text , ln=1, align='C')
    print(text)

def addBlank():
    pdf.ln()
    print()

def add(a,b):
    math = int(a)+int(b)
    addline("a = " + str(a))
    addline("b = " + str(a))
    addline("a+b = "+ str(math))
    addBlank()

def multAndAdd(a,b):
    math = 2*int(a)+int(b)
    addline("a = " + str(a))
    addline("b = " + str(a))
    addline("2*a+b = "+ str(math))
    addBlank()

if __name__ == "__main__":
    #create pdf file with 8.5x11 size
    global pdf
    pdf = FPDF('P','mm', (215.9,279.4))
    pdf.add_page()
    pdf.set_font("Times", size=12)
    #pdf.image("logo.png",0,0,40,40)ß
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    add(a,b)
    multAndAdd(a,b)

    pdf.output("../public_html/output.pdf",'F')
