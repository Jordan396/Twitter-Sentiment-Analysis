'''
Python 3.6
This script contains methods to process the text in the tweets.

Methods here are not called directly.
Instead, they are called from either "NLTK_clean_tweet_testing.py" or "TextBlob_clean_tweet_testing.py"

'''
print("Importing tweetProcesser..")

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import csv

sentiment = SentimentIntensityAnalyzer()


def abbreviation_extender():
	'''
	Parses the text and identifies any abbreviated words. 
	The abbreviated words are then converted to their full words.
	This is done with reference to "abbreviations_match.txt".
	'''
	
	#Creating dictionary of abbreviations
	list1 = []
	list2 = []
	print("Creating dictionary of abbreviations..")
	with open("abbreviations_match.txt","r") as myFile:
		for line in myFile.readlines():
			x = line.split("\t")
			list1.append(x[0])
			list2.append(x[1][:-1])
			myDict = dict(zip(list1,list2))
	print("Done creating dictionary of abbreviations.")

	#Convert abbreviated words to their full words
	print("Extending abbreviations..")
	with open("abbreviations_twitter.txt","w",encoding="utf-8",newline="\n") as temporary:
		with open("raw_twitter.txt","r",encoding="utf-8") as commentFile:
			newWriter = csv.writer(temporary, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)	
			
			for line in commentFile.readlines():
				line = line.lower()
				words_changed = []
				comment_words = line.split()
					
				for word in comment_words:
					if word in myDict.keys():
						words_changed.append(word)
						word_position = comment_words.index(word)
						del comment_words[word_position]
						comment_words.insert(word_position, myDict[word])
					
				newWriter.writerow([" ".join(comment_words)])

	print("Conversion completed.")

	
def emoticon_score(review):
	'''
	Adds a score of [-0.05,0.05] to the total score according to the emoticon used.
	This function also strips the tweet of emoticons and returns the clean tweet.
	'''
	emoji_dict = {'💯': 3, '😠': -3, '😧': -3, '😲': 2, '🖤': 3, '💙': 3, '😊': 2, '💔': -3, '👏': 3,
			'🤡': 0, '😰': -2, '😖': -2, '😕': -2, '🤠': 2, '🤞': 2, '😢': -2, '😿': -2, '💘': 3,
			'😞': -2, '😥': -1, '😵': -1, '🤤': 0, '😑': 0, '🤕': -2, '🤒': -1, '😨': -2, '😳': -2,
			'😦': -1, '☹️': -2, '🖕': -4, '👻': -1, '💝': 3, '💚': 3, '😬': -2, '😁': 2, '😀': 2,'🤝': 1,
			'❤️': 3, '♥️': 3, '😍': 3, '😻': 3, '💓': 3, '💗': 3, '🤗': 2, '😯': -1, '👿': -4,
			'😇': 3, '😂': 3, '😹': 3, '💋': 2, '😗': 2, '😽': 2, '😚': 2, '😘': 3, '😙': 2, '😆': 1,
			'👄': 2, '🤥': -2, '😷': -1, '🤑': 0, '🤢': -2, '🤓': -1, '😐': 0, '😶': 0, '👌': 2, '😮': -2,
			'😔': -1, '😣': -2, '😾': -4, '🙏': 1, '👊': -1, '💜': 3, '😡': -4, '🙌': 4, '☺️': 2, '😌': 2,
			'💞': 3, '🤣': 4, '🙄': -1, '😱': -3, '🙀': -3, '💩': -3, '💀': -2, '☠️': -2, '😴': 0, '😪': 0,
			'🙁': -1, '🙂': 1, '😄': 2, '😸': 2, '😃': 2, '😺': 2, '😈': -3, '😏': 2, '😼': 2, '🤧': -2,
			'😭': -3, '💖': 3, '😛': 1, '😝': 0, '😜': -1, '😎': 1, '😓': -1, '😅': 2, '🤔': -1, '👎': -2,
			'👍': 2, '😫': -2, '😤': 0, '💕': 3, '😒': -2, '🙃': 0, '✌️': 2, '😩': -2, '😉': 3, '😟': -3,
			'💛': 3, '😋': 3, '🤐': -1, '<3': 3, ':)':2, ':(':-2, ';-)': 2,';)': 2}
			
	emoticon_counter = 0
	score = 0
	
	for emoticon in emoji_dict.keys():
		condition = False
		while not condition:
			if emoticon in review:
				score += (emoji_dict[emoticon]/10)
				review = review.replace("{}".format(emoticon),"",1)
				emoticon_counter += 1
			else:
				condition = True
	return (review,score)


def sentimentClassifier(wiki, input_score):
	'''
	Used by TextBlob model only!
	Attaches a normalized score and a sentiment category to the tweet.
	Score is normalized for fairer comparison.
	'''
	numberOfSentences = 0
	score = input_score
	for sentence in wiki.sentences:	
		polarity = sentence.sentiment.polarity
		subjectivity = sentence.sentiment.subjectivity
		numberOfSentences += 1
		score += polarity * subjectivity
		
	normalized_score = round(score/numberOfSentences,3)
	
	#Classifying sentence based on score.
	if normalized_score > 0:
		sentiment_label = "positive"
	elif normalized_score < 0:
		sentiment_label = "negative"
	else:
		sentiment_label = "neutral"
	return (normalized_score,sentiment_label)

print("Finished importing tweetProcesser.")