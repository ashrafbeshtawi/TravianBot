import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime
import func

health_for_adv=50
session = requests.Session()
URLs=['https://ts1.arabics.travian.com',"https://tx3.travian.com"]
Username=["beshtawi","beshtawi"]
Password=["smartart16","smartart16"]


Log_text=""

for j in range(len(URLs)):
    URL= URLs[j]
    username=Username[j]
    password=Password[j]
    print("check: "+URL)

    #log in 
    func.login(session,URL,username,password)


    ###### try to build
    build_page=URL+"/build.php?id="
    for i in range(50):
        num=random.randint(1, 40)
        temp_page=build_page+str(num)+"&category="


        for k in range(1,4):
            temp_page_x=temp_page+str(k)
            page = session.get(temp_page_x)
            page = BeautifulSoup(page.content, 'html.parser')

            ## check if upgrading possible
            if(page.find(class_="textButtonV1 green build")):
                link="/"+page.find(class_="textButtonV1 green build")["onclick"].replace("window.location.href = '","").replace("'; return false;","")
                session.get(URL+link)
                print("upgrade building ")
                Log_text=Log_text+URL+": "+"upgrade building id:"+str(num)+"\n"

            ## check if new building possible     
            if(page.find(class_="textButtonV1 green new")):
                link="/"+page.find(class_="textButtonV1 green new")["onclick"].replace("window.location.href = '","").replace("'; return false;","")
                session.get(URL+link)
                print("new building")
                Log_text=Log_text+URL+": "+"new building id:"+str(num)+"\n"
    
    ##adventure
    page = session.get(URL+"/hero.php?t=1")
    page = BeautifulSoup(page.content, 'html.parser')
    ##get health bar
    if page.find(class_="attribute health tooltip")!=None:
        temp=page.find(class_="attribute health tooltip")
        bar=int(temp.find(class_="bar")["style"].replace("width:","").replace("%;",""))
        # if enough health then go on adventure
        if(bar>=health_for_adv):
                page = session.get(URL+"/hero.php?t=3")
                page = BeautifulSoup(page.content, 'html.parser')
                if page.find(class_="adventureSendButton")!=None:
                    link=page.find(class_="adventureSendButton")["action"]

                    page = session.post(URL+link,{"action":"sendHeroToAdventure"})
                    print("new adventure")
                    Log_text=Log_text+URL+": "+"new adventure \n"


    else:
        print("not found")

session.close()


### LOG
import os
os.chdir('C:\\Users\\user\\Desktop\\Bot')
f= open("log.txt","a+")
f.write(str(datetime.now())+"\n")
f.write(Log_text)
###