class Codec:
    def __init__(self):
        self.encodeUrl = {}
        self.decodeUrl = {}
        self.template = 'http://tinyurl.com'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encode:

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
