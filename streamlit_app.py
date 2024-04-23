import streamlit as st
from PIL import Image
from vertexai.preview import GenerativeModel

# Function to perform OCR using Gemini
def perform_ocr(image):
    # Load the Gemini model
    model = GenerativeModel("gemini-latest")
    # Perform OCR on the image
    ocr_response = model.generate_content(image)
    return ocr_response.text

# Streamlit app
def main():
    st.set_page_config(page_title="Medicine Information OCR App", page_icon=":pill:", layout="wide")
    st.title("Medicine Information OCR App")
    st.markdown("---")
    st.write("Upload an image containing medicine information:")

    # Image uploader
    uploaded_file = st.file_uploader("", type=["jpg", "png"], accept_multiple_files=False, key="file_uploader")

    if uploaded_file is not None:
        # Display the uploaded image
        st.markdown("---")
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Perform OCR on the image
        ocr_text = perform_ocr(image)

        # Display the extracted information in a table
        st.markdown("---")
        st.subheader("Extracted Medicine Information:")
        rows = ocr_text.split("\n")
        if len(rows) > 1:
            st.table([rows])
        else:
            st.write("No medicine information found in the image.")

if __name__ == '__main__':
    main()
