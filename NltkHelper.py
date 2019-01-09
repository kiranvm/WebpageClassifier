from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag,RegexpParser,FreqDist
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import wordnet as wn
from string import punctuation	

class NltkHelper:

	#tokenizing below
	def txtTokenizer(tokenType,txt):
		if(tokenType == "txt"):
			return word_tokenize(txt) #word tokenizer below
		elif(tokenType == "snt"):
			return sent_tokenize(txt) #sentence tokenizer below

	#stopword elimination below
	def stopWordEliminator(tokenizedText):
		#print (set(stopwords.words('english'))) #see the list of stop words in library
		stop_words = set(stopwords.words('english'))
		#word_tokens = word_tokenize(txt)
		#filtered_sentence = [w for w in tokenizedText if not w in stop_words]
		filtered_sentence = []

		for w in tokenizedText:
			if w not in stop_words:
				filtered_sentence.append(w)
		return filtered_sentence

	#Stemming done below
	def stemmSentence(tokenizedText):
		stemmed_sentence = []
		ps = PorterStemmer()
		for word in tokenizedText:
			stemmed_sentence.append(ps.stem(word))
		return stemmed_sentence


	#part os speech tagging
	def posTaggin(normalText):	
		custom_sent_tokenizer = PunktSentenceTokenizer()
		tokenized = custom_sent_tokenizer.tokenize(normalText)
		chunks = []

		try:
			for i in tokenized:
				words = word_tokenize(i)
				tagged = pos_tag(words)
				#chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
				chunkGram = r"""Chunk: {<.*>+}
						    }<VB.?|IN|DT|TO>+{"""
				chunkParser = RegexpParser(chunkGram)
				chunked = chunkParser.parse(tagged)
				#chunked.draw()
				#print(tagged)
				#print(chunked)
				for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
					#print(subtree)
					chunks.append(subtree)
					#chunked.draw()
		
		except Exception as e:
			print(str(e))

		return chunks


	def mostCommon(tokenizedText,count):
		#finding frequency distribution
		all_words = FreqDist(tokenizedText)
		return(all_words.most_common(count))

	def findNouns(words):
		results = []
		for w in words:
			desc = wn.synsets(w)
			#print(str(w) +" : "+str(desc))
			if desc:
				tmp = wn.synsets(w)[0].pos()
				#print (w, ":", tmp)
				if tmp == "n":
					results.append(w)
			else:
				ww = ''.join(c for c in w if c not in punctuation)
				if (len(ww)>2):
					#print("word here: ",ww)
					results.append(ww)
		return (results)
