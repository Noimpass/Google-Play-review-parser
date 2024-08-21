import pandas as pd

def to_excel(dict: Dict, path_to_file: str) -> int:
    df = pd.DataFrame(dict).T
    df.to_excel(path_to_file)


def _test():
    graph = {'A':{'A':0,'B':6,'C':INF,'D':6,'E':7},

         'B':{'A':INF,'B':0,'C':5,'D':INF,'E':INF},

         'C':{'A':INF,'B':INF,'C':0,'D':9,'E':3},

         'D':{'A':INF,'B':INF,'C':9,'D':0,'E':7},

         'E':{'A':INF,'B':4,'C':INF,'D':INF,'E':0}

         }
    to_excel(graph, 'file.xls')

if __name__ == '__main__':
    _test()
