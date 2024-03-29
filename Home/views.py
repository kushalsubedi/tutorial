from django.shortcuts import render
from django.http import HttpResponse



def index (request):
    return  render(request,'Home/index.html')


def about (request):
    owner = {

        "name":"kushal",
        "age":24,
        "salary":50_000

    }

    general = {
        "copyright":"2024",
        "location":"Pokhara"
    }

    context = {
        "owner":owner,
        "general":general
    }

    return  render(request,'Home/about.html',context)


def Months(request):
    

    janauary = {
        "name":"jan",
        "days":31,
        "season":"winter"
    }

    April = {
        "name":"apr",
        "days":28,
        "season":"summer"
    }

    march = {
        "name":"mar",
        "days":31,
        "season":"spring"
    }




    context = {
        "jan":janauary,
        "apr":April,
        "mar":march
    }


    return  render(request,'Home/months.html',context)




