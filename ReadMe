Web Classfier Project.
Given any page (URL), the program will classify the page, and return a list of relevant topics. 

Tools Required:
+
	Python - 3.0+ /url "https://www.python.org/downloads/"
+
Dependancies :
+
	1. Python NLTK Library 
	.................
	> pip install nltk
	.................

	2. Python BeautifulSoup	
	.................
	> pip install BeautifulSoup
	.................

	3. Python urllib	
	.................
	> pip install urllib
	.................

	4. Python requests	
	.................
	> pip install requests
	.................
+

How to run:
+
	Program takes one command line argument which should be a valid url.
	Syntax : python webClassifier.py <url> 
	Example as given below.
	.................
	> python webClassifier.py https://www.cnn.com/2013/06/10/politics/edward-snowden-profile/
	.................	
+

Design Details:
+
	1. webClassifier.py - Main File to run
	2. NltkHelper.py - Helper functions using NLTK library
	3. WebHelper.py - Web parsing helper functions
	4. IOHelper.py	- I/O operations helper functions
	5. Helpers.py	- Miscellenous helper functions
+

Process Abstract:
+
	1. Project parses readable text from a webpage
	2. Word tokenization is performed on the result
	3. Stop words from the word tokenized text is removed
	4. Stemming is performed on this
	5. Frequency distribution is used to find most top repeated words
	6. Nouns from the most repeated words are given as the relevant keywords defining the page
+

In progress:
+
	1. Using part of Speech tagging to identify group of nouns
	2. Identifying relevant bigrams/trigrams from the page.
+

Bugs:
+
	1. Project doesn't support amazon webpages as amazon prevents web crawling through program. Alternative approach to be checked.
+

