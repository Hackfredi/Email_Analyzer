import imaplib
import configparser
import re

# Create ConfigParser object
config = configparser.ConfigParser()

# Read the config file
config.read('config.ini')

# Get email credentials from config
email_user = config['email']['email_user']
email_pass = config['email']['email_pass']

# Connect to Gmail's IMAP server
mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)

# Log in using your email and app password
mail.login(email_user, email_pass)

# Select the inbox
mail.select('inbox')

# Search for all emails
status, response = mail.search(None, 'ALL')
email_ids = response[0].split()

# Fetch the most recent email in raw format
status, email_data = mail.fetch(email_ids[-1], '(RFC822)')

# Store raw email data
raw_email = email_data[0][1].decode('utf-8')

# 1) Extract Header (everything before the first empty line)
header, body = raw_email.split("\r\n\r\n", 1)


# 3) Extract URLs from body using regex
urls = re.findall(r'(https?://[^\s]+)', body)

# 4) Extract Attachments (look for 'Content-Disposition: attachment')
attachments = []
if 'Content-Disposition: attachment' in raw_email:
    attachment_lines = [line for line in raw_email.split('\n') if 'Content-Disposition: attachment' in line]
    attachments.extend(attachment_lines)

# Print the extracted data (optional)
print("Headers:\n", header)
print("\nBody:\n", body[:500], "...")  # Print the first 500 chars of body for inspection
print("\nURLs Found:\n", urls)
print("\nAttachments Found:\n", attachments)

# Logout from the server
mail.logout()
