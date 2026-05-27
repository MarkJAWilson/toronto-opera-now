import os
import json
import smtplib
from email.mime.text import MIMEText

recipient = "mark@mwilson.on.ca"
config_file = "email_config.json"

if not os.path.exists(config_file):
    print("Error: email_config.json not found in the root directory.")
    exit(1)

try:
    with open(config_file, "r", encoding="utf-8") as f:
        config = json.load(f)
        
    smtp_server = config.get("smtp_server", "smtp.gmail.com")
    port = config.get("port", 587)
    username = config.get("username")
    password = config.get("password")
    sender = config.get("sender", username)
    
    if not username or not password:
        print("Error: SMTP username and password must be set in email_config.json.")
        exit(1)
        
    body = "This is a test email from the Toronto Opera Now background daily updater to verify that your Gmail SMTP credentials are correct."
    subject = "Toronto Opera Now - Test Email"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    
    print(f"Connecting to {smtp_server}:{port}...")
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    print("Logging in...")
    server.login(username, password)
    print(f"Sending test email to {recipient}...")
    server.sendmail(sender, [recipient], msg.as_string())
    server.quit()
    print("Success! Test email sent successfully.")
except Exception as e:
    print(f"Failed to send test email: {e}")
