#SENDING EMAIL USING PYTHON
import streamlit as st
import smtplib
from email.message import EmailMessage

# Title of the app
st.title("📬 Email Express — Simple Mail & File Sender in Python")

# Input fields (labels only — do not put actual values here!)
sender_email = st.text_input("Your Gmail Address")
app_password = st.text_input("Your Gmail App Password", type="password")
receiver_email = st.text_input("Receiver's Email")
subject = st.text_input("Email Subject")
message = st.text_area("Your Message")
# File uploader (multiple files allowed)
uploaded_files = st.file_uploader("Attach files (images, PDFs, etc.)", type=None, accept_multiple_files=True)

# Send Button
if st.button("Send Email"):
    if sender_email and app_password and receiver_email and message:
        try:
            # Setup the email
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg.set_content(message)
            # Attach all uploaded files
            if uploaded_files:
                for uploaded_file in uploaded_files:
                    file_data = uploaded_file.read()
                    msg.add_attachment(
                        file_data,
                        maintype="application",
                        subtype="octet-stream",
                        filename=uploaded_file.name
                    )

            # Sending the email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(sender_email, app_password)
                smtp.send_message(msg)

            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please fill all fields.")
