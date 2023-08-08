#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    if not word_list:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "CountWordsBot"}  # Provide a user-agent to prevent 429 error
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                word = word.lower()
                if word in title:
                    counts[word] = counts.get(word, 0) + title.count(word)

        if data["data"]["after"]:
            count_words(subreddit, word_list, after=data["data"]["after"], counts=counts)
        else:
            count_words(subreddit, word_list, counts=counts)
    else:
        print("Invalid subreddit or error fetching data")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])