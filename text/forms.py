from django import forms


class SummaryForm(forms.Form):
  inptext = forms.CharField(label="Enter text to summarise", widget=forms.Textarea(attrs={'rows': '10'}))
  count = forms.IntegerField(label="Enter number of sentences to summarise", widget=forms.NumberInput(attrs={'min':'3'}))

class UrlSummaryForm(forms.Form):
  inptext = forms.CharField(label="enter the url", widget=forms.TextInput(attrs={'rows': '1'}))
  count = forms.IntegerField(label="Enter number of sentences to summarise", widget=forms.NumberInput(attrs={'min':'3'}))
