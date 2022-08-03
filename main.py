from fpdf import FPDF
import os

current_directory = os.getcwd()
print (current_directory)
contents = os.listdir(current_directory)
class PDF(FPDF):
    def header(self) :
        #logo
        self.image("Formode .png", 10,8,25)
        #font 
        self.set_font("helvetica", "B", 20 )

        #padding
        self.cell(40)

        #title
        self.cell(0,10,"client's brief", border = True, ln = 1, align="C")

        # line break
        self.ln(20)
    # page footer
    def footer(self):
        #set position of footer
        self.set_y(-15)
        #set font
        self.set_font("helvetica", "I", 10 )
        #page number
        self.cell(0,10,f"Page {self.page_no}", align="C")

pdf = PDF("p", "mm", "A4")


# collect client's project name
name_of_project = input("Insert the name of the project:")
# collect client's brief
brief = input("Insert the brief: ")

#add page
pdf.add_page()

#page breaker
pdf.set_auto_page_break (auto = True, margin = 15)



#TITLE
# font
pdf.set_font("Helvetica", "B", 16)
# add text
pdf.cell(0, 10, name_of_project, ln=True)

# line break
pdf.ln(5)

# BRIEF
# font
pdf.set_font("Helvetica", "", 12)
# add text
pdf.multi_cell(0, 10, brief, ln=True)

# line break
pdf.ln(5)



#print pdf
pdf.output("sample.pdf")



