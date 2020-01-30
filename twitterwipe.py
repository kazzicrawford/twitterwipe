import os
import tweepy
import json
import yaml
from datetime import timedelta, datetime
from dateutil.parser import parse

def main():
    print('hello')

    with open('config.yaml', 'r') as yamlfile:
        config = yaml.load(yamlfile)

    delete_timestamps = get_delete_timestamps(config)

    purge_activity(delete_timestamps)


def get_delete_timestamps(config):
    curr_dt_utc = datetime.utcnow()

    days = config['days_to_save']
    likes = days['likes']
    retweets = days['retweets']
    tweets = days['tweets']

    likes_delta = timedelta(likes)
    retweets_delta = timedelta(tweets)
    tweets_delta = timedelta(tweets)

    likes_time = curr_dt_utc - likes_delta
    retweets_time = curr_dt_utc - retweets_delta
    tweets_time = curr_dt_utc - tweets_delta

    return (likes_time, retweets_time, tweets_time)


def purge_activity(delete_timestamps):
    api = get_api()

    delete_tweets(api, delete_timestamps[2])
    delete_retweets(api, delete_timestamps[1])
    delete_likes(api, delete_timestamps[0])


def delete_tweets(api, ts):

    for status in tweepy.Cursor(api.user_timeline).items():
        if status.created_at < ts:
            try:
                api.destroy_status(status.id)
            except:
                print('failed to delete {}'.format(status.id))
    return


def delete_retweets(api, ts):
    return


def delete_likes(api, ts):
    return


def get_api():
    with open('keys.json', 'r') as f:
        d = json.load(f)

    auth = tweepy.OAuthHandler(d['consumer_key'], d['consumer_secret'])
    auth.set_access_token(d['app_key'], d['app_secret'])

    return tweepy.API(auth)

if __name__ == '__main__':

    # insert a check for auth credentials and send error email if broken
    main()
