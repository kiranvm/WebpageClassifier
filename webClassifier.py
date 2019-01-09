#Imports
import sys
from Helpers import Helpers
import string

#user defined classes below
from IoHelper import IoHelper
from WebHelper import WebHelper
from NltkHelper import NltkHelper

#reading the url supplied as command line argument
url = str(sys.argv[1])
print (url)
if not Helpers.urlValidator(url):
	print ("URL entered is not valid")
	sys.exit()

webPage = WebHelper(url)

#parsing readable text from the html page below
txt = webPage.text_from_html().lower()
print (txt)

# Optional Step - writing to a file as temporary backup for troubleshooting
io = IoHelper("output.txt")
io.fileWriter(txt)

#Text cleansing logic below
tokenizedTxt = NltkHelper.txtTokenizer("txt",txt)

#stopWord Elimination below
trimmedTxt = NltkHelper.stopWordEliminator(tokenizedTxt)
#print (trimmedTxt)

#Finding most repeated words using frequency distribution
keyWords = NltkHelper.mostCommon(trimmedTxt,20)
print(keyWords)
keyWords = dict(keyWords)
for key, value in keyWords.items():
	if key not in string.punctuation:
		print (key)
