# Replace them with your keys.
SUPABASE_URL = ""
SUPABASE_KEY = ""

REDDIT_PUBLIC = ""
REDDIT_SECRET = ""
REDDIT_USER_AGENT = ""  # format - <institution:project-name (u/reddit-username)>

DB_CONFIG = {
    "user": "test_redditor",
    "submission": "test_submission",
    "comment": "test_comment"
}

import redditharbor.login as login
import time
import sys

reddit_client = login.reddit(public_key=REDDIT_PUBLIC, secret_key=REDDIT_SECRET, user_agent=REDDIT_USER_AGENT)
supabase_client = login.supabase(url=SUPABASE_URL, private_key=SUPABASE_KEY)

from redditharbor.dock.pipeline import collect

collect = collect(reddit_client=reddit_client, supabase_client=supabase_client, db_config=DB_CONFIG)

subreddits = ['aiwars',
              'aiArt',
              'Generative',
              'DefendingAIArt']

#
# query = ("(AI and art) OR (AI and music) OR (AI and paint) OR (AI and film) OR (AI and animation) OR (AI and "
#          "sculpture) OR (AI and design) OR (AI and graphic) OR (AI and artist) OR (AI and creative) OR (Generative "
#          "and art) OR (Generative and music) OR (Generative and paint) OR (Generative and film) OR (Generative and "
#          "animation) OR (Generative and sculpture) OR (Generative and design) OR (Generative and graphic) OR ("
#          "Generative and artist) OR (Generative and creative)")

sort_types = ["hot", "top"]
start_time = time.time()

# collect.submission_by_keyword(subreddits, query, limit=None)
collect.subreddit_submission(subreddits, sort_types, limit=None)

end_time = time.time()
elapsed_time = (end_time - start_time) / 60
print(f"Elapsed time: {elapsed_time:.2f} minutes")

