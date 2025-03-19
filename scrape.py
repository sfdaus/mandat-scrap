import os
import tweepy
import pandas 
from dotenv import load_dotenv

#Load API Creds & Authentication
load_dotenv()
token = os.getenv("BEARER_TOKEN")
client = tweepy.Client(bearer_token=token, wait_on_rate_limit=True)

#Scrapping Mulai
query = "(RUU TNI OR revisi UU TNI OR tolak ruu tni) (trading halt OR IHSG turun OR saham turun OR ihsg anjlok) -is:retweet -has:media lang:id"

def scrapeTweets(query, maxRes):
    res = client.search_recent_tweets(query=query, max_results=maxRes, tweet_fields=["created_at", "text", "author_id", "public_metrics"])

    data = []
    if res.data:
        for tweet in res.data:
            data.append([
                tweet.created_at, tweet.author_id, tweet.text.replace("\n", " "),  
                tweet.public_metrics["retweet_count"],
                tweet.public_metrics["like_count"]
            ])

    df = pandas.DataFrame(data, columns=["created_at", "author_id", "text", "retweets", "likes"])
    df.to_csv("result-csv/scrape_data.csv", index=False, encoding="utf-8-sig")

if __name__ == "__main__":
    scrapeTweets(query, maxRes=10)