import streamlit as st
import convertapi
from pathlib import Path
from txtchunking import chunk_text, flatten_chunked_sentences
#To process chatobject variables
from messages_operations import add_message

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

st.title("DOC Q&A Azure Tool")

uploaded_file = st.file_uploader("Choose a DOC file", type="doc")

if uploaded_file is not None:
    st.write("File uploaded successfully.")
    if st.button("Convert to TXT"):
        with st.spinner('Converting...'):
            output_path = convert_file(uploaded_file)
            st.success('Conversion successful!')
            
            with open(output_path, "r", encoding="utf-8", errors="ignore") as file:
                file_content = file.read()
                if file_content:
                    #Gramamr Data
                    grammar = """
            NP: {<DT>?<JJ>*<NN>}  # Chunk determiners, adjectives, and nouns
                {<NNP>+}          # Chunk sequences of proper nouns
        """ 
                    chunked = chunk_text(file_content, grammar)
                    flattened = flatten_chunked_sentences(chunked)
                    conversation=[]
                    for sentence in flattened:
                        conversation=add_message(conversation, "user", sentence)
                st.text_area("Converted TXT file content", flattened, height=400)
