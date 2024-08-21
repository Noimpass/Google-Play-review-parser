import requests as rq
from typing import List

class ParseReviews:
    def __init__(self, links: List[str]):
        self.links = links

    def _reconfigure_links(self):
        for i in self.links:
            
    

def read_file(links_txt_path: str) -> List[str]:
    links_result: List[str] = []
    with open(links_txt_path, 'r') as file:
        for line in file.readlines():
            links_result.append(line.replace('\n', ''))
    return links_result




def main(links_txt_path: str) -> None: 
    print(read_file(links_txt_path))


if __name__ == '__main__':
    main('./links.txt')
