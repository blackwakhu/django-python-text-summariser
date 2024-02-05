from django.shortcuts import render
from .forms import SummaryForm, UrlSummaryForm
from .tasks import summarize, summarise_url

# Create your views here.

def index(request):
  """this is the index page that acts as the home page"""
  return render(request, 'index.html')

def summariser(request):
  """this will act as the page for the summarise text functions"""
  return render(request, "summariser.html", {
    "form": SummaryForm(),
    "urlform": UrlSummaryForm()
  })
  
def summarise_text(request):
  """this will act as the route that will summarise document text"""
  form = SummaryForm()
  if request.method == "POST":
    myform = SummaryForm(request.POST)
    if myform.is_valid():
      text = myform.cleaned_data['inptext']
      lang = "english"
      count = myform.cleaned_data['count']
      output = summarize(text, lang, count)
  return render(request, 'summariser.html', {
    "form": form, 
    "output": output,
    "urlform": UrlSummaryForm()
  })


def summarise_url(request):
  """this is the route that will act as the page for the summarise url functions"""
  form = UrlSummaryForm()
  if request.method == "POST":
    myform = UrlSummaryForm(request.POST)
    if myform.is_valid():
      url = myform.cleaned_data['inptext']
      lang = "english"
      count = myform.cleaned_data['count']
      output = summarise_url(url, lang, count)
  return render(request, 'summariser.html', {
    "form": SummaryForm(), 
    "urlform": form,
    "output": output
  })
