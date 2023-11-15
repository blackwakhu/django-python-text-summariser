from django import forms
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


class Data(forms.Form):
    number_of_sentences = forms.IntegerField()
    text_data = forms.CharField(widget=forms.Textarea)


def summarise_text(text, num_sentences=5):
    """this function will do all the summarising"""
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summariser = LsaSummarizer()
    summary = summariser(parser.document, num_sentences)
    return " ".join([str(sentence) for sentence in summary])

