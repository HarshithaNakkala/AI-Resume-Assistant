
import os
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    """

    # Check whether the PDF exists
    if not os.path.exists(pdf_path):
        print("Error: PDF file not found!")
        return ""

    try:
        # Open the PDF
        reader = PdfReader(pdf_path)

        text = ""

        # Extract text from each page
        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception as error:
        print(f"Error while reading PDF: {error}")
        return ""


def save_text_to_file(text, output_path):
    """
    Save extracted text into a text file.
    """

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)

        print(f"Text saved successfully to: {output_path}")

    except Exception as error:
        print(f"Error while saving text file: {error}")


# Input PDF
pdf_path = "data/Resume.pdf"

# Output text file
output_path = "data/resume.txt"


# Extract text from PDF
resume_text = extract_text_from_pdf(pdf_path)


# Check whether text was extracted
if resume_text:

    # Print extracted text
    print("\n========== RESUME TEXT ==========\n")
    print(resume_text)
    print("\n========== END OF RESUME ==========\n")

    # Save extracted text
    save_text_to_file(resume_text, output_path)

    print("\nResume text extraction completed successfully!")

else:
    print("No text was extracted from the PDF.")

