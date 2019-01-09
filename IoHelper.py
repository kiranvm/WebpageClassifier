class IoHelper:

	fName = ""

	def __init__(self,fileName):
		self.fName = fileName

	def fileReader(self):
		text_file = open(self.fName, "r")
		txt = text_file.read()
		text_file.close()
		return txt
		#print(txt)

	def fileWriter(self,text):
		text_file = open(self.fName, "w")
		text_file.write(text)
		text_file.close()
