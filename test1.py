from google_play_scraper import Sort, reviews
import pandas as pd
from datetime import datetime
from tqdm import tqdm
import time

# Fetch reviews using google_play_scraper, Replace with ur app-id!
app_id = 'com.whatsapp'

# Fetch reviews
result = []
continuation_token = None
reviews_count = 25000  # change count here

with tqdm(total=reviews_count, position=0, leave=True) as pbar:
    while len(result) < reviews_count:
        new_result, continuation_token = reviews(
            app_id,
            continuation_token=continuation_token,
            lang='ru',
            country='ru',
            sort=Sort.NEWEST,
            filter_score_with=None,
            count=150
        )
        if not new_result:
            break
        result.extend(new_result)
        pbar.update(len(new_result))

# Create a DataFrame from the reviews & Download the file
df = pd.DataFrame(result)

today = str(datetime.now().strftime("%m-%d-%Y_%H%M%S"))
df.to_csv(f'reviews-{app_id}_{today}.csv', index=False)
print(len(df))
files.download(f'reviews-{app_id}_{today}.csv')