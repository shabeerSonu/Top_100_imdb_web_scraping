import csv
import requests
from bs4 import BeautifulSoup

# Change the url into any imdb Top 100 List
# Make sure the url https://www.imdb.com/list/<LIST_CODE>/ follows this format
# So you can get Top 100 list.csv file
url = "https://www.imdb.com/list/ls057577566/"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    anime_data = soup.select(".lister-item-header")
    rating_data = soup.select(".ipl-rating-star")
    anime_list = [anime.getText() for anime in anime_data]

    # change the name '100_Anime_List.csv' to whatever you want
    with open("100_Anime_List.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Year"])
        for anime in anime_list:
            anime_name = anime.split("\n")
            writer.writerow([f"{anime_name[2]}", f"{anime_name[3]}"])
else:
    print(f"{response.status_code}-Error!! Website not available.")
