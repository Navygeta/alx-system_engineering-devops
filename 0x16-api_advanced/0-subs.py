#!/usr/bin/python3
"""
Queries the Reddit API to retrieve the total number of subscribers for
a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the total number of subscribers for a specified subreddit.

    :param subreddit: The name of the subreddit.
    :return: The total number of subscribers or 0 if the subreddit is invalid.
    """
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    request_headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(api_url, headers=request_headers,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers_count = data.get('data', {}).get('subscribers', 0)
            return subscribers_count
    except requests.RequestException as e:
        print(f"Error: {e}")

    return 0
