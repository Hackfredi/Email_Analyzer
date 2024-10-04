class AttachmentProcessor:
    def __init__(self, raw_email):
        self.__raw_email = raw_email  # Private variable
        self.__attachments = self.__extract_attachments()  # Private method

    def __extract_attachments(self):
        attachments = []
        if 'Content-Disposition: attachment' in self.__raw_email:
            attachment_lines = [line for line in self.__raw_email.split('\n') if 'Content-Disposition: attachment' in line]
            attachments.extend(attachment_lines)
        return attachments

    def get_attachments(self):
        return self.__attachments  # Public method to access private attachments

    def has_suspicious_attachments(self):
        # Add logic to analyze attachments for phishing
        suspicious_types = ['.exe', '.scr', '.zip']
        return [attachment for attachment in self.__attachments if any(attachment.endswith(ext) for ext in suspicious_types)]
