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

submission_ids = pd.read_csv('submission_ids_filtered.csv')
submission_ids_list = submission_ids['submission_id'].tolist()

print('before: ', len(submission_ids_list))

id_list = pd.read_csv('existing_ids.csv')
link_id_list = id_list['link_id'].tolist()
ids_filtered = [x for x in submission_ids_list if x not in link_id_list]


idWithComments = pd.read_csv('id_with_comments.csv')
idWithComments_list = idWithComments['submission_id'].tolist()
ids_filtered = [x for x in ids_filtered if x in idWithComments_list]

print('after: ', len(ids_filtered))

start_time = time.time()

collect.comment_from_submission(submission_ids=ids_filtered,
                                level=3)  # Set level=None to collect entire comment threads
end_time = time.time()
elapsed_time = (end_time - start_time) / 60
print(f"Elapsed time: {elapsed_time:.2f} minutes")
