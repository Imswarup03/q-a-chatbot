import tweepy
import pandas as pd
import time

latest_tweet_number = 0


# with open("C:\\Users\\User\\Desktop\\LangChain\\twitter_number.txt") as f:
#     latest_tweet_number = int(f.read())

print(latest_tweet_number)

import pandas as pd
df = pd.read_csv(r"C:\\Users\\User\\Desktop\\LangChain\\twitter.csv", sep=';')

def tweet_now(msg):
    msg = msg[0:270]
    try:

        auth = tweepy.OAuthHandler("zrTTiOIRqqBWodFAWlHZ6SzRX", 
            "8tGNpdPlxonar9XU3HXN8oDSDemMycdq11KjonkOptxfqssM5u")
        auth.set_access_token("793449496051154944-Hl3uGYIApPnATb6eZQUaJeEXjXmo3E0","Jti5yGOs5kGny2Spa7gQmfM4St2KOlVnSdQwNAMY8jeyN")
        api = tweepy.API(auth)
        print("api++++++++",api)

        try:
            response = api.verify_credentials()
            print("response==================>",response.status_code)
            # print("response",response)
            print("Authentication OK")
        except:
            print("Error during authentication")
        api = tweepy.API(auth, wait_on_rate_limit=True )
        print({"api=============":api})
        api.create_tweet(msg)
        print("msg======",msg)

        print("Tweeted")
    
    except Exception as e:
        print(e)

for idx, rows in df.iterrows():
    if idx <= latest_tweet_number:
        continue
        
    hashtags = '#inspirational #inspiration #motivation #motivational #inspirationalquotes #inspire #motivationalquotes #quotes #love #quoteoftheday #success #believe #mindset #life #positivevibes #entrepreneur #quote #positivity #goals #selflove #happiness #lifestyle #successquotes #bhfyp #yourself #thoughts #instadaily #loveyourself #photooftheday #bhfyp'
    tweet_now(rows['QUOTE'] + ' - ' + rows['AUTHOR'] + '\n\n\n' + hashtags)
    
    with open("C:\\Users\\User\\Desktop\\LangChain\\twitter_number.txt","w") as f:
        f.write(str(idx))

    print("done")
    time.sleep(1800)
