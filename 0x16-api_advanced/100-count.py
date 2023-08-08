#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'My Reddit API Client'}

    # Send a GET request to the subreddit's API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()

            for word in word_list:
                word = word.lower()
                if word in title:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        # Check if there are more posts to fetch (pagination)
        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                print(f"{word}: {count}")
    elif response.status_code == 404:  # Invalid subreddit
        print("Invalid subreddit.")
    else:
        print(f"An error occurred: {response.status_code}")

if __name__ == '__main__':
    subreddit = input("Enter a subreddit name: ")
    word_list = input("Enter keywords separated by spaces: ").split()
    count_words(subreddit, word_list)