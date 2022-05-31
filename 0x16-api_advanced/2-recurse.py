#!/usr/bin/python3
"""function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """function that queries the Reddit API and
    prints the titles of the first 10 hot posts listed for a given subreddit"""
    headers = {'User-Agent': 'nuwtts'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {
        'limits': 100,
        'after': after,
    }
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 404:
        return None

    results = res.json().get("data")
    after = results.get("after")

    for result in results.get("children"):
        hot_list.append(result.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
