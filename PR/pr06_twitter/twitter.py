"""Twitter."""


class Tweet:
    """Wof."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """Wof."""
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


def find_fastest_growing(tweets: list) -> Tweet:
    """Wof."""
    growlist = []
    for t in tweets:
        grow = t.retweets / t.time
        growlist.append(grow)

    max_grow_tw = growlist.index(max(growlist))
    return tweets[max_grow_tw]


def sort_by_popularity(tweets: list) -> list:
    """Wof."""
    popsort = sorted(tweets, key=lambda x: (x.retweets, -x.time), reverse=True)
    return popsort


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """Wof."""
    ftweets = []
    for t in tweets:
        if hashtag in t.content:
            ftweets.append(t)

    return ftweets


def sort_hashtags_by_popularity(tweets: list) -> list:
    """Wof."""
    hashtags = {}
    taglist = []

    for t in tweets:
        for tag in t.content.split():
            if tag.startswith("#"):
                taglist.append(tag)
                cnt = t.retweets
                if tag in hashtags:
                    hashtags[tag] = hashtags.get(tag) + cnt
                else:
                    hashtags[tag] = cnt

    print(hashtags)
    sorted_dict = sorted(hashtags, key=lambda k: (-hashtags[k], k))
    return sorted_dict
