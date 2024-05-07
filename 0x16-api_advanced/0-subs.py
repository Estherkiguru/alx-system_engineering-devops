#!/usr/bin/python3
"""
function that queries the Reddit API returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    print(number_of_subscribers(subreddit))

