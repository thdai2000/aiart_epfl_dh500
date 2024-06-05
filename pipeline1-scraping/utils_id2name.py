import praw
import pandas as pd

# Replace them with your keys.
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent=""
)


def get_username(reddit, fullname):
    try:
        redditor = reddit.redditor(fullname=fullname)
        # print(redditor)
        return redditor.name
    except Exception as e:
        print(f"Failed to get username for user {user_id}: {e}")
        return None


users = pd.read_csv('redditor_id_unique.csv')
user_ids = users['redditor_id'].tolist()
print('user_ids:', len(user_ids))

fullnames = []
for user_id in user_ids:
    if user_id.startswith('suspended:'):
        continue
    elif user_id.startswith('t2_'):
        fullnames.append(user_id)
    else:
        fullnames.append('t2_' + user_id)

print('fullnames:', len(fullnames))

user_names = []

for fullname in fullnames:
    username = get_username(reddit, fullname)
    print(username)
    user_names.append(username)

print('user_names:', len(user_names))

user_names_df = pd.DataFrame({'user_name': user_names})

user_names_df.to_csv('user_names.csv', index=False)