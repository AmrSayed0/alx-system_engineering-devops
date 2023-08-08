#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "underscoDe@alx-holbertonschool"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data")
        if "children" in data:
            children = data["children"]
            if children:
                [print(child.get("data").get("title")) for child in children]
            else:
                print("No posts found in the subreddit.")
        else:
            print("No valid data found in the response.")
    elif response.status_code == 404:
        print("Subreddit not found.")
    else:
        print("An error occurred. Status code:", response.status_code)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
