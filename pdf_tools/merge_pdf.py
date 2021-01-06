# merge_pdf.py
# For combining two PDF files into 1
# Can be executed as a standalone script or as part of pdf_tool.py
#
# Usage (standalone):   python merge_pdf.py <output>.pdf <input1>.pdf <input2>.pdf
# Usage (pdf_tool.py):  python pdf_tool.py -m <output>.pdf <input1>.pdf <input2>.pdf

import sys
import PyPDF2

def merge(files):
    merger = PyPDF2.PdfFileMerger()

    input1 = open(files[1], "rb")
    input2 = open(files[2], "rb")

    merger.append(fileobj = input1)
    merger.append(fileobj = input2)

    # Write to an output PDF document
    output = open(files[0], "wb")
    merger.write(output)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Not enough inputs specified")
        print("Usage: python merge_pdf.py <output>.pdf <input1>.pdf <input2>.pdf")
        exit()

    files = []
    for i in range(3):
        files.append(sys.argv[i+1])
        if files[i][-4:-1] != ".pdf":
            files[i] += ".pdf"

    merge(files)