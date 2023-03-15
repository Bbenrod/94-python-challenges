# Scraping GitHub Profile

import requests
from bs4 import BeautifulSoup as bs


def scrape_profile(name):
    github_profile = f"https://github.com/{name}"
    req = requests.get(github_profile)
    scraper = bs(req.content, "html.parser")
    try:
        profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
        print(f"PROFILE IMAGE URL:\t{profile_picture}")
    except:
        print(f"PROFILE ${name} NOT FOUND.")


if __name__ == "__main__":
    name = input("TYPE AN USER FROM GITHUB:\t")
    url = scrape_profile(name)
