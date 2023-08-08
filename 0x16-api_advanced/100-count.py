#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "my-app/0.0.1"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return
    data = response.json()
    for post in data["data"]["children"]:
        title = post["data"]["title"]
        for word in word_list:
            word_count[word] = word_count.get(word, 0) + title.lower().count(word.lower())
    after = data["data"]["after"]
    if after is not None:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            if count > 0:
                print(f"{word}: {count}")
