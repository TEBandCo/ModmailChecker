# ModmailChecker - A Reddit bot for mods.
Checks Reddit modmail messages for a specified subreddit, archives them if they containing a word from badword list.

Edit praw.ini with your bots:
- username
- password
- client_id
- client_secret

Then, edit modmailChecker.py with the subreddit mail to be checked. Next, edit the badWords list with words (or phases) you want checked. 

Now, just run the script, it'll run constantly so may be a good idea to cron job it to run at regular intervals.
