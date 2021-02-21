from datetime import datetime
import requests
class siteActualitees:
    titles=[]
    date_creation_info=""
    url="valeur initiale"
    request=requests
     
    def __init__(self,url):
        self.url=url
        self.request=requests.get(url)
        self.__date_creation_info = datetime.now()
    
 
         