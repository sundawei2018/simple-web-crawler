'''
Created on May 29, 2017

@author: Dave
'''
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # // /view/123.htm <a href="/wiki/Measuring_programming_language_popularity" title="Measuring programming language popularity">widely used</a>
        # r"/view/\d+\.htm"
        links = soup.find_all('a', href = re.compile(r"/wiki/.*"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        # <h1 id="firstHeading" class="firstHeading" lang="en">Python (programming language)</h1>
        title_node = soup.find('h1', class_ = "firstHeading")
        res_data['title'] = title_node.get_text()
        # <div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><table class="infobox vevent" style="width:22em">
        summary_node = soup.find('div', class_ = "mw-content-ltr")
        res_data['summary']  = summary_node.get_text()
        res_data['url'] = page_url
        return res_data
    
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return 
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls, new_data
    
    



