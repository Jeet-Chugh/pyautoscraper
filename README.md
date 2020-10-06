# pyautoscraper  
#### Author: Jeet Chugh  

###### pyautoscraper is a A lightweight module which automates webscraping and gathering HTML elements within Python 3

### Features:
  - Find elements by searching for tags, attributes, classes, id's, and more
  - Parse through Cloudflare protected sites (NOT CAPTCHA)
  - Install easily with pip
  - Lightweight, only uses cloudscraper and BS4
#### [Github Link](https://github.com/Jeet-Chugh/pyautoscraper) | [PyPi Link](https://pypi.org/project/pyautoscraper/) | [Example Code Link](https://raw.githubusercontent.com/Jeet-Chugh/pyautoscraper/master/example.py)  

  Quick and Easy Installation via PIP: `pip install pyautoscraper`  

Import Statement:  ``from pyautoscraper.scraper import Scraper``  

Dependencies: *bs4, cloudscraper*  

#### Code License: MIT  

# Documentation  

###### Documentation is split into 2 sections. First is the 'Part' Class and second is the 'Query' Function.  

---  

#### 'Scraper' Class:  

The 'Scraper' class takes in an input of a URL as a string, and has many methods that return specific chunks of data.  

**Import:**  

``from pyautoscraper.scraper import Scraper``  

**Instantiation:**  

``webscraper = Scraper('URL') # Takes in url string (with https://)``  

``another_scraper = Scraper('Second URL') # Instantiate multiple Scrapers though variables``  

#### **'Scraper' Methods:**  

##### Scraper will raise a URLerror if the request is unsuccessful. Scraper will return None if no elements are found.

---  

``Scraper('url').find(tag, **attributes)``  --> ``Scraper('URL').find('h1', class_='blog-title')``

returns a string containing the first HTML element that matches your parameters. To find classes, use the 'class_' keyword argument.

 (``<h1 class="blog-title>Title</h1>"``)  

---  

``Scraper('url').findAll(tag, **attributes)`` --> ``Scraper('URL').findAll('p')``

returns a list of strings, containing all the HTML elements that match the parameters.

(``[<p>first</p>, <p>second</p>, <p>third</p>]``)  

---  

`Scraper('url').findText()`  

returns a string containing the text content of the HTML, with all tags and attributes stripped.

(``h1 text       paragraph text            span text        h5 text        im in a div tag``)  

---  

`Scraper('url').findLinks()`  

returns a list of all http/https links in a tags within the HTML code of the page.

(``[https://www.google.com, https://www.github.com]``)  

---  

`Scraper('url').findJS()`  

returns a list containing strings, which represent the string tags within the HTML code.

Example Dictionary:`{'model':'Intel','Core Clock':'3.2Ghz','TDP':'95W','Socket':'LGA1155'}`  

---  

`Scraper('url').findElementByID(IDname)`  

returns a string containing the first HTML element that matches your IDname.

(``<div id="database_div">content</div>``)  

---  

`Scraper('url').findElementByClass(className)`  

returns a string containing the first HTML element that matches your className.

(``<div class="database_div">content</div>``)  

---  

`Scraper('url').findComments()`  

returns a list of strings, containing all the HTML comments within the code.

(``['<!-- a comment -->','<!-- ANOTHER COMMENT -->']``)  

---  


Thank you for reading the documentation. If you need an example using all these methods, go to [link]  


If you have issues, report them to the github project link.
