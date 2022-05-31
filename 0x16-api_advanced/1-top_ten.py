#!/usr/bin/python3
"""function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and
    prints the titles of the first 10 hot posts listed for a given subreddit"""
    headers = {'User-Agent': 'nuwtts'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    res = requests.get(url, headers=headers, params={'limit': 10})
    if res.status_code > 300:
        print("None")
        return
    results = res.json().get("data")
    for result in results.get("children"):
        print(result.get("data").get("title"))
