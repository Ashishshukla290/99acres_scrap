#from django.db import models
# Create your models here.
from mongoengine import Document,StringField,URLField,connect
connect('database')
class Details(Document):
    property_name = StringField(max_length=300)
    property_cost = StringField(max_length=50)
    property_type = StringField(max_length=300)
    property_area = StringField(max_length=50)
    property_link = URLField(max_length=300)
    city = StringField(max_length=50)