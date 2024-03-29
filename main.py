from datetime import timedelta
import re
import pandas as pd
import numpy as np
import sanitize_logs

# Ask user input to update logs
while True:
    update = input('Update logs? [y/n] ')
    if update.lower() in ['y', 'yes']:
        sanitize_logs.updateLog()
        break
    elif update.lower() in ['n', 'no']:
        break
    else:
        print('Please enter valid input')

# Regex Patterns
date_pattern = re.compile('[A-Z][a-z]{2} [0-9]{1,2}, [0-9]{4} [0-9]{1,2}:[0-9]{2} [A-Z]{2}')

# Empty list
lines = []

# Loop through each line in final logs
with open('Talk_logs.txt', 'r') as f:
    for line in f:
        if 'joined this chatroom.' in line:
            user = line.split('M: ')[1].split(' joined')[0]
            message = 'Announce: JOINED THE CHAT.'
        elif 'left this chatroom.' in line:
            user = line.split('M: ')[1].split(' left this chatroom.')[0]
            message = 'Announce: LEFT THE CHAT.'
        elif 'has been assigned as the admin' in line:
            user = line.split('M: ')[1].split(' has been assigned as the admin.')[0]
            message = 'Announce: ASSIGNED AS ADMIN.'
        elif 'has been removed from this chatroom' in line:
            user = line.split('M: ')[1].split(' has been removed from this chatroom.')[0]
            message = 'Announce: REMOVED FROM CHAT.'
        elif 'The host has been reassigned' in line or 'This message has been hidden by the chatroom managers.' in line or 'is no longer an admin' in line:
            continue
        else:
            user = line.split('M, ')[1].split(' : ')[0]
            message = line.split('M, ')[1].split(' : ')[1]

        # Use regex to get date and convert to pd datetime obj
        date = pd.to_datetime(date_pattern.search(line).group())

        # Add dictionary to empty list
        lines.append({
            'date': date,
            'user': user,
            'message': message
        })

df = pd.DataFrame(lines)

# Dates
end_date = lines[-1]['date']
start_date = end_date - timedelta(days=28)

# Get list of all users and active users
users = df['user'].str.strip().unique()
active_users = df[df['date'].between(start_date, end_date)]['user'].str.strip().unique()

# Get all inactive users
inactive_users = list(set(users) - set(active_users))

# Missing Users
missing_users = []

# Remove users who have left
for user in inactive_users:
    last_message = ''
    if df[df['user'] == user].shape[0] == 0:
        last_message = 'Announce: JOINED CHAT.'
    else:
        last_message = df[df['user'] == user]['message'].iloc[-1] 
    if last_message == 'Announce: LEFT THE CHAT.' or last_message == 'Announce: REMOVED FROM CHAT.' or last_message == 'Announce: JOINED CHAT.':
        missing_users.append(user)

# Remove missing users from list
inactive_users = list(set(inactive_users) - set(missing_users))

print(inactive_users)
