import requests as rq
from time import sleep
from typing import List
from google_play_scraper import app
from google_play_scraper import Sort, reviews_all, reviews
import time
import pandas as pd

class ParseReviews:
    def __init__(self, links: List[str]):
        self.links = links

    def scrape(self):
        for link in self.links:
            name = link.split("=")[1]
            info = app(
                name,
                lang='ru', # defaults to 'en'
                country='ru', # defaults to 'us'
            )
            reviews_count = info["reviews"]
            title = info["title"]
            print(f"parsing {title}")
            for i in range(1,6):
                result = []
                new_result = None
                continuation_token = None
                while len(result) < reviews_count:
                    new_result, continuation_token = reviews(
                    name,
                    continuation_token=continuation_token,
                    lang='ru', # defaults to 'en'
                    country='ru', # defaults to 'us'
                    count=25000,
                    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
                    filter_score_with=i # defaults to None(means all score)
                    )
                    result.extend(new_result)
                    print(f"review collected for {title} with score {i} - ",len(result))
                    if not new_result:
                        to_excel(result, info["title"], i)
                        print("done")
                        break
                print("TOTAL REVIEW ==",len(result))
                time.sleep(30)
                    

def to_excel(result, title, score):
    print(f"\ncreating excel file for {title}-{score}")
    try:
        df_existing = pd.read_excel(f'{title}-{score}.xlsx')
        df_new = pd.DataFrame({"Author": [x["userName"] for x in result],
                            "Rating": [x["score"] for x in result],
                            "Date": [x["at"] for x in result], 
                            "Text": [x["content"] for x in result],
                            "Thumbup": [x["thumbsUpCount"] for x in result],
                            "Reply": [x["replyContent"] for x in result],
                            "ReplyDate": [x["repliedAt"] for x in result]
                            })
        df_combined = pd.concat([df_existing, df_new], ignore_index=False)
        df_existing = None
        df_new = None
        df_combined.to_excel(f'{title}-{score}.xlsx', index=False)
        df_combined = None
        print("\n excel file created")
    except:
        df = pd.DataFrame({"Author": [x["userName"] for x in result],
                            "Rating": [x["score"] for x in result],
                            "Date": [x["at"] for x in result], 
                            "Text": [x["content"] for x in result],
                            "Thumbup": [x["thumbsUpCount"] for x in result],
                            "Reply": [x["replyContent"] for x in result],
                            "ReplyDate": [x["repliedAt"] for x in result]
                            })
        df.to_excel(f'{title}-{score}.xlsx', index=False)
        df=None
        print("\n excel file created")


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
