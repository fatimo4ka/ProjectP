from django.shortcuts import render
from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup
import csv
import os


def main_page(request):
    return render(request, 'main\Main.html')

def research_page(request):
    return render(request, 'main\Research.html')

def author_page(request):
    return render(request, 'main\Author.html')