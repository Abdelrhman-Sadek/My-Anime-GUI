import pandas as pd 
import warnings
warnings.simplefilter("ignore")
import re
from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
import customtkinter as ctk
#from PIL import Image, ImageTk


df=pd.read_csv('E:\\py\\scraping_mal\\cleaned_data.csv')
del df['Unnamed: 0']

#replace all the nulls with readable text 
subset = df.loc[:, ~df.columns.isin(['platform', 'rating','Demographic'])]
subset.fillna('Unavailable or not provided information by MAL', inplace=True)
df.update(subset)

#Building GUI functions
def search():
    input_value = anime_name.get()

    pattern = re.compile(f'{input_value}', re.IGNORECASE)
    matches = [x for x in df['Name'] if pattern.match(x)]
    name_display.configure(text=f'Ainmes that starts with {input_value}')
    output_text=""
    if len(matches) > 0:
        for i in range(len(matches)):
            print("-" + matches[i])
            output_text += f"- {matches[i]}\n"
            output.delete("1.0",'end')
            output.insert('end', output_text)
            output_kind.configure(text='Search')
    else:
        print('Cant Identify Any Ainme (try enter it frist litters or frist word)')
        output.delete("1.0",'end')
        output.insert('end','Cant Identify Any Ainme (try enter it frist litters or frist word)')
        name_display.configure(text='Unknown Anime')
        output_kind.configure(text='Search')
    print('\n \n')       
    
    
stop_words = set(stopwords.words('english'))

ps = PorterStemmer()
df['preprocessed_overview'] = df['overview'].apply(lambda x: ' '.join([ps.stem(word.lower()) for word in word_tokenize(x) if word.isalpha() and word not in stop_words]))  
df['preporcessed_genres']=df['Genres'].apply(lambda x: ' '.join([ps.stem(word.lower()) for word in word_tokenize(x) if word.isalpha() and word not in stop_words]))
df['preporcessed_theme']=df['Theme(s)'].apply(lambda x: ' '.join([ps.stem(word.lower()) for word in word_tokenize(x) if word.isalpha() and word not in stop_words]))   
    
def recommendation_based_on_overview():
    try:
        tfidf_vectorizer = TfidfVectorizer()
        vectorized_overview = tfidf_vectorizer.fit_transform(df['preprocessed_overview'])
        
        #Make the anime name get the highest matche to the usesr input
        anime_name = anime_name_var.get()
        pattern = re.compile(f'{anime_name}', re.IGNORECASE)
        matches = df.loc[df['Name'].str.contains(pattern, na=False), 'Name']
        
        if len(matches) == 0:
            print('No Anime with this name found. Please try entering the first few letters or the first word of the anime title.')
        else:
            anime_name = sorted(matches, key=lambda x: len(x))[0]
            #Get the overview from the name 
            anime_matches = df.loc[df['Name'] == anime_name, 'overview'].iloc[0]
        
        #anime_name=df.loc[matches, 'Name'].iloc[0]
        name_display.configure(text=f'{anime_name}')
        

        # Check if the input value contains any digits or not
        
        
        # Vectorize the input value
        name_vector = tfidf_vectorizer.transform([anime_matches])

        # Calculate the cosine similarity between the input value and all the anime titles
        similarity_scores = list(cosine_similarity(name_vector, vectorized_overview)[0])

        # Get the indices and names of top 10 similar anime titles
        top_10_anime_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:15]
        recommendations = df[['Name','Score', 'overview']].iloc[top_10_anime_indices]
        #recommendations_sorted = recommendations.sort_values('Score', ascending=False)

        # Print the recommended anime titles
        print(f"Recommended Animes for {anime_name}")
        output_text=""
        for index, anime in recommendations.iterrows():
            print("- " + anime['Name'] + " (Score: " + str(round(anime['Score'], 2)) + ")")
            output_text += f"- {anime['Name']} (Score:{str(round(anime['Score'], 2))})\n"
        output.delete("1.0",'end')
        output.insert('end', output_text)
        output_kind.configure(text='Recommendation By Story Like')
        print('\n \n')
    except Exception:
        print('No Anime With This Name In The Data (try enter it frist litters or frist word) ')
        output.delete("1.0",'end')
        output.insert('end','Cant Identify Any Ainme (try enter it frist litters or frist word)')
        name_display.configure(text='Unknown Anime')
        output_kind.configure(text='Recommendation By Story Like')
        print('\n \n')
    

