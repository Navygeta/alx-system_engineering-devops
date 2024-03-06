#!/usr/bin/python3

import requests


def get_hot_posts(subreddit, limit=10):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": limit}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()
        results = response.json().get("data")
        return [c.get("data").get("title") for c in results.get("children")]

    except requests.RequestException as e:
        raise Exception(f"Error making request to Reddit API: {e}")


def print_top_ten_titles(subreddit):
    hot_posts = get_hot_posts(subreddit, limit=10)

    if not hot_posts:
        print("None")
        return

    for index, title in enumerate(hot_posts, start=1):
        print(f"{index}. {title}")


if __name__ == "__main__":
    subreddit_name = "python"
    print_top_ten_titles(subreddit_name)
