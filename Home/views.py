from django.shortcuts import render
from django.http import HttpResponse



def index (request):
    return  render(request,'Home/index.html')


# def about (request):
#     owner = {

#         "name":"kushal",
#         "age":10,
#         "salary":50_000

#     }

#     general = {
#         "copyright":"2024",
#         "location":"Pokhara"
#     }

#     context = {
#         "owner":owner,
#         "general":general
#     }

#     return  render(request,'Home/about.html',context)



# def months (request):

#     months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

#     context = {
#         "months":months
#     }
    



#     return  render(request,'Home/months.html',context)






