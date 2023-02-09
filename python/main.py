'''
to do:
1. audio to text (att)
	a. get audio file input
	b. run it through whisper
	c. save dict in pkl format
2. get categories (gc)
	a. load dict
	b. clean text
		regex, clean, stopwords, lemmatize
	c. get top 5 repeted words
	d. get closest score for each in sql table
	e. return highest cat score
'''
from att import Audio_To_Text

Audio_To_Text('epi_1221762_medium.mp4')
