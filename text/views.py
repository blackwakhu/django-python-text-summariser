from django.shortcuts import render
from .forms import SummaryForm
from .tasks import summarize

# Create your views here.

def index(request):
  return render(request, 'index.html')

def summariser(request):
  return render(request, "summariser.html", {"form": SummaryForm()})
  
def summarise_text(request):
  form = SummaryForm()
  if request.method == "POST":
    myform = SummaryForm(request.POST)
    if myform.is_valid():
      text = myform.cleaned_data['inptext']
      lang = "english"
      count = myform.cleaned_data['count']
      output = summarize(text, lang, count)
  return render(request, 'summariser.html', {"form": form, "output": output})

def summarise_url(request):
  return render(request, 'summariser.html', {{"form": SummaryForm()}})
