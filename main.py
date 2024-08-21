import requests as rq
from typing import List
from google_play_scraper import app
from google_play_scraper import Sort, reviews_all

class ParseReviews:
    def __init__(self, links: List[str]):
        self.links = links

    def scrape(self):
        app_reviews = reviews_all(
            'de.flaschpost.app', # GOOGLE APPLCIATION ID FROM LINK!
            sleep_milliseconds=10,
            lang='de',
            country='de',
            sort=Sort.NEWEST
        )
        print(app_reviews)
    

def read_file(links_txt_path: str) -> List[str]:
    links_result: List[str] = []
    with open(links_txt_path, 'r') as file:
        for line in file.readlines():
            links_result.append(line.replace('\n', ''))
    return links_result




def main(links_txt_path: str) -> None: 
    k = read_file(links_txt_path)
    ParseReviews(k).scrape()

if __name__ == '__main__':
    main('./links.txt')
