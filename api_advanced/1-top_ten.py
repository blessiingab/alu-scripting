#!/usr/bin/python3
"""Fetches and prints the titles of the top 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Read Reddit API and print top 10 hot post titles of a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'holbertonschool-user-agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            for post in posts[:10]:
                print(post['data']['title'])
        else:
            print("None")
    except Exception:
        print("None")

