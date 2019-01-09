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
#print (url)
if not Helpers.urlValidator(url):
	print ("URL entered is not valid")
	sys.exit()

webPage = WebHelper(url)

#parsing readable text from the html page below
txt = webPage.text_from_html().lower()
#print (txt)

# Optional Step - writing to a file as temporary backup for troubleshooting
io = IoHelper("output.txt")
io.fileWriter(txt)

#Text cleansing logic below
tokenizedTxt = NltkHelper.txtTokenizer("txt",txt)

#stopWord Elimination below
trimmedTxt = NltkHelper.stopWordEliminator(tokenizedTxt)
#print (trimmedTxt)

#part os speech tagging to identify
#chunks = NltkHelper.posTaggin(txt)
#print(chunks[0])

#stemming the result
stemmedText = NltkHelper.stemmSentence(trimmedTxt)

#Finding most repeated words using frequency distribution
highFreqWords = []
keyWords = NltkHelper.mostCommon(stemmedText,10)
keyWords = dict(keyWords)
for key, value in keyWords.items():
	if key not in string.punctuation:
		highFreqWords.append(key)
#print(output)

result = NltkHelper.findNouns(highFreqWords)
print(result)
