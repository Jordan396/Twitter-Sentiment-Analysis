# Basic_Twitter_Sentiment_Analysis
### Overview
In this tutorial, we shall perform sentiment analysis on tweets using **TextBlob** and **NLTK**. You may wish to compare the accuracy of your results from the two modules and select the one you prefer. 

I shall be using the [US airline tweets](https://www.kaggle.com/crowdflower/twitter-airline-sentiment) dataset which can be downloaded from Kaggle. This dataset originates from the *Crowdflower's Data for Everyone library*.

**IMPORTANT**: The sentiment analysis we shall be performing is at the basic level and it serves as a starting point to those new to Natural Language Processing. For more accurate industrial applications, I'd recommend checking out [Spacy](https://spacy.io/) or [Apache OpenNLP](https://opennlp.apache.org/).

#### Overview of what each file does:
| File                       | Description                                           |
| :-------------------------:|:----------------------------------------------------- |
| README.txt                 |Information about the repository and everything in it  |
| raw_twitter.txt            |Contains the raw dataset of tweets                     |
| abbreviations_match.txt    |List of abbreviations and they words they represent    |
| stopwords.txt              |List of common english stopwords                       |
| tweetCleaner.py            |Contains functions to clean the twitter text           |
| tweetProcesser.py          |Contains functions to process the twitter text         |
| Compiled_Results.xlxs      |Compiled results of running the scripts                |
| main_NLTK.py               | Contains the NLTK models we will be executing         |
| main_TextBlob.py           | Contains the TextBlob models we will be executing     |

### Concepts (Optional, for your understanding)

At a high level the sentiment analysis will involve 4 steps:
⋅⋅1. Data Assembly
⋅⋅2. Data Processing
⋅⋅3. Data Exploration or Visualization
⋅⋅4. Model Building & Validation

Let's understand different data preprocessing activities:
..* Convert text to lowercase – Allows us to deal with uniform case text.
..* Remove numbers – Numbers usually do not carry any importance in sentiment analysis
..* Remove punctuation – Punctuation can provide grammatical context which supports understanding. For bag of words based sentiment analysis punctuation does not add value.
..* Remove stop words – Stop words are common words found in a language. Words like for, of, are etc are common stop words.
..* Strip white space – Eliminate extra white spaces.
..* *Stemming* – Transforms to root word. Stemming uses an algorithm that removes common word endings for English words, such as “es”, “ed” and “’s”. 
..* Lemmatisation – Transform to dictionary base form i.e., “produce” & “produced” become “produce”
..* *Sparse terms* – We are often not interested in infrequent terms in our documents. Such “sparse” terms should be removed from the document term matrix.

NOTE: Activites in italics were not dealt with in our models.


## Installation
* beautifulsoup4
* nltk
* textblob

For your convenience, I have attached a *requirements.txt* file containing the modules to install. Simply execute `pip install -r requirements.txt` on your console (after setting the directory path to this project's folder) to install the modules. 

Next, we need to install specific NLTK modules. To do this, open your Python shell and execute `import nltk`. Then, execute `nltk.download()`. The NLTK installer will appear. Select *punkt*, *vader_lexicon* and *wordnet* under "All Packages" and click "Download". Once the download completes, you may close the installer.

## Executing the script





