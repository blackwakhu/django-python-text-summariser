from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk 

nltk.download('punkt')


def summarize(text, language="english", sentences_count=5):
  parser = PlaintextParser.from_string(text, Tokenizer(language))
  summarizer = LsaSummarizer()
  summary = summarizer(parser.document, sentences_count)
  return ' '.join(str(sentence) for sentence in summary)

