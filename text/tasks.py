from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import requests
from bs4 import BeautifulSoup
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import Word2Vec
from gensim.summarization import summarize


nltk.download('punkt')
nltk.download('stopwords')


def summarize(text, language="english", sentences_count=5):
  parser = PlaintextParser.from_string(text, Tokenizer(language))
  summarizer = LsaSummarizer()
  summary = summarizer(parser.document, sentences_count)
  return ' '.join(str(sentence) for sentence in summary)

def extract_text_from_url(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")

  paragraphs = soup.find_all("p")
  text = " ".join([p.get_text() for p in paragraphs])

  return text

def preprocess_text(text):
  sentences = sent_tokenize(text)
  stop_words = set(stopwords.words("english"))

  words = [word_tokenize(sentence.lower()) for sentence in sentences]
  words = [[word for word in sentence if word.isalnum() and word not in stop_words] for sentence in words]

  return sentences, words

def summarize_text(sentences, words):
  model = Word2Vec(words, min_count=1, size=100, window=5)

  sentence_vectors = []
  for sentence in words:
      sentence_vec = sum([model.wv[word] for word in sentence]) / len(sentence)
      sentence_vectors.append(sentence_vec)

  similarity_matrix = [[model.wv.similarity(w1, w2) for w1 in sentence_vectors] for w2 in sentence_vectors]

  summary = summarize(" ".join(sentences), ratio=0.3, word_count=None, split=False)

  return summary

def summarise_url(url):
  text = extract_text_from_url(url)
  sentences, words = preprocess_text(text)
  return summarize_text(sentences, words)
  
