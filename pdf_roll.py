import PyPDF2

def pdf_roll(file_name, angle):
    file = PyPDF2.PdfFileReader(open(file_name, 'rb'))
    file_output = PyPDF2.PdfFileWriter()
    for page_num in range(file.numPages):
        page = file.getPage(page_num)
        page.rotateClockwise(angle)
        file_output.addPage(page)
    with open('result.pdf', 'wb') as f:
        file_output.write(f)

file_name = input()
angle = int(input())

pdf_roll(file_name, angle)
