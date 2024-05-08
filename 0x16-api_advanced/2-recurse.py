#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
Returns list containing titles of hot articles for given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Retrieves list of title of hot articles on given reddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Custom User-Agent"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    posts = results.get("children")

    for post in posts:
        hot_list.append(post.get("data").get("title"))

    after = results.get("after")

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
