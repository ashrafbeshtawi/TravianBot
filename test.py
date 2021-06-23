import func
import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime
session = requests.Session()
URL= "https://tx3.travian.com"
username="ashraf000"
password="smartart16"

func.login(session,URL,username,password)
x=func.get_buildings(session,URL)
print(x)

y=func.build_new(session,URL,30,x)
print(y)