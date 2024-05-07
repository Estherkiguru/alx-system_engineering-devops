#!/usr/bin/python3
"""
function that queries the Reddit API 
Prints the titles of the first 10 hot posts
"""
import requests
from sys import argv

def top_ten(subreddit):
    """
    returns first 10 hot posts for a given subreddit
    """
    headers = { "User-Agent": "Esther"}

    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
            .format(subreddit), headers=headers, allow_redirects=False)
    try:
        for post in url.get("data").get("children"):
            print(post.get("data").get("title"))
    except Exception:
        print(None)



if __name__ == "__main__":
     top_ten(argv[1])
