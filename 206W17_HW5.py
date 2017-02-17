import unittest
import tweepy
import requests
import json

## SI 206 - W17 - HW5
## COMMENT WITH:
## Your section day/time:
## Any names of people you worked with on this assignment:

######## 500 points total ########

## Write code that uses the tweepy library to search for tweets with a phrase of the user's choice (should use the Python input function), and prints out the Tweet text and the created_at value (note that this will be in GMT time) of the first THREE tweets with at least 1 blank line in between each of them, e.g.

## TEXT: I'm an awesome Python programmer.
## CREATED AT: Sat Feb 11 04:28:19 +0000 2017

## TEXT: Go blue!
## CREATED AT: Sun Feb 12 12::35:19 +0000 2017

## .. plus one more.

## You should cache all of the data from this exercise in a file, and submit the cache file along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets about "rock climbing", when we run your code, the code should use CACHED data, and should not need to make any new request to the Twitter API. 
## But if, for instance, you have never searched for "bicycles" before you submitted your final files, then if we enter "bicycles" when we run your code, it _should_ make a request to the Twitter API.

## The lecture notes and exercises from this week will be very helpful for this. 
## Because it is dependent on user input, there are no unit tests for this -- we will run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

## **** For 50 points of extra credit, create another file called twitter_info.py that contains your consumer_key, consumer_secret, access_token, and access_token_secret, import that file here, and use the process we discuss in class to make that information secure! Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information for an 'extra' Twitter account you make just for this class, and not your personal account, because it's not ideal to share your authentication information for a real account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these with variables rather than filling in the empty strings if you choose to do the secure way for 50 EC points
consumer_key = "Te0B5HIDVx0t6Mo4BBUArbmv7" 
consumer_secret = "0IO6Omtj52U4rtRGvFZbNe3kcmzT3e5gCTVZhlXcECuf3rBUQU"
access_token = "804675986445004800-6XIC8Y3wNawB750liMfYECgS1x3yi0U"
access_token_secret = "ZSPXsPFlARViPhcxRb1VqT2765kbGNlfE7JznWPygHAWw"
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) 

#print(type(public_tweets)," is the type of publictweets")
## Write the rest of your code here!
public_tweets = api.home_timeline() 
#print (type(public_tweets))
#for tweet in public_tweets:     
	#print("\n*** type of the tweet object that is included ***\n")     
	#print(type(tweet),"type of one tweet")     
	#print(tweet) ## Huh. That's not easy to read.

# Let's pull apart one tweet to take a look at it. 
single_tweet = public_tweets[0:2]
#print (single_tweet)


#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except statement shown in class.
## 2. Write a function to get twitter data that works with the caching pattern, so it either gets new data or caches data, depending upon what the input to search for is. You can model this off the class exercise from Tuesday.
## 3. Invoke your function, save the return value in a variable, and explore the data you got back!
## 4. With what you learn from the data -- e.g. how exactly to find the text of each tweet in the big nested structure -- write code to print out content from 3 tweets, as shown above.

CACHE_FNAME = "umsi_cache_file.json"
try: 
	cache_file_obj=open(CACHE_FNAME,"r")
	cache_contents= cache_file_obj.read()
	CACHE_DICTION= json.loads(cache_contents)
except: 
	CACHE_DICTION= {}
#print (CACHE_DICTION)
	

def getWithCaching(query): 
	unique = "twitter_{}".format(query)
	if unique in CACHE_DICTION:
		print('using cached data for', query)
		twitter_results = CACHE_DICTION[unique] 
	else: 
		print('getting data from interent', query)
		twitter_results= api.search(query)
		CACHE_DICTION[unique] = twitter_results
	
	#print (type(twitter_results))

	
	f = open (CACHE_FNAME, "w")
	f.write(json.dumps(CACHE_DICTION))
	f.close()
	#print ((json.dumps(CACHE_DICTION)))

	# tweets=[]
	# for x in twitter_results:
	# 	tweets.append(x["text"])
	# return tweets[:3]
	y = twitter_results["statuses"]
	for r in y[:3]:
		w= r["created_at"]
		f=r["text"]
		#print (w)
		#print (f)
		g="TEXT: {}".format(f)
		l="CREATED AT: {}".format(w)
		print (g)
		print (l)
		print ("")

three_tweets = getWithCaching("umsi")












