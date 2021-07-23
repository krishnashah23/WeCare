from django.urls import path,include
from .views import getname,coronaDetails,selectoption,getoption,allcountrydata,allcountries
urlpatterns=[
    # path('getcoronaupdates/',getcoronaupdates),
    path('getname/',getname),
    path('coronaDetails/',coronaDetails),
    path('selectoption/',selectoption),
    path('getoption/',getoption),
    path('allcountrydata/',allcountrydata),
    path('allcountries/',allcountries)
]