from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import urlopen
import requests

class WebHelper:
	page = ""
	html = ""

	def tag_visible(element):
		if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
			return False
		if isinstance(element, Comment):
			return False
		return True

	def text_from_html(self):
		soup = BeautifulSoup(self.html, 'html.parser')
		texts = soup.findAll(text=True)
		visible_texts = filter(WebHelper.tag_visible, texts)  
		return u" ".join(t.strip() for t in visible_texts)


	def __init__(self,url):
		self.page = requests.get(url)
		self.html = self.page.text


