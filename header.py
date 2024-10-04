class HeaderProcessor:
    def __init__(self, header):
        self.__header = header  # Private variable

    def get_header(self):
        return self.__header  # Public method to access private header

    def is_phishing(self):
        # Add logic to analyze the header for phishing indicators
        return "phishing" in self.__header.lower()  # Example condition
