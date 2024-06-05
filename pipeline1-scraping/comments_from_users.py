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
import pandas as pd

reddit_client = login.reddit(public_key=REDDIT_PUBLIC, secret_key=REDDIT_SECRET, user_agent=REDDIT_USER_AGENT)
supabase_client = login.supabase(url=SUPABASE_URL, private_key=SUPABASE_KEY)

from redditharbor.utils import fetch
from redditharbor.dock.pipeline import collect
collect = collect(reddit_client=reddit_client, supabase_client=supabase_client, db_config=DB_CONFIG)


users = pd.read_csv('user_names.csv')
users_list = users['user_name'].tolist()

print('total users:', len(users_list))


start_time = time.time()
collect.comment_from_user(user_names=users_list, sort_types=["hot"], limit=20)
end_time = time.time()
elapsed_time = (end_time - start_time) / 60
print(f"Elapsed time: {elapsed_time:.2f} minutes")
