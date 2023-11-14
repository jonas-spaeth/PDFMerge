import base64

import streamlit as st
import PyPDF2

st.header("Merge 2 PDFs")


def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

def concatenate_pdfs(input_files, output_file):
    pdf_writer = PyPDF2.PdfWriter()

    for input_file in input_files:
        pdf_reader = PyPDF2.PdfReader(input_file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    #with open(output_file, 'wb') as output_pdf:
    #    pdf_writer.write(output_pdf)
    return pdf_writer


uploaded_file = st.file_uploader('Choose the first .pdf file', type="pdf")
if uploaded_file is not None:
    pass
    # df = extract_data(uploaded_file)


uploaded_file2 = st.file_uploader('Choose the second .pdf file', type="pdf")
if uploaded_file is not None:
    pass
    # df2 = extract_data(uploaded_file2)


export_as_pdf = st.button("Export Report")
if export_as_pdf:
    pdf = concatenate_pdfs([uploaded_file, uploaded_file2], "outputfile")
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

    st.markdown(html, unsafe_allow_html=True)

# Example usage: