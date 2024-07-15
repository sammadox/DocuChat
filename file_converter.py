import win32com.client
import os

def doc_to_text(doc_path):
    # Ensure the path is absolute
    doc_path = os.path.abspath(doc_path)

    try:
        # Initialize the Word application
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False

        # Open the DOC file
        doc = word.Documents.Open(doc_path)

        # Extract text from the DOC file
        text = doc.Range().Text

        # Close the DOC file
        doc.Close()

        # Quit the Word application
        word.Quit()

        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        if 'word' in locals():
            word.Quit()
        return None

def pdf_to_txt(input_file, output_file):
    import PyPDF2

    pdf_file = open(input_file, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    with open(output_file, "w") as file:
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            file.write(page.extract_text())
    pdf_file.close()
