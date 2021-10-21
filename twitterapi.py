import tweepy

auth = tweepy.OAuthHandler("lmOT7OKQXox3PZmxjtaxHsbvn", "uRWHUOuitaCvzqU5NWEX2cidsxtaBVjrS2RRaQAdBsuIT8lhLF")
auth.set_access_token("961058910064005120-poQq3o4Nh5lAudKg6ayqh943ropr8VY", "xqbm1Dy8qqrRPh6hDcYkZQUuOD63v4cyj94UfBkChz29V")

api = tweepy.API(auth)


# public_tweets = api.user_timeline(*, user_id, screen_name, since_id, count, max_id, trim_user, exclude_replies, include_rts)
public_tweets = api.user_timeline(screen_name = 'uva', count = 10)
for tweet in public_tweets:
    print(tweet.text)