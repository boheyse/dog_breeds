from html.parser import HTMLParser
from urllib import parse

url = parse.urlsplit("https://www.akc.org/dog-breeds/affenpinscher/", scheme = "/dog-breeds/")

breed = url[2]
breed = breed[12:-1]
print(breed)