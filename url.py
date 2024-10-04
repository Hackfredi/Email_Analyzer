import re

class URLProcessor:
    def __init__(self, body):
        self.__body = body  # Private variable
        self.__urls = self.__extract_urls()  # Private method

    def __extract_urls(self):
        return re.findall(r'(https?://[^\s]+)', self.__body)

    def get_urls(self):
        return self.__urls  # Public method to access private URLs

    def check_malicious_urls(self):
        # Add logic to analyze URLs for phishing
        malicious_domains = ["malicious.com", "phishing.com"]
        return [url for url in self.__urls if any(domain in url for domain in malicious_domains)]
