from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.plaintext import PlaintextParser
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
import nltk 


nltk.download('punkt')
nltk.download('stopwords')


def summarize(text, language="english", sentences_count=5):
  """this function will take the data that was colected from the user and summarize it"""
  parser = PlaintextParser.from_string(text, Tokenizer(language))
  summarizer = LsaSummarizer()
  summary = summarizer(parser.document, sentences_count)
  return ' '.join(str(sentence) for sentence in summary)


def summary_url(url, language, count):
  parser = HtmlParser.from_url(url, Tokenizer(language))
  summarizer = LsaSummarizer(Stemmer(language))
  summary = summarizer(parser.document, count)
  return ' '.join(str(sentence) for sentence in summary)
  
  
  
