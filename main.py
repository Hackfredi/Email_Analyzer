import imaplib
import configparser
from header import HeaderProcessor  # Import the HeaderProcessor class
from url import URLProcessor        # Import the URLProcessor class
from attachment import AttachmentProcessor  # Import the AttachmentProcessor classm attachment import AttachmentProcessor

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

# Create instances of the processors
header_processor = HeaderProcessor(header)           # Header object
url_processor = URLProcessor(body)                   # URL object
attachment_processor = AttachmentProcessor(raw_email) # Attachment object

# Use the encapsulated methods
print("Headers:\n", header_processor.get_header())
print("\nIs Phishing:\n", header_processor.is_phishing())  # Check if the header indicates phishing
print("\nBody:\n", body[:500], "...")  # Print the first 500 chars of body for inspection
print("\nURLs Found:\n", url_processor.get_urls())
print("\nMalicious URLs:\n", url_processor.check_malicious_urls())  # Check for malicious URLs
print("\nAttachments Found:\n", attachment_processor.get_attachments())
print("\nSuspicious Attachments:\n", attachment_processor.has_suspicious_attachments())  # Check for suspicious attachments

# Logout from the server
mail.logout()