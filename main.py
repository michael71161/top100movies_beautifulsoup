# we want to scrap site with 100 best movies list 
# we will get the movies from raiting 100 till 1 
# we need to reverse the scraped list of movie titles and save it to .txt document 





import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"



response = requests.get(URL)
website_html = response.text # response/text will give raw .html file with original tags 

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title") #will give a list of all h3 tags from title class

movie_titles = [movie.getText() for movie in all_movies] # list comperhansion- creating a new list from the old one, getting texty of each tag 
movies = movie_titles[::-1]  # to reverse the list, before : from 100 to 1, now: from 1 to 100 

with open("movies.txt", mode="w") as file:   #create and write to movies.txt, we will get each item in new line from 1 to 100 :)) 
    for movie in movies:
        file.write(f"{movie}\n")


'''
The URLs ,tags and classes name can change very frequently on a live site 
We need to inpect the site using chrome dev tools like inspect to see the -
- correct tags name to know what we sholud look for in the site 
 

'''