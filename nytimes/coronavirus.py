import datetime as dt
from nytimes_scraper import run_scraper, scrape_month

# scrape february of 2020
article_df, comment_df = scrape_month('puNQh1sGyqYhSQo1hNzmqaT9RA7EOFGq', date=dt.date(2020, 2, 1))

article_df.to_csv("articles")
comment_df("comments")

# scrape all articles month by month
#run_scraper('puNQh1sGyqYhSQo1hNzmqaT9RA7EOFGq')