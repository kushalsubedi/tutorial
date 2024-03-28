from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    return  HttpResponse("Hello World")

def about (request):
    return  HttpResponse("""
                         
                         <style>
                         span {
                         color: red;
                         }
                         
                          </style>
                         <h1> Task for you </h1> 

                            <p> 1. Create 2 <span> new app <span> </p>
                            <p> create urls.py in both app </p>
                            <p> create some views in both app  and make sure they were access in web</p>   
                         
                         
                         """)