def recommendation_based_on_genre():
    try:
        tfidf_vectorizer = TfidfVectorizer()
        vectorized_genre = tfidf_vectorizer.fit_transform(df['preporcessed_genres'])
        
        #Make the anime name get the highest matche to the usesr input
        anime_name = anime_name_var.get()
        pattern = re.compile(f'{anime_name}', re.IGNORECASE)
        matches = df.loc[df['Name'].str.contains(pattern, na=False), 'Name']
        
        
        if len(matches) == 0:
            print('No Anime with this name found. Please try entering the first few letters or the first word of the anime title.')
        else:
            anime_name = sorted(matches, key=lambda x: len(x))[0]
            #Get the Genres from the name
            anime_matches = df.loc[df['Name'] == anime_name, 'Genres'].iloc[0]
        
        name_display.configure(text=f'{anime_name}')

        # Vectorize the input value
        name_vector = tfidf_vectorizer.transform([anime_matches])

        # Calculate the cosine similarity between the input value and all the anime titles
        similarity_scores = list(cosine_similarity(name_vector, vectorized_genre)[0])

        # Get the indices and names of top 10 similar anime titles
        top_10_anime_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:15]
        recommendations = df[['Name','Score', 'Genres']].iloc[top_10_anime_indices]
        #recommendations_sorted = recommendations.sort_values('Score', ascending=False)

        # Print the recommended anime titles
        print(f"Recommended Animes for {anime_name}")
        output_text=""
        for index, anime in recommendations.iterrows():
            print("- " + anime['Name'] + " (Score: " + str(round(anime['Score'], 2)) + ")")
            output_text += f"- {anime['Name']} (Score:{str(round(anime['Score'], 2))})\n"
        output.delete("1.0",'end')
        output.insert('end', output_text)
        output_kind.configure(text='Recommendation By Genres')
        print('\n \n')
    except Exception:
            print('No Anime With This Name In The Data (try enter it frist litters or frist word) ')
            output.delete("1.0",'end')
            output.insert('end','Cant Identify Any Ainme (try enter it frist litters or frist word)')
            name_display.configure(text='Unknown Anime')
            output_kind.configure(text='Recommendation By Genres')
            print('\n \n')

def recommendation_based_on_themes():
    try:
        tfidf_vectorizer = TfidfVectorizer()
        vectorized_themes = tfidf_vectorizer.fit_transform(df['preporcessed_theme'])
        
        #Make the anime name get the highest matche to the usesr input
        anime_name = anime_name_var.get()
        pattern = re.compile(f'{anime_name}', re.IGNORECASE)
        matches = df.loc[df['Name'].str.contains(pattern, na=False), 'Name']
        
        #Get the Genres from the name 
        if len(matches) == 0:
            print('No Anime with this name found. Please try entering the first few letters or the first word of the anime title.')
        else:
            anime_name = sorted(matches, key=lambda x: len(x))[0]
            #Get the Themes from the name 
            anime_matches = df.loc[df['Name'] == anime_name, 'Theme(s)'].iloc[0]
        
        name_display.configure(text=f'{anime_name}')
        # Vectorize the input value
        name_vector = tfidf_vectorizer.transform([anime_matches])

            # Calculate the cosine similarity between the input value and all the anime titles
        similarity_scores = list(cosine_similarity(name_vector, vectorized_themes)[0])

            # Get the indices and names of top 10 similar anime titles
        top_10_anime_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:15]
        recommendations = df[['Name','Score', 'Theme(s)']].iloc[top_10_anime_indices]
        #recommendations_sorted = recommendations.sort_values('Score', ascending=False)

        # Print the recommended anime titles
        print(f"Recommended Animes for {anime_name}")
        output_text=""
        for index, anime in recommendations.iterrows():
            print("- " + anime['Name'] + " (Score: " + str(round(anime['Score'], 2)) + ")")
            output_text += f"- {anime['Name']} (Score:{str(round(anime['Score'], 2))})\n"
        output.delete("1.0",'end')
        output.insert('end', output_text)
        output_kind.configure(text='Recommendation By Themes')
        print('\n \n')
    except Exception:
            print('No Anime With This Name In The Data (try enter it frist litters or frist word) ')
            output.delete("1.0",'end')
            output.insert('end','Cant Identify Any Ainme (try enter it frist litters or frist word)')
            name_display.configure(text='Unknown Anime')
            output_kind.configure(text='Recommendation By Themes')
            print('\n \n')
    
    
