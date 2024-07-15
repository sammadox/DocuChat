import streamlit as st
import win32com.client
import os
import pythoncom  # Import the pythoncom module

def doc_to_text(doc_path):
    pythoncom.CoInitialize()  # Initialize the COM library

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

# Streamlit interface
st.title('DOC to Text Converter')
doc_file = st.file_uploader("Choose a DOC file", type=['doc', 'docx'])
if doc_file is not None:
    # Save the uploaded file to a temporary path
    with open(doc_file.name, "wb") as f:
        f.write(doc_file.getbuffer())
    
    # Convert the DOC to text
    text = doc_to_text(doc_file.name)
    
    if text:
        # Display the extracted text in a textbox
        st.text_area("Extracted Text", text, height=300)
    else:
        st.error("Failed to extract text. Please check the document format and try again.")
