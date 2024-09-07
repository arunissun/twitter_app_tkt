import os
import time
import tweepy

def get_tweepy_api(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuth1UserHandler(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    return tweepy.API(auth)

def get_tweepy_client(consumer_key, consumer_secret, access_token, access_token_secret):
    return tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

def upload_media(image_paths, api):
    media_ids = []
    for image_path in image_paths:
        if os.path.exists(image_path):
            media = api.media_upload(image_path)
            media_ids.append(media.media_id)
    return media_ids

def post_tweet(text, image_paths=None, api=None, client=None, in_reply_to=None, quote_tweet_id=None):
    media_ids = None

    # Handle image_paths as a list or comma-separated string
    if image_paths:
        if isinstance(image_paths, str):
            image_paths_list = [path.strip() for path in image_paths.split(',')]  # Split paths by comma
        elif isinstance(image_paths, list):
            image_paths_list = [path.strip() for path in image_paths]  # Directly use the list
        else:
            image_paths_list = []  # Handle unexpected types

        # Upload media and get media_ids
        media_ids = upload_media(image_paths_list, api)

    # Create tweet with or without media
    tweet_params = {'text': text}
    if media_ids:
        tweet_params['media_ids'] = media_ids

    if in_reply_to:
        tweet_params['in_reply_to_status_id'] = in_reply_to
    if quote_tweet_id:
        tweet_params['quote_tweet_id'] = quote_tweet_id

    # Create the tweet using the client
    response = client.create_tweet(**tweet_params)
    print(f"Tweet URL: https://twitter.com/user/status/{response.data['id']}")


def post_all_tweets(tweet_text_vars, image_path_vars, credentials):
    """Function to post all tweets with corresponding images at 30-second intervals."""
    consumer_key, consumer_secret, access_token, access_token_secret = credentials
    api = tweepy.API(
        tweepy.OAuth1UserHandler(
            consumer_key, consumer_secret, access_token, access_token_secret
        )
    )
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    tweets = []
    for tweet_text_var, image_path_str in zip(tweet_text_vars, image_path_vars):
        tweet_text = tweet_text_var.get("1.0", "end").strip()
        image_paths = image_path_str.strip().split('\n')  # Split by new lines
        if tweet_text:
            tweets.append((tweet_text, image_paths))

    def delayed_post(tweets, interval):
        for tweet, image_paths in tweets:
            post_tweet(tweet, image_paths, api=api, client=client)
            time.sleep(interval)  # Delay for the specified interval

    # Post tweets sequentially with a delay
    interval = 20  # seconds
    delayed_post(tweets, interval)