def get_information():
    try:
        anime_name = anime_name_var.get()
        pattern = re.compile(f'{anime_name}', re.IGNORECASE)
        matches = df.loc[df['Name'].str.contains(pattern, na=False), 'Name']
        
        anime_name = sorted(matches, key=lambda x: len(x))[0]
        #anime_name=df.loc[matches, 'Name'].iloc[0]
        name_display.configure(text=f'{anime_name}')
        
        anime_themes=df.loc[df['Name'] == anime_name, 'Theme(s)'].iloc[0]
        anime_genre=df.loc[df['Name'] == anime_name, 'Genres'].iloc[0]
        anime_studio=df.loc[df['Name'] == anime_name, 'Studio'].iloc[0]
        anime_score=df.loc[df['Name'] == anime_name, 'Score'].iloc[0]
        anime_episodes=df.loc[df['Name'] == anime_name, 'episodes'].iloc[0]
        ainme_duration=df.loc[df['Name'] == anime_name, 'duration'].iloc[0]
        anime_demographic=df.loc[df['Name'] == anime_name, 'Demographic'].iloc[0]
        anime_rating=df.loc[df['Name'] == anime_name, 'rating'].iloc[0]
        anime_platform=df.loc[df['Name'] == anime_name, 'platform'].iloc[0]
        anime_overview=df.loc[df['Name'] == anime_name, 'overview'].iloc[0]
        
        anime_hero=df.loc[df['Name'] == anime_name, 'hero'].iloc[0]
        anime_sup_heros=df.loc[df['Name'] == anime_name, 'sup_heros'].iloc[0]
        anime_supporters=df.loc[df['Name'] == anime_name, 'supporters'].iloc[0]
        anime_series_name=df.loc[df['Name'] == anime_name, 'Adaptation'].iloc[0]
        anime_Side_story=df.loc[df['Name'] == anime_name, 'Side_story'].iloc[0]
        anime_Alternative_version=df.loc[df['Name'] == anime_name, 'Alternative_version'].iloc[0]
        anime_Prequel=df.loc[df['Name'] == anime_name, 'Prequel'].iloc[0]
        anime_Sequel=df.loc[df['Name'] == anime_name, 'Sequel'].iloc[0]
        
        print(f"Anime Name: {anime_name}")
        print(f"\nOverview: {anime_overview}")
        print(f"\nThemes: {anime_themes}")
        print(f"Genres: {anime_genre}")
        print(f"Studio: {anime_studio}")
        print(f"Score: {anime_score}")
        print(f"Episodes: {anime_episodes}")
        print(f"Duration: {ainme_duration}")
        print(f"Demographic: {anime_demographic}")
        print(f"Rating: {anime_rating}")
        print(f"Platform: {anime_platform}")
        print("\nCharacters:")
        print(f"- Main Hero: {anime_hero}")
        print(f"- Supporting Heroes: {anime_sup_heros}")
        print(f"- Supporters: {anime_supporters}")
        print("\nAdaptations:")
        print(f"- Series Name: {anime_series_name}")
        print(f"- Prequel: {anime_Prequel}")
        print(f"- Side Story: {anime_Side_story}")
        print(f"- Alternative Version: {anime_Alternative_version}")
        print(f"- Sequel: {anime_Sequel}")
        print('\n \n')
        
        #Display on GUI
        
        output_text = f"Anime Name: {anime_name}\n\n"
        output_text += f"Overview: {anime_overview}\n\n"
        output_text += f"Themes: {anime_themes}\n"
        output_text += f"Genres: {anime_genre}\n"
        output_text += f"Studio: {anime_studio}\n"
        output_text += f"Score: {anime_score}\n"
        output_text += f"Episodes: {anime_episodes}\n"
        output_text += f"Durantion: {ainme_duration}\n"
        output_text += f"Demographic: {anime_demographic}\n"
        output_text += f"Rating: {anime_rating}\n"
        output_text += f"Platform: {anime_platform}\n\n"
        output_text += "Characters:\n"
        output_text += f"- Main Hero: {anime_hero}\n"
        output_text += f"- Supporting Heroes: {anime_sup_heros}\n"
        output_text += f"- Supporters: {anime_supporters}\n\n"
        output_text += "Adaptations:\n"
        output_text += f"- Series Name: {anime_series_name}\n"
        output_text += f"- Prequel: {anime_Prequel}\n"
        output_text += f"- Sequel: {anime_Sequel}\n"
        output_text += f"- Side Story: {anime_Side_story}\n"
        output_text += f"- Alternative Version: {anime_Alternative_version}\n"
        output.delete("1.0",'end')
        output.insert('end', output_text,'bold')
        output_kind.configure(text='Informations')
    except Exception:
        print('Cant Identify This Ainme (try enter it frist litters or frist word)')
        output.delete("1.0",'end')
        output.insert('end','Cant Identify This Ainme (try enter it frist litters or frist word)')
        name_display.configure(text='Unknown Anime')
        output_kind.configure(text='Informations')
        print('\n \n')

