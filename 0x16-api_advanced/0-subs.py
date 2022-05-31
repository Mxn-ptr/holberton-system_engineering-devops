#!/usr/bin/python3
"""Function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and
    returns the number of subscribers"""
    headers = {'User-Agent': 'nuwtts'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    res = requests.get(url, headers=headers)
    if res.status_code > 300:
        return 0

    return res.json().get("data").get("subscribers")
