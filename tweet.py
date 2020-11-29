import argparse
import tweepy
import os

def get_auth():
    return (
        os.getenv("TWITTER_CONSUMER_API_KEY"),
        os.getenv("TWITTER_CONSUMER_API_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"),
        os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
    )

def get_api(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)

def post_image(filename, status=""):
    api = get_api(*get_auth())

    media = api.media_upload(filename)

    return api.update_status(status, media_ids=[media.media_id])

def main():
    parser = argparse.ArgumentParser("Upload an image to twitter")
    parser.add_argument("filename", type=str, help="Image file to upload")
    parser.add_argument("--status", type=str, default="", help="Optional status to post alongside image")

    args = parser.parse_args()

    print("Uploading", args.filename, "with attached status:", args.status)
    print(post_image(args.filename, status=args.status))

if __name__ == "__main__":
    main()
