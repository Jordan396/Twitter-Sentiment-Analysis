'''
Python 3.6, TextBlob model

This file contains the code required to test the various models under the TextBlob model.
The results will be written into their individual output file in a CSV format.

Instructions to execute the file can be found at the bottom of the file.
'''

import tweetProcesser
import tweetCleaner
import csv
from textblob import TextBlob

def TextBlobCleanRaw():
	'''
	Raw TextBlob model
	Our current model uses the pre-cleaned raw TextBlob model.
	'''
	tweet_counter = 0
	with open("results_textblob_raw.txt","w",encoding="utf-8") as preresults:
		newWriter = csv.writer(preresults, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		with open("raw_twitter.txt","r",encoding="utf-8") as preproccessed:
			for line in preproccessed.readlines():
				tweet_counter += 1
					
				try:
					print("Processing tweet: {}".format(tweet_counter))
					tweet = tweetCleaner.lowercase(line)
					tweet = tweetCleaner.StopWordRemover(tweet)
					tweet = tweetCleaner.removeSpecialChars(tweet)
					tweet = tweetCleaner.removeAllNonAlpha(tweet)
					tweet = tweetCleaner.lemmatizer(tweet)
					
					wiki = TextBlob(tweet)
					normalized_score, sentiment_label = tweetProcesser.sentimentClassifier(wiki, 0)
					newWriter.writerow([normalized_score, sentiment_label,tweet])
					
				except:
					newWriter.writerow(["0","neutral", "BLANK"])
					print("ERROR processing tweet: {}".format(tweet_counter))


def TextBlobCleanAbbrev():
	'''
	TextBlob model with abbreviations extended.
	'''
	tweet_counter = 0
	tweetProcesser.abbreviation_extender()
	with open("results_textblob_abbrev.txt","w",encoding="utf-8") as postresults:
		newWriter = csv.writer(postresults, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		with open("abbreviations_twitter.txt","r",encoding="utf-8") as postprocessed:
			for line in postprocessed.readlines():
				tweet_counter += 1
				try:
					print("Processing tweet: {}".format(tweet_counter))
					tweet = tweetCleaner.StopWordRemover(line)
					tweet = tweetCleaner.removeSpecialChars(tweet)
					tweet = tweetCleaner.removeAllNonAlpha(tweet)
					tweet = tweetCleaner.lemmatizer(tweet)
					
					wiki = TextBlob(tweet)
					normalized_score, sentiment_label = tweetProcesser.sentimentClassifier(wiki, 0)
					newWriter.writerow([normalized_score, sentiment_label, tweet])
				except:
					newWriter.writerow(["0","neutral", "BLANK"])
					print("ERROR processing tweet: {}".format(tweet_counter))
					
					
def TextBlobCleanEmoji():
	'''
	TextBlob model with Emoticon scoring.
	'''
	tweet_counter = 0
	with open("results_textblob_emoji.txt","w",encoding="utf-8") as preresults:
		newWriter = csv.writer(preresults, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		with open("raw_twitter.txt","r",encoding="utf-8") as preproccessed:
			for line in preproccessed.readlines():
				tweet_counter += 1
				try:
					print("Processing tweet: {}".format(tweet_counter))
					tweet = tweetCleaner.lowercase(line)
					tweet = tweetCleaner.StopWordRemover(tweet)
					tweet = tweetCleaner.removeSpecialChars(tweet)
					tweet,score = tweetProcesser.emoticon_score(tweet)
					tweet = tweetCleaner.removeAllNonAlpha(tweet)
					tweet = tweetCleaner.lemmatizer(tweet)
						
					wiki = TextBlob(tweet)
					normalized_score, sentiment_label = tweetProcesser.sentimentClassifier(wiki, score)
					newWriter.writerow([normalized_score, sentiment_label, tweet])
					
				except:
					newWriter.writerow(["0","neutral", "ERROR"])
					print("ERROR processing tweet: {}".format(tweet_counter))
				
				
def TextBlobCleanAbbrevEmoji():
	'''
	TextBlob model with Emoticon scoring and extended abbreviations.
	'''
	tweet_counter = 0
	tweetProcesser.abbreviation_extender()
	with open("results_textblob_abbrev_emoji.txt","w",encoding="utf-8") as preresults:
		newWriter = csv.writer(preresults, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		with open("abbreviations_twitter.txt","r",encoding="utf-8") as preproccessed:
			for line in preproccessed.readlines():
				tweet_counter += 1
				try:
					print("Processing tweet: {}".format(tweet_counter))
					tweet = tweetCleaner.StopWordRemover(line)
					tweet = tweetCleaner.removeSpecialChars(tweet)
					tweet,score = tweetProcesser.emoticon_score(tweet)
					tweet = tweetCleaner.removeAllNonAlpha(tweet)
					tweet = tweetCleaner.lemmatizer(tweet)
						
					wiki = TextBlob(tweet)
					normalized_score, sentiment_label = tweetProcesser.sentimentClassifier(wiki, score)
					newWriter.writerow([normalized_score, sentiment_label, tweet])
					
				except:
					newWriter.writerow(["0","neutral", "ERROR"])
					print("ERROR processing tweet: {}".format(tweet_counter))
					
					
					
print("====================TEST BEGIN=======================")
'''
BASIC: This is the main function we will be executing.
It combines all the cleaning and processing steps described in the GitHub README.
Run this script in your python command shell.
'''
TextBlobCleanAbbrevEmoji()

'''
ADVANCED: Sometimes, performing excessive cleaning operations on the input may worsen the accuracy of the model.
Hence, here are several other models you may wish to test for accuracy comparison. 
The description of the models may be found under the individual functions above.
To test a model, simply comment the above "Basic" model and uncomment any of the models below. 
Run this script in your python command shell.
'''

#TextBlobCleanRaw()
#TextBlobCleanAbbrev()
#TextBlobCleanEmoji()

print("====================TEST END=========================")