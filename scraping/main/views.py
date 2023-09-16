from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import requests
from .models import Details 
# Create your views here.

def main(request):
    city = ['Mumbai','Lucknow','Agra','Ahmedabad','Kolkata','Jaipur','Chennai','Bengaluru','Pune','Delhi']
    for j in city:
        try:    
            url = f'https://www.99acres.com/search/property/buy/{j}?keyword={j}e&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N'
            headers = {'User-Agent':'Mozilla/5.0 (X11;Linux x88_64; rv:995.0) Gecko/20200101 Firefox/95.0'}
            r = requests.get(url,headers=headers)
            soup = BeautifulSoup(r.content,'html.parser')
            a = soup.find_all(class_ = 'srpTuple__cardWrap tupleCardWrap')
            for i in a:
                b = i.find(class_ = 'srpTuple__tupleTitleOverflow').text
                c = i.find(class_ = 'srpTuple__dFlex')
                e = i.find(id = 'srp_tuple_price').text
                g = i.find(id = 'srp_tuple_primary_area').text
                link = 'https://www.99acres.com'+c['href']
                data = Details(property_name = c.text,
                            property_cost = e,
                            property_type = b,
                            property_area = g ,
                            property_link = link,
                            city = j)
                data.save()
        except:
            continue        
        return HttpResponse('hello') 