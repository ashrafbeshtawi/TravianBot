import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime

def login(session,url,username,password):
    page = session.get(url)
    page = BeautifulSoup(page.content, 'html.parser')
    if page.find(type="text")!= None and page.find(type="password")!= None :
        page.find(type="text")["value"]=username
        page.find(type="password")["value"]=password
        ##data
        data={"name":username,"password":password}
        result=session.post(url+"/login.php",data)
        print("logged in",result)
        return True
    return False
        
## get a list of all possible buildings
def get_buildings(session,url):
    buildings=[]
    build_page=url+"/build.php?id="
    #check every building :)
    for i in range(19,41):
        temp_page=build_page+str(i)
        page = session.get(temp_page)
        page = BeautifulSoup(page.content, 'html.parser')
        x=page.find(class_="titleInHeader")
        #if the name of the building foung
        if(x!=None):
            #if it is not empty place add it to the list
            if(x.find("span")!=None):
                x.find("span").decompose()
                buildings.append(x.getText().replace(" ",""))
    return buildings

## build new building with no duplicates
def build_new(session,url,id,building_list):
    for i in range(1,4):
        print(i)
        page = session.get(url+"/build.php?id="+str(id)+"&category="+str(i))
        page = BeautifulSoup(page.content, 'html.parser')
        ## check if new building possible     
        if(page.find(class_="buildingWrapper")!= None):
            print("possible")
            alle=page.find_all(class_="buildingWrapper")
            for item in alle:
                title=item.find("h2").getText()

                if(title!=None and  not (title.replace(" ","") in building_list) and item.find(class_="textButtonV1 green new")!=None):
                    link="/"+item.find(class_="textButtonV1 green new")["onclick"].replace("window.location.href = '","").replace("'; return false;","")
                    session.get(url+link)
            return url+": "+"new building id:"+str(id)+"\n"
    return ""


## upgrade building 
def build_upgrade(session,url,id):
    page = session.get(url+"/build.php?id="+str(id))
    page = BeautifulSoup(page.content, 'html.parser')
    if(page.find(class_="textButtonV1 green build")):
        link="/"+page.find(class_="textButtonV1 green build")["onclick"].replace("window.location.href = '","").replace("'; return false;","")
        session.get(url+link)
        print("upgrade building")
        return url+": "+"upgrade building id:"+str(id)+"\n"
    return ""
