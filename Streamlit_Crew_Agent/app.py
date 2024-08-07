import os
import tempfile
import streamlit as st
from pdf_ops import PDF_Ops
from streamlit_pdf_viewer import pdf_viewer

def main():
    st.title("PDF Operations App")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        pdf_content = uploaded_file.read()
        pdf_ops = PDF_Ops(pdf_content=pdf_content)

        # Page selection
        total_pages = len(pdf_ops.pdf_reader.pages)
        page_number = st.number_input("Enter page number to view", min_value=1, max_value=total_pages, value=1)

        if st.button("View Page"):
            # Display extracted text
            st.subheader(f"Extracted Text from Page {page_number}:")
            st.text(pdf_ops.get_page_text(page_number))

            # Display PDF viewer
            st.subheader(f"PDF Viewer:")
            st.write(f"Showing page {page_number} of {total_pages}")
            
            base64_pdf = pdf_ops.get_base64_pdf()
            pdf_display = f'<iframe src="https://mozilla.github.io/pdf.js/web/viewer.html?file=data:application/pdf;base64,{base64_pdf}#page={page_number}" width="700" height="1000" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
