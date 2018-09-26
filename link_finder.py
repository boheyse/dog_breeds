from html.parser import HTMLParser
from urllib import parse



class html_finder(HTMLParser):
    
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links() = set()
        
    def handle_starttag(self, tag, attrs):
        if tag == 'option':
            for (attribute, value) in attrs:
                if attribute == 'value':
                    url = parse.urlsplit    #splits the url into a size 5 array 
                    breed = url[2]          # /dog-breed/name is in position 2
                    breed = breed[12:-1]    # We want the name, so ignore the first 12 letters and the last
                    print(breed)        
                    
    
    def error(self, message):
        pass
                    