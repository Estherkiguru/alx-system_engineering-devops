#!/usr/bin/python3
"""
function that queries the Reddit API
-Returns the number of subscribers for a given subreddit.
-If an invalid subreddit is given, the function returns 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API to return no. of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
