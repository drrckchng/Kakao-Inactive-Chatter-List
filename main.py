from datetime import timedelta
import re
import pandas as pd
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
            message = 'Announce: JOINED THE CHAT'
        elif 'left this chatroom.' in line:
            user = line.split('M: ')[1].split(' left this chatroom.')[0]
            message = 'Announce: LEFT THE CHAT.'
        elif 'has been assigned as the admin' in line:
            user = line.split('M: ')[1].split(' has been assigned as the admin.')[0]
            message = 'Announce: ASSIGNED AS ADMIN.'
        elif 'The host has been reassigned' in line or 'This message has been hidden by the chatroom managers.':
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
start_date = end_date - timedelta(days=30)

users = pd.unique(df['user'].to_list())

active_users = pd.unique(df[df['date'].between(start_date, end_date)]['user'].to_list())

inactive_users = list(set(users) - set(active_users))
print(inactive_users)
