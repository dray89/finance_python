# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 11:55:03 2020

@author: rayde
"""


from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def merge_pdfs(paths, output = 'C:\\Users\\rayde\\Documents\\merge_files\\Ray_Debra_ResumeCoverLetter_Bose.pdf'):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = []
    for file in os.listdir("C:\\Users\\rayde\\Documents\\merge_files"):
          if file.endswith(".pdf"):
               paths.append("C:\\Users\\rayde\\Documents\\merge_files\\"+ file)
    merge_pdfs(paths)