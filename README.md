# Basic_Twitter_Sentiment_Analysis

In this tutorial, we shall perform sentiment analysis on tweets using either **TextBlob** and **NLTK**, before classifying them as either positive/neutral/negative. You may wish to compare the accuracy of your results from the two different modules and select the one that best suits your needs. I shall be using the (https://www.kaggle.com/crowdflower/twitter-airline-sentiment "US airline tweets") dataset which can be downloaded from Kaggle. This dataset originates from the *Crowdflower's Data for Everyone library*.

IMPORTANT: The sentiment analysis we shall be performing here is only at the basic level and it serves as a starting point for users who are new to Natural Language Processing. For more accurate industrial applications, I'd recommend checking out (https://spacy.io/ "spacy") or (https://opennlp.apache.org/ "Apache OpenNLP").

## Installation:

#### Modules required:
* beautifulsoup4 (BeautifulSoup)
* nltk (Python's NLTK)
* textblob (TextBlob)
//Vader lexicon, wordnet, punkt

For your convenience, I have attached a *requirements.txt* file containing the modules to install. Simply execute `pip install -r requirements.txt` on your console (after setting the directory path to this project's folder) to install the modules. 

Next, we need to install specific NLTK modules. To do this, open your Python shell and execute `import nltk`. Then, execute `nltk.download()`. The NLTK installer will appear. Select *punkt*, *vader_lexicon* and *wordnet* under "All Packages" and click "Download". You may then close the installer once the download completes.

### Executing the script:

Overview of what each file does:
README.txt --> Information about the folder and everything in it.
raw_twitter.txt --> Contains the raw dataset of tweets.
abbreviations_match.txt --> List of abbreviations and the full words they represent.
stopwords.txt --> List of common english stopwords.
tweetCleaner.py --> Contains methods to clean the twitter text.
tweetProcesser.py --> Contains methods to process the twitter text and for classification based on sentiment.
Compiled Twitter Sentiment.xlxs --> Compiled results of running the scripts.

NLTK_clean_tweet_testing.py                     IMPORTANT: These are the files that we will run to test the models.
NLTK_tweet_testing.py				All other files need not be changed, unless you wish to implement additional changes.
TextBlob_clean_tweet_testing.py			MORE INFORMATION CAN BE FOUND IN THE PYTHON SCRIPT DOCSTRING.
TextBlob_tweet_testing.py


At a high level the sentiment analysis will involve 4 steps:
    Step 1: Data Assembly
    Step 2: Data Processing
    Step 3: Data Exploration or Visualization
    Step 4: Model Building & Validation (train & test)

Let's understand different possible data preprocessing activities:

    *Convert text to lowercase – This is to avoid distinguish between words simply on case.

    *Remove Number – Numbers may or may not be relevant to our analyses. Usually it does not carry any importance in sentiment analysis

    *Remove Punctuation – Punctuation can provide grammatical context which supports understanding. For bag of words based sentiment analysis punctuation does not add value.

    *Remove English stop words – Stop words are common words found in a language. Words like for, of, are etc are common stop words.

    Remove Own stop words(if required) – Along with English stop words, we could instead or in addition remove our own stop words. The choice of own stop word might depend on the domain of discourse, and might not become apparent until we’ve done some analysis.

    *Strip white space – Eliminate extra white spaces.

    Stemming – Transforms to root word. Stemming uses an algorithm that removes common word endings for English words, such as “es”, “ed” and “’s”. For example i.e., 1) “computer” & “computers” become “comput”

    *Lemmatisation – transform to dictionary base form i.e., “produce” & “produced” become “produce”

    Sparse terms – We are often not interested in infrequent terms in our documents. Such “sparse” terms should be removed from the document term matrix.

NOTE: * represents the steps which I have written under "tweetCleaner.py" to clean the Twitter text.

