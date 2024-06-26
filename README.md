# My-Anime-GUI
Scraping My Anime List, Analyzing anime properties, Building a GUI to recommend animes to the ones you like
![eran](https://user-images.githubusercontent.com/94745919/232258116-71d27e54-aabd-40ac-910d-d344b6aa9184.jpg)
For the 2 persons who dont know what Anime is, Anime is a style of animation that originated in Japan. It encompasses a wide range of genres, from action and adventure to romance and comedy. The term "anime" is derived from the English word "animation," but it has come to refer specifically to Japanese animation.
</br>
Anime is known for its distinctive visual style, which often features large eyes, colorful hair, and exaggerated facial expressions. It also frequently employs themes and motifs from Japanese culture, such as samurai warriors, ninjas, and Shinto mythology.
</br>
One of the unique characteristics of anime is its ability to tell stories across multiple episodes or seasons, allowing for more complex narratives and character development than traditional films or television shows.
</br>
Today, anime has become popular around the world and has inspired countless fans and creators. It continues to evolve and push artistic boundaries, making it an exciting and dynamic medium for storytelling.
## Description
the goal of this project is to **analyze** and **make a recommendation system** that recommends animes based on anime features like(story,genre,etc)then put it in a GUI to make it easy to use 
</br>
### Collecting the data 
with the help of **My Anime List (MAL)** using selenium web driver, I scraped the following information:
</br>
* Titles
* Scores
* Popularity
* Ranked
* Members
* Platform
* Studio
* Episodes
* Aired
* Genres
* Themes
* Demographic
* Duration
* Rating
* Description(Synopsis)
* Related Anime
* Characters from Characters & Voice Actors
* Favorites
</br>

I used selenium to scrap from the **Top Ainmes List** to scrap 25 pages around(1250 anime) *because in my opinion animes after this are unwatchable and I dont care about*
</br>
I made the scarping code modifiable and responds to the user's input if you run the code it will ask you how many pages you want to scrap you can scrap less or more as you like and the like of the list you can replace it with the most popular,top aring,etc 
**Note** 
if it must be a link of a list to run smoothly without any problems)

