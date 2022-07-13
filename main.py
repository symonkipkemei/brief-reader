from fpdf import FPDF

class PDF(FPDF):
    def header(self) :
        #logo
        self.image("Formode.png", 10,8,25)
        #font 
        self.set_font("helvetica", "B", 20 )

        #title
        self.cell(0,10,"client's brief", border = True, ln = 1, align="C")
        

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


# BRIEF
# font
pdf.set_font("Helvetica", "", 16)
# add text
pdf.cell(0, 10, brief, ln=True)




#print pdf
pdf.output("sample.pdf")



