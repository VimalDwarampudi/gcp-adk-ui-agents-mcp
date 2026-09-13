from google.adk.agents import LlmAgent
import PyPDF2

def extract_pdf_text():
    pdf_path = '/app/Leave_Policy.pdf'
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

pdf_content = extract_pdf_text()


leave_policy_agent = LlmAgent(
    name="leave_policy_agent",
    model="gemini-2.5-flash",
    description='agent which provides leave policy information from the PDF document',
    instruction=f"You are a helpful assistant. Use the following document text to answer user questions: {pdf_content}",
)