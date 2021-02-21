 
import html
from siteActualitees import siteActualitees
class clicanoo(siteActualitees):
    result=""
    def __init__(self):
        super().__init__("https://www.clicanoo.re")
        #self.__url=super().url

    def setup(self):
        r= super().request.get(self.url)
        main_title=r.text[r.text.index("<h1 class='in-field-body-title-large'>"):r.text.index("</h1>")]  #un seul h1 est présent dans la page
        text_buffer=r.text.replace(main_title,"")
        main_title=main_title[main_title.index("a href="):main_title.index("</a>")]
        main_title=main_title[(main_title.index(">")+1):len(main_title)]
        self.result=text_buffer
        
        title1=text_buffer[text_buffer.index("<h3 class='in-field-body-title-medium'>"):text_buffer.index("</a></h3>")] 
        #print("titre 1 :"+title1)
        text_buffer=text_buffer.replace(title1+"</a></h3>","")
        title1=title1[title1.index("a href="):len(title1)]
        title1=title1[(title1.index(">")+1):len(title1)]

        title2=text_buffer[text_buffer.index("<h3 class='in-field-body-title-medium'>"):text_buffer.index("</a></h3>")]  
        #print("titre 2 :"+title2)
        text_buffer=text_buffer.replace(title2+"</a></h3>","")
        title2=title2[title2.index("a href="):len(title2)]
        title2=title2[(title2.index(">")+1):len(title2)]

        title3=text_buffer[text_buffer.index("<h3 class='in-field-body-title-medium'>"):text_buffer.index("</a></h3>")]  
        #print("titre 3 :"+title3)
        text_buffer=text_buffer.replace(title3+"</a></h3>","")
        title3=title3[title3.index("a href="):len(title3)]
        title3=title3[(title3.index(">")+1):len(title3)]

        title4=text_buffer[text_buffer.index("<h3 class='in-field-body-title-medium'>"):text_buffer.index("</a></h3>")]  
        #print("titre 3 :"+title4)
        text_buffer=text_buffer.replace(title4+"</a></h3>","")
        title4=title4[title4.index("a href="):len(title4)]
        title4=title4[(title4.index(">")+1):len(title4)]

        title5=text_buffer[text_buffer.index("<h3 class='in-field-body-title-medium'>"):text_buffer.index("</a></h3>")]  
        #print("titre 3 :"+title3)
        text_buffer=text_buffer.replace(title5+"</a></h3>","")
        title5=title5[title5.index("a href="):len(title5)]
        title5=title5[(title5.index(">")+1):len(title5)]

        title6=text_buffer[text_buffer.index("<h3 class='in-field-body-title-medium'>"):text_buffer.index("</a></h3>")]  
        #print("titre 3 :"+title5)
        text_buffer=text_buffer.replace(title6+"</a></h3>","")
        title6=title6[title6.index("a href="):len(title6)]
        title6=title6[(title6.index(">")+1):len(title6)]

        self.titles.insert(1,html.unescape(title1))
        self.titles.insert(2,html.unescape(title2 ))
        self.titles.insert(3,html.unescape(title3 ))
        self.titles.insert(4,html.unescape(title4 ))
        self.titles.insert(5,html.unescape(title5 ))
        self.titles.insert(6,html.unescape(title6 ))