import os
import pickle
from cleantext import clean
from collections import Counter

import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")

from nltk.stem import WordNetLemmatizer

class Get_Category:
	def __init__(self, text_file, text_data_path = None):
		self.text_data_path = text_data_path if text_data_path else '../data/text/'
		text = self.clean_data(text)
		recurring = self.get_recurring_n(text, n = 5)

	def clean_text(self, text):
		lemmatizer = WordNetLemmatizer()
		text = text.replace('[^A-Za-z0-9 ]+', ' ')
		text = clean(text, clean_all = False, 
						   extra_spaces = True, 
						   stemming = False,
						   stopwords = True, 
						   lowercase = True, 
						   numbers = True, 
						   punct = True
					)
		text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
		return text

	def get_recurring_n(self, text, n = 5):
		return Counter(text).most_common(n)

	def score_mapping(self, recurring, category_list):
		return None
