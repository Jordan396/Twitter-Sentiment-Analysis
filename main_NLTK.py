'''
Python 3.6, Python NLTK model

This file contains the code required to test the various models under the Python NLTK model.
The results will be written into their individual output file in a CSV format.

Instructions to execute the file can be found at the bottom of the file.
'''
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import tweetCleaner
import tweetProcesser


sentiment = SentimentIntensityAnalyzer()


def NLTKCleanRaw():
	'''
	Raw NLTK model
	'''
	tweet_counter = 0
	with open("results_nltk_raw.txt","w", encoding = "utf-8") as postresults:
		newWriter = csv.writer(postresults, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		with open("raw_twitter.txt","r", encoding = "utf-8") as postprocessed:
			for line in postprocessed.readlines():
				total_score = 0
				tweet_counter += 1
				
				try:
					print("Processing tweet: {}".format(tweet_counter))
					tweet = tweetCleaner.lowercase(line)
					tweet = tweetCleaner.StopWordRemover(tweet)
					tweet = tweetCleaner.removeSpecialChars(tweet)
					tweet = tweetCleaner.removeAllNonAlpha(tweet)
					tweet = tweetCleaner.lemmatizer(tweet)
				
					lines_list = tokenize.sent_tokenize(tweet)
					
					for sentence in lines_list:
						ss = sentiment.polarity_scores(sentence)
						total_score -= ss["neg"]
						total_score += ss["pos"]
					
					total_score = round(total_score,3)
					
					if total_score == 0:
						newWriter.writerow([0, "neutral"])
					elif total_score > 0:
						newWriter.writerow([total_score, "positive"])
					else:
						newWriter.writerow([total_score, "negative"])
				
				except:
					newWriter.writerow([0, "neutral"])
					print("ERROR processing tweet: {}".format(tweet_counter))

def NLTKCleanAbbrev():
	"""
	NLTK model with extended abbreviations
	"""
	tweet_counter = 0
	tweetProcesser.abbreviation_extender()
	with open("results_nltk_abbrev.txt","w", encoding = "utf-8") as postresults:
		newWriter = csv.writer(postresults, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		with open("abbreviations_twitter.txt","r", encoding = "utf-8") as postprocessed:
			for line in postprocessed.readlines():
				total_score = 0
				tweet_counter += 1
				
				try:
					print("Processing tweet: {}".format(tweet_counter))
					tweet = tweetCleaner.StopWordRemover(tweet)
					tweet = tweetCleaner.removeSpecialChars(tweet)
					tweet = tweetCleaner.removeAllNonAlpha(tweet)
					tweet = tweetCleaner.lemmatizer(tweet)
					
					lines_list = tokenize.sent_tokenize(tweet)
					for sentence in lines_list:
						ss = sentiment.polarity_scores(sentence)
						total_score -= ss["neg"]
						total_score += ss["pos"]
					
					total_score = round(total_score,3)
					
					if total_score == 0:
						newWriter.writerow([0, "neutral"])
					elif total_score > 0:
						newWriter.writerow([total_score, "positive"])
					else:
						newWriter.writerow([total_score, "negative"])
					
				except:
					newWriter.writerow([0, "neutral"])
					print("ERROR processing tweet: {}".format(tweet_counter))
					
def NLTKCleanEmoji():
	"""
	NLTK model with emoticon scoring
	"""
	tweet_counter = 0
	with open("results_nltk_emoji.txt","w", encoding = "utf-8") as postresults:
		newWriter = csv.writer(postresults, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		with open("raw_twitter.txt","r", encoding = "utf-8") as postprocessed:
			for line in postprocessed.readlines():
				total_score = 0
				tweet_counter += 1
				
				try:
					print("Processing tweet: {}".format(tweet_counter))
					tweet = tweetCleaner.lowercase(line)
					tweet = tweetCleaner.StopWordRemover(tweet)
					tweet = tweetCleaner.removeSpecialChars(tweet)
					tweet,total_score = tweetProcesser.emoticon_score(tweet)
					tweet = tweetCleaner.removeAllNonAlpha(tweet)
					tweet = tweetCleaner.lemmatizer(tweet)
					
					lines_list = tokenize.sent_tokenize(tweet)
					
					for sentence in lines_list:
						ss = sentiment.polarity_scores(sentence)
						total_score -= ss["neg"]
						total_score += ss["pos"]
					
					total_score = round(total_score,3)
					
					if total_score == 0:
						newWriter.writerow([0, "neutral"])
					elif total_score > 0:
						newWriter.writerow([total_score, "positive"])
					else:
						newWriter.writerow([total_score, "negative"])
						
				except:
					newWriter.writerow([0, "neutral"])
					print("ERROR processing tweet: {}".format(tweet_counter))
				
				
def NLTKCleanAbbrevEmoji():
	"""
	NLTK model with extended abbreviations AND emoticon scoring
	"""
	tweet_counter = 0
	tweetProcesser.abbreviation_extender()
	with open("results_nltk_abbrev_emoji.txt","w", encoding = "utf-8") as postresults:
		newWriter = csv.writer(postresults, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		with open("abbreviations_twitter.txt","r", encoding = "utf-8") as postprocessed:
		
			for line in postprocessed.readlines():
				total_score = 0
				tweet_counter += 1
			
				try:
					print("Processing tweet: {}".format(tweet_counter))
					tweet = tweetCleaner.lowercase(line)
					tweet = tweetCleaner.StopWordRemover(tweet)
					tweet = tweetCleaner.removeSpecialChars(tweet)
					tweet,total_score = tweetProcesser.emoticon_score(tweet)
					tweet = tweetCleaner.removeAllNonAlpha(tweet)
					tweet = tweetCleaner.lemmatizer(tweet)
					
					lines_list = tokenize.sent_tokenize(tweet)
					
					for line in lines_list:
						ss = sentiment.polarity_scores(line)
						total_score -= ss["neg"]
						total_score += ss["pos"]
					
					total_score = round(total_score,3)
					
					if total_score == 0:
						newWriter.writerow([0, "neutral"])
					elif total_score > 0:
						newWriter.writerow([total_score, "positive"])
					else:
						newWriter.writerow([total_score, "negative"])

				except:
					newWriter.writerow([0, "neutral"])
					print("ERROR processing tweet: {}".format(tweet_counter))
					
					
					
print("====================TEST BEGIN=======================")

'''
BASIC: This is the main function we will be executing.
It combines all the cleaning and processing steps described in the GitHub README.
Run this script in your python command shell.
'''
NLTKCleanAbbrevEmoji()
'''
ADVANCED: Sometimes, performing excessive cleaning operations on the input may worsen the accuracy of the model.
Hence, here are several other models you may wish to test for accuracy comparison. 
The description of the models may be found under the individual functions above.
To test a model, simply comment the above "Basic" model and uncomment any of the models below. 
Run this script in your python command shell.
'''

#NLTKCleanRaw()
#NLTKCleanAbbrev()
#NLTKCleanEmoji()

print("====================TEST END=========================")
					
					
					
					
					
					
					
					
					
					
					
					