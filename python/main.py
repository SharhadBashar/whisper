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

import os
import sys
import time

def make_folders():
	if (not os.path.isdir('../data')):
		os.makedirs('../data')
	if (not os.path.isdir('../data/audio')):
		os.makedirs('../data/audio')
	if (not os.path.isdir('../data/text')):
		os.makedirs('../data/text')
	if (not os.path.isdir('../data/category')):
		os.makedirs('../data/category')

def get_categories():
	None

if __name__ == '__main__':
	make_folders()
	get_categories()
	try:
		command = sys.argv[1].lower()
	except IndexError:
		print('No command found. Please type transcribe or -t for transcribing, or categorize or -c to get categories')
		exit()

	if (command == 'transcribe' or sys.argv[1] == '-t'):
		from att import Audio_To_Text
		try:
			audio_file = sys.argv[2]
		except IndexError:
			print('No audio file passed. Please pass an audio file to be transcribed')
			exit()
		start = time.time()
		Audio_To_Text(audio_file)
		print('Finished transcribing in {} s'.format(round(time.time() - start, 2)))

	elif (command == 'categorize' or sys.argv[1] == '-c'):
		from get_category import Get_Category
		try:
			text_file = sys.argv[2]
		except IndexError:
			print('No text file passed. Please pass a text file to get categories')
			exit()
		start = time.time()
		Get_Category(text_file)
		print('Finished getting categories in {} s'.format(round(time.time() - start, 2)))

	else:
		print('Command {} not understood. Please type transcribe or t for transcribing, or categorize or c to get categories'.format(command))

