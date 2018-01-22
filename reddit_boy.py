#copyright (c) busterroni February 18, 2017
#video: https://www.youtube.com/watch?v=krTUf7BpTc0
import praw
#import config
import time

def bot_login():
	print "Loggin in..."
	r = praw.Reddit(client_id = "_WkPL3qfOww1xw",
                     client_secret = "W74sDxX2UGPSFUmnrHGu9dFJkrw",
                     username = "prasadgujar16",
                     password = "tooweaktooslow",
                     user_agent = "prawtutoral")
	print "Logged in!"

	return r

def run_bot(r):
	print "Obtaining 25 comments..."
	for comment in r.subreddit('test').comments(limit=25):
		if "dog" in comment.body:
			print "String with \"dog\" found in comment " + comment.id
			comment.reply("I also love dogs! [Here](http://i.imgur.com/LLgRKeq.jpg) is an image of one!")
			print "Replied to comment " + comment.id

	print "Sleeping for 10 seconds..."
	Sleep for 10 seconds...
	time.sleep(10)


r = bot_login()
while True:
	run_bot(r)
