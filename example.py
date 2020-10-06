# AUTHOR: Jeet Chugh
# Example use of pyautoscraper

# import statement
from pyautoscraper.scraper import Scraper

# Instantiate the class with a URL you want to webscrape from
scraper = Scraper("https://webscraper.io/test-sites/e-commerce/allinone")

# find the first p tag on the site
print(scraper.find('p'))

# find all the span tags on the sites (as a list)
print(scraper.findAll('span'))

# find all the text within the HTML code
print(scraper.findText())

# find all the a tags with href attributes (Links)
print(scraper.findLinks())

# find all the JavaScript code (in script tags)
print(scraper.findJS())

# You can look up elements by class by: scraper.findElementByClass(className)
# or look up by ID with: scraper.findElementByID(ID)

# find all the HTML comments in the code
print(scraper.findComments())
