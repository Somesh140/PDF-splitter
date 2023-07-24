from PyPDF2 import PdfWriter, PdfReader

filepath= "19 - Statistics part1 .pdf"

reader = PdfReader(filepath)
writer = PdfWriter()

# add page no x from reader to output document, unchanged:
for page_no in range(1,31):
    writer.add_page(reader.pages[page_no])


# add page 2 from reader, but rotated clockwise 90 degrees:
#writer.add_page(reader.pages[1].rotate(90))

# add page 3 from reader, but crop it to half size:
#page3 = reader.pages[2]
#page3.mediabox.upper_right = (
#    page3.mediabox.right / 2,
#    page3.mediabox.top / 2,
#)
#writer.add_page(page3)

# add some Javascript to launch the print window on opening this PDF.
# the password dialog may prevent the print dialog from being shown,
# comment the the encription lines, if that's the case, to try this out:
#writer.add_js("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

# write to document-output.pdf
with open("stats-basic.pdf", "wb") as fp:
    writer.write(fp)