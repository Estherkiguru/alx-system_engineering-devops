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

    params = {"after": after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data").get("after")

        if results is not None:
            after = results
            recurse(subreddit, hot_list)

        posts = results.json().get("data").get("children")

        for post in posts:
            hot_list.append(post.get("data").get("title"))

        return hot_list
    else:
        return None