#################################GUI########################################

# system settings 
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')
# app frame
app=ctk.CTk()
app.geometry('1080x720')
app.title('My Anime Guide')


title = ctk.CTkLabel(app, text='Welcome to My Anime Guide (MAG)', font=('Arial', 20, 'bold'), text_color='#ADD8E6')
title.pack(padx=10,pady=10)

name_display=ctk.CTkLabel(app, text='Enter Ainme Name', font=('Arial', 15, 'bold'))
name_display.pack(padx=10,pady=10)

anime_name_var=tk.StringVar()

anime_name=ctk.CTkEntry(app,width=350,height=20,textvariable=anime_name_var)

anime_name.pack()


# add Buttons 
search=ctk.CTkButton(app,text='Search',command=search)
search.pack(padx=0,pady=10)

story=ctk.CTkButton(app,text='Recomendation By Story Like',command=recommendation_based_on_overview)
story.pack(padx=10,pady=10)

genres=ctk.CTkButton(app,text='Recomendation By Genres Like',command=recommendation_based_on_genre)
genres.pack(padx=10,pady=10)

themes=ctk.CTkButton(app,text='Recomendation By Themes Like',command=recommendation_based_on_themes)
themes.pack(padx=10,pady=10)

get_Information=ctk.CTkButton(app,text='Get_Information',command=get_information)
get_Information.pack(padx=10,pady=10)



#output lable
output_kind=ctk.CTkLabel(app, text='', font=('Arial', 15, 'bold'))
output_kind.pack()

output = ctk.CTkTextbox(app, height=200, width=700, wrap="word")
output.pack(padx=10, pady=10)

app.mainloop()


    
    
    
    
    
    
    
    
    