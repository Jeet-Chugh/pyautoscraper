from bs4           import BeautifulSoup, Comment
import requests

class Scraper():

    def __init__(self, URL):
        self.HTML = self.__scrape(URL)
        self.URL = URL

    def find(self, tag, **kwargs):
        return self.__find("find", tag, kwargs)

    def findAll(self, tag, **kwargs):
        return self.__find("findAll", tag, kwargs)

    def findText(self):
        return self.HTML.get_text()

    def findLinks(self):
        return [x['href'] for x in self.HTML.find_all('a', href=True) if x['href'].startswith('http')]

    def findJS(self):
        return self.HTML.find_all("script")

    def findElementByID(self, ID):
        return self.HTML.find(id=ID)

    def findElementByClass(self, className):
        return self.HTML.find(class_=className)

    def findComments(self):
        return self.HTML.find_all(string=lambda text: isinstance(text, Comment))

    def __find(self, type, tag, kwargs):
        if tag[0] == '<' and tag[-1] == '>':
            tag = tag.replace('<', '').replace('>', '')
        try:
            if "class_" in kwargs:
                kwargs["class"] = kwargs["class_"]
                del kwargs["class_"]
            if type == 'find':
                result = self.HTML.find(tag, attrs=kwargs)
            elif type == "findAll":
                result = self.HTML.findAll(tag, attrs=kwargs)
            return result
        except:
            return None

    def __scrape(self, URL):
        try:
            request = requests.get(URL).content
            return BeautifulSoup(request, 'html.parser')
        except:
            raise URLerror("Invalid URL")

class URLerror(Exception):
    pass
class WebscrapingError(Exception):
    pass

if __name__ == "__main__":
    scraper = AutoScraper("https://webscraper.io/test-sites/e-commerce/allinone")
    print(scraper.HTML)
