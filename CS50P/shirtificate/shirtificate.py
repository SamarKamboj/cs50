from fpdf import FPDF


def main():
    name = input("Name: ")
    add(name)


def add(s):
    pdf = FPDF()
    pdf.add_page()
    pdf.image("shirtificate.png", y=(pdf.w-142.50), w=190, h=190)
    pdf.set_font("helvetica", 'B', 50)
    pdf.text(x=40, y=50, txt="CS50 Shirtificate")
    pdf.set_font("helvetica", 'B', 30)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=65, y=(pdf.h-25)/2, txt=f"{s} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()