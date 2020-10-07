from urllib.parse import quote, unquote
class UrlDecode:
    def __init__(self,urlStr):
        self.urlStr = urlStr
    def DecodeUrl(self):
        str = self.urlStr
        return unquote(str, 'utf-8')