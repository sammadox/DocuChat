import streamlit as st
import convertapi
from pathlib import Path

# Set your ConvertAPI secret
convertapi.api_secret = 'UVJ2EbZ5ei63xEdu'

def convert_file(uploaded_file):
    # Save the uploaded file to a temporary location
    temp_file_path = Path("/tmp") / uploaded_file.name
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Convert the file
    result = convertapi.convert('txt', {
        'File': str(temp_file_path)
    }, from_format='doc')

    # Save the converted file to the same directory
    save_path = Path("/tmp") / (temp_file_path.stem + '.txt')
    result.save_files(str(save_path))

    return save_path

st.title("DOC to TXT Converter")

uploaded_file = st.file_uploader("Choose a DOC file", type="doc")

if uploaded_file is not None:
    st.write("File uploaded successfully.")
    if st.button("Convert to TXT"):
        with st.spinner('Converting...'):
            output_path = convert_file(uploaded_file)
            st.success('Conversion successful!')
            with open(output_path, "r") as file:
                st.download_button(
                    label="Download TXT file",
                    data=file.read(),
                    file_name=output_path.name,
                    mime="text/plain"
                )