![alt text](https://user-images.githubusercontent.com/94745919/232259708-19e05348-7785-4299-9d48-73b742379bb1.jpg)
</br>
### Data Analysis
The analysis is going to be about the first 1250 anime in the top animes
</br>
Around 85% of the top ranked animes are the **Not original** work and are **Alternative_version** and dont have one (Remaster)
![image](https://user-images.githubusercontent.com/94745919/232334713-a4850472-d52c-4659-aa11-7f0053157a9c.png)
</br>
80% of the animes have anime or movie side story of the anime(stories about some of sup caracters)
![image](https://user-images.githubusercontent.com/94745919/232335025-125769c8-a46b-4965-8c21-e2790b73e1cb.png)
</br>
Out of top ranked animes only 40% of the animes that have **series** and the rest are **stand alone** animes
(completed on one show)
![image](https://user-images.githubusercontent.com/94745919/232335037-3153c3ec-6f76-4222-ba70-22e59be6def8.png)
</br>
The **Shounen** demographic is taking the majority of the shows with around 60% and **Seinen** in the second place with 22.5%
![image](https://user-images.githubusercontent.com/94745919/232335076-868941fa-779f-4372-a0e9-dd0ed21b29fb.png)
</br>
A good story does not always mean good animes some studious ruin a good anime by bad drawings or changing the story 
</br>
these top 10 studious that have the biggest share of the top ranked animes means that have the highest quality of production and also the choice of good mangas to produce
![image](https://user-images.githubusercontent.com/94745919/232335633-58e17829-18c0-4e1a-af6a-baaa720b204f.png)
</br>
**Production I.G, Madhouse, and Sunrise** have **229** anime on the top ranked list and the top 10 have **655** out of **1250** more than a half !! huge Market monopoly
</br>
The members show how popular the anime is the most popular 2 by far are **attack on titen'1'** and **Death Note'2'** and the rest are close to each other
![image](https://user-images.githubusercontent.com/94745919/232336398-f4a05c50-0c38-4531-bbfd-a20c6ceaa819.png)
<br>
unexpectedly they are not the most Favorites as **Fullmetal '1'** and **HXH '2'** comes in the first 2 places as most favorites and the most popular ones come in the **Death Note '5'** and **Attack on titen'6'**
<br>
![Screenshot (500)](https://user-images.githubusercontent.com/94745919/232336508-98633c51-15d0-4130-a8e8-6d4b16e483eb.png)
<br>
The Action genre dominates 43% of the animes and Fantasy with 28% and less than 1% goes to Girls Love, Romance and Slice of life genres
![image](https://user-images.githubusercontent.com/94745919/232336551-761be6dd-ee14-406d-8892-ed1c21db84e3.png)
<br>
The most common anime themes you will find in the top animes are **School,Adult Cast,Psychological** and **Mysology**
![image](https://user-images.githubusercontent.com/94745919/232336822-8d97bb3c-1a27-48f2-aa5d-e217f8376d95.png)
<br>
over half of the production of the anime goes to **TV** as a main platform but we can not lose sight of **Movies** too in the second place but not as heavily as **TV**
<br>
![image](https://user-images.githubusercontent.com/94745919/232336879-00f89036-9c50-4124-b221-7692a2a05980.png)

and here comes the sad part forever anime lover and defender
<br>
the plot shows that the majority of the top animes ranting are for **Teens 13 or older** over (600 of 1000)
<br>
But there is a good production going to the **R rating(17+)**
![image](https://user-images.githubusercontent.com/94745919/232336943-9571e145-fe11-49f5-96a5-53ebca0cf494.png)
<br>
And to be honest, I watched a lot of the Teens 13 or older rating and I really enjoyed it wasn't bad at all
### GUI
![Screenshot (501)](https://user-images.githubusercontent.com/94745919/232339644-2330f123-cf19-4fd1-addb-14eb9f44eaf9.png)
<br>
let us walk through this GUI
<br>
this GUI has 5 buttons every one of them does a function:
<br>
#### Search
This button will return all the animes that start with the **name or laters** the user input
![Screenshot (502)](https://user-images.githubusercontent.com/94745919/232340055-e6d5ed87-69a8-4d1a-b178-af0130cdd551.png)
<br>
#### Recomendation By Story Like
This button will give a **Recommendation** for 15 anime depending on the user anime input by **story overview**
<br> 
**Note**
<br> 
as the search button you can enter the first letter of the anime and it will return the highest anime name that matches your input
![Screenshot (503)](https://user-images.githubusercontent.com/94745919/232340566-f6cf9dd9-5141-4a9e-831a-24eac07a2f36.png)
<br> 
#### Recomendation By Genres Like
This button will give a **Recommendation** for 15 anime depending on the user anime input by **Anime Genres**
<br> 
*Note: as the search button you can enter the first letter of the anime and it will return the highest anime name that matches your input*
![Screenshot (504)](https://user-images.githubusercontent.com/94745919/232341272-3963f848-f899-4b0f-846c-62d05548d8f7.png)

#### Recomendation By Themes Like
This button will give a **Recommendation** for 15 anime depending on the user anime input by **Anime Themes**
<br> 
*Note: as the search button you can enter the first letter of the anime and it will return the highest anime name that matches your input*
![Screenshot (505)](https://user-images.githubusercontent.com/94745919/232341333-6cda7e8f-88ad-4807-b82a-7ebb8dd9e7a5.png)

#### Get_Information
This button will give you all the information you need about the anime the user inputs like:
<br> 
*Themes,Genres,Series Name,Prequel,Sequel,Main Hero,Supporting Heroes,Supporters and alot more*
<br>
**Note** 
<br>
as the search button you can enter the first letter of the anime and it will return the highest anime name that matches your input
![Screenshot (506)](https://user-images.githubusercontent.com/94745919/232341401-7e8e4820-44b0-4327-8961-c04a026f50e1.png)
