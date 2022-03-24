#authentication method and praw adapted from busterttoni11 and bboe's videos. 
#created by /u/TheEpicBlob, requested by /u/Lucy-k


#Script to check a modmail of a subreddit, if there is a new message that has never been read, will check against list of badwords. If badword is within message it'll archive the message. 
#It should work with single words, or phrases such as 'mango man', where a message containing just 'mango' or 'man' is fine. 

#v1.0


import praw
import time 



badWords = ['mango man', 'orange'] #list of bad words, must be formatted between quotes and comma, e.g. ['mango', 'orange', 'foo', 'bar']
subredditToCheck = 'SPECIFY SUBREDDIT HERE'


######################


def authenticate():
    print("Authenticating..."),
    reddit = praw.Reddit('Bot', #see praw.ini file, this should be the username 
        user_agent="Reads modmail, if the message is new *and* unread, then will check against badWords list.") #provide description of bot
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def main():
	reddit = authenticate()
	while True:
		wordToCheck = getModMessage(reddit)


def getModMessage(reddit):
	conversation = reddit.subreddit(subredditToCheck).modmail.conversations(state="inbox", sort= 'unread', limit=60)
	for convo in conversation:
		if convo.last_unread != None:
			print('I have found an unread comment: ' + convo.id)
			for message in convo.messages:
				messagetext = str(message.body_markdown)
				print('Checking: ' + convo.id)
				for word in badWords:
					if word in messagetext.lower():
						print('Bad word found: ' + word + ', archiving message ' + convo.id)
						convo.archive()
				time.sleep(0.5)
			
				
if __name__ == '__main__':
	main()
