import validators
import string

class Helpers:
	def urlValidator(txt):
		return validators.url(txt)

	def removePunctuation(tokenizedList):
		x = [''.join(c for c in tokenizedList if c not in string.punctuation) for s in tokenizedList]
		x = [s for s in x if s]
		return x
