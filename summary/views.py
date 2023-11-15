from django.shortcuts import render, redirect

# Create your views here.

from .forms import Data, summarise_text


def index(request):
    """this is the index view in the summary app"""
    context = {
        "form": Data()
    }
    return render(request, "index.html", context)


def get_summary(request):
    """this will be the function that will return the summary of the text"""
    if request.method == "POST":
        myData = Data(request.POST)
        if myData.is_valid():
            num = myData.cleaned_data["number_of_sentences"]
            data = myData.cleaned_data["text_data"]
            word = summarise_text(data, num)
            return redirect("display summary", word)
    return redirect("display summary", "No data entered")


def display_results(request, word):
    """this will display the results of the function"""
    context = {
        "form": Data(),
        "name": word
    }
    return render(request, "index.html", context)
