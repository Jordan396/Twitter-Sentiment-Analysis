'''
Python 3.6
This script contains functions to clean the text in the tweets.

Methods here are not called directly.
Instead, they are called from either "NLTK_clean_tweet_testing.py" or "TextBlob_clean_tweet_testing.py"
'''

print("Importing tweetCleaner...")

from bs4 import BeautifulSoup
import re
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

"""
Returns a list of stopwords called StopWordList.
The file containing the stopwords is titled "stopwords.txt".
"""
def StopWordListCreator():
	StopWordList = []
	with open("stopwords.txt","r",encoding="utf-8") as stopwords:
		for stopword in stopwords.readlines():
			StopWordList.append(stopword[:-1])
	return StopWordList


def StopWordRemover(tweet):
	'''
	Removes all stopwords in the tweet, w.r.t. the StopWordList created above.
	'''
	tweet_words = tweet.split()
	new_tweet = []		
	for word in tweet_words:
		if word in StopWordListCreator():
			pass
		else:
			new_tweet.append(word)		
	return (" ").join(new_tweet) 


def lowercase(tweet):
	'''
	Returns the tweet in lowercase.
	'''
	return tweet.lower()


def removeSpecialChars(tweet):
	'''
	Removes special characters which are specifically found in tweets.
	'''
	#Converts HTML tags to the characters they represent
	soup = BeautifulSoup(tweet, "html.parser")
	tweet = soup.get_text()
	
	#Convert www.* or https?://* to empty strings
	tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
	
    #Convert @username to empty strings
	tweet = re.sub('@[^\s]+','',tweet)
	
    #Remove additional white spaces
	tweet = re.sub('[\s]+', ' ', tweet)
	
    #Replace #word with word
	tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
	
    #Trims the tweet
	tweet = tweet.strip('\'"')
	
	return tweet
	

def removeAllNonAlpha(tweet):
	'''
	Remove all characters which are not alphabets, numbers or whitespaces.
	'''
	tweet = re.sub('[^A-Za-z0-9 ]+','', tweet)
	return tweet  

def lemmatizer(tweet):
	'''
	Attempts to replace every individual word with it's root word.
	'''
	word_list = []
	for word in tweet.split():
		word_list.append(wordnet_lemmatizer.lemmatize(word))
	return (" ".join(word_list))
	
print("Finished importing tweetCleaner.")