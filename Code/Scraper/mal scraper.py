from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd 
from tqdm import tqdm
import sys

# Setting the web driver 
url='https://myanimelist.net/topanime.php'
driver_path = "C:\\Program Files (x86)\\chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
driver  = webdriver.Chrome(executable_path=driver_path, chrome_options=option)


# Scraping the links from the ainme name link in the web page  
try:
    
    num_pages=int(input('how many pages do you want to scrap: '))
    def get_links(url):
        anime_links = []
        print(f'Geting Links Form {num_pages} Pages...')
        for page in tqdm(range(0,num_pages*50,50)):
            driver.get(url +'?limit='+ str(page))
            results = driver.find_element(By.CLASS_NAME, 'detail')
            animes = results.find_elements(By.XPATH, '//a[contains(@id, "area")]')

            for anime in animes:
               anime_links.append(anime.get_attribute("href"))
        
            anime_links = list(dict.fromkeys(anime_links))
        


            # #print('Got the following links:')
            # for link in anime_links:
            #     print(link)
        return anime_links




    # accessing each link and extract the information form the web page
    def scraping():
        Titles=[]
        Scores=[]
        Popularty=[]
        Rank=[]
        Paltform=[]
        Members=[]
        Studio=[]
        Ep_number=[]
        Themes=[]
        Genra=[] 
        Aired=[]
        Demographic=[]
        Duration=[] 
        Rating=[]
        Description=[]
        Caracters_Role=[]
        Relateds=[]
        Favorites=[]
        links = get_links(url)
        
        print('Scraping Begins...')
        for link in tqdm(links):
            driver.get(link)
            page_content=driver.find_element(By.XPATH,'//div[contains(@id, "contentWrapper")]')
            title=page_content.find_element(By.CSS_SELECTOR,'div[itemprop="name"] h1').text
            rigth_infos=page_content.find_element(By.CSS_SELECTOR,'div[class="stats-block po-r clearfix"]')
            score=rigth_infos.find_element(By.CSS_SELECTOR,'div[class="fl-l score"]').text
            pop=rigth_infos.find_element(By.CSS_SELECTOR,'span[class="numbers popularity"] strong').text
            rank=rigth_infos.find_element(By.CSS_SELECTOR,'span[class="numbers ranked"] strong').text
            member=rigth_infos.find_element(By.CSS_SELECTOR,'span[class="numbers members"] strong').text
            try:
                paltform=rigth_infos.find_element(By.CSS_SELECTOR,'span[class="information type"] a').text
        
            except Exception:
                paltform='unknown'
        
            try:
                studio=rigth_infos.find_element(By.CSS_SELECTOR,'span[class="information studio author"] a').text
        
            except Exception:
                studio='unknown'
                
        
            description=page_content.find_element(By.CSS_SELECTOR,'p[itemprop="description"]').text
           
            # getting the 'Related Anime' elements
            
            try:
                related = page_content.find_element(By.CSS_SELECTOR,'table[class="anime_detail_related_anime"]')
                related_type=[]
                related_ainme_name=[]

                for info in related.find_elements(By.TAG_NAME, 'tr'):
                    related_type.append(info.find_element(By.CSS_SELECTOR, 'td[class="ar fw-n borderClass"]').text)
                    related_ainme_name.append(info.find_element(By.CSS_SELECTOR, 'td[class="borderClass"] a').text)      
                
                #replace ":" with '__' in related_ainme_name and removeing ":" in related_type to make varables readable and accseable from the dictionary they will be put in   
                related_ainme_name = [name.replace(": ", "__") for name in related_ainme_name]
                related_type = [name.replace(":", "") for name in related_type]
                
            except Exception:
                relateds='no related animes'
             
            try:
                
                caracters=page_content.find_elements(By.CSS_SELECTOR,'div[class="detail-characters-list clearfix"]')
                caracters_discription=[]
                for caracter in caracters:
                    caracter_name=page_content.find_elements(By.CSS_SELECTOR,'div[class="detail-characters-list clearfix"] h3')
                    caracter_discription=caracter.find_elements(By.CSS_SELECTOR,'div[class="spaceit_pad"] small')
                    
                    
                    
                    for dis in caracter_discription:
                        dis.find_elements(By.CSS_SELECTOR,'div[class="spaceit_pad"]')
                        caracters_discription.append(dis.text)
                        
                    caracters_name=[]
                    for car in caracter_name :
                        car.find_elements(By.CSS_SELECTOR,'div[class="detail-characters-list clearfix"] h3')
                        caracters_name.append(car.text)
                    
                
            except Exception:
                caracters_discription.append("no carcater")
                caracters_name.append("no carcater")
            
            # the producer section have the as same class as caracters_discription and that is unwanted information to me so making the 2 lists equal will drop the producers info
            caracters_discription=caracters_discription[0:len(caracters_name)]
            
            #reformating the caracters names in the right order (website have the caracters name reversed)
            formatted_list = []
            for name in caracters_name:
                name_parts = name.split(", ")
                if len(name_parts) >= 2:
                    formatted_name = name_parts[1] + " " + name_parts[0]
                    formatted_list.append(formatted_name)

            #print(formatted_list)
            #print(caracters_name)
            caracters_name=formatted_list
        
           #getting the infos on the left side of the page
            left_side=page_content.find_element(By.XPATH,'//div[contains(@class, "leftside")]')
        
            infos=left_side.find_elements(By.XPATH,'div[contains(@class, "spaceit_pad")]')
        
        
            for info in infos:
                info=str(info.text).split(': ')
                
               
                info_category=info[0]
                info_content=info[1]
                    
                if info_category == 'Episodes':
                    if info_content == 'Unknown':
                        ep_number=0
                        
                    ep_number=str(info_content)
                
                elif info_category == 'Aired':
                    if info_content =='Not available':
                        aired='not yet aired'
                        
                    aired=str(info_content)
                    
                
        
                elif info_category == 'Rating':
                    
                    rating=str(info_content)
                    
                    
                
                elif info_category == 'Duration':
                    
                        duration=str(info_content)            
                
                elif info_category == 'Genres':
                    genra=[]
                    for i in info_content.split(', '):
                        genra.append(i)
                
                 
                elif info_category == 'Theme' or info_category == 'Themes':
                    themes=[]
                    for i in info_content.split(', '):
                        themes.append(i)
                    
                
                elif info_category == 'Demographic' :
                    demographic=[]
                    for i in info_content.split(', '):
                        demographic.append(i)
                
                elif info_category == 'Favorites' :
                    favorites=[]
                    for i in info_content.split(', '):
                        favorites.append(i)
                        
        
        
                
            #putting caracters_name and caracters_discription in a dictionary so they can be accessible 
            caracters_role=dict(zip(caracters_name,caracters_discription))
            
            # same as caracters_role for related_ainmes_to_this_sereis
            related_ainmes_to_this_sereis={}

            for i,j in zip(related_type,related_ainme_name):
                temp={}
                temp[i]=j
                related_ainmes_to_this_sereis.update(temp)
        

            Titles.append(title)
            Scores.append(score)
            Popularty.append(pop)
            Rank.append(rank)
            Members.append(member)
            Paltform.append(paltform)
            Studio.append(studio)
            Ep_number.append(ep_number)
            Aired.append(aired)
            Genra.append(genra)
            Themes.append(themes)
            Demographic.append(demographic)
            Duration.append(duration)
            Rating.append(rating)
            Description.append(description)
            Relateds.append(related_ainmes_to_this_sereis)
            Caracters_Role.append(caracters_role)
            Favorites.append(favorites)
        
        
            
        anime_score_dict = {
                'Name': Titles, 
                'Score' : Scores,
                'Score_Rank' : Rank,
                'Popularity_Rank' : Popularty,
                'Members':Members,
                'Favorites':Favorites,
                'Studio' : Studio,
                'episodes' : Ep_number,
                'Genres' : Genra,
                'Theme(s)' : Themes,
                'Demographic' : Demographic,
                'rating' : Rating,
                'duration' : Duration,
                'platform' : Paltform,
                'aired_time' : Aired,
                'overview' : Description,
                'related_animes': Relateds,
                'caracter_name' : Caracters_Role
            }
        anime_df = pd.DataFrame.from_dict(anime_score_dict)
        anime_df.to_csv('E:\\py\\scraping_mal\\mal.csv')
        print('Scraping Ends :) ')
        driver.close()
        
except ValueError:
    print('ENTER NUMBER NOT WORDS!!!')
    sys.exit()
    

scraping()