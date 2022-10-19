import re
import pandas as pd
import sanitize_logs

# Ask user input to update logs
while True:
    update = input('Update logs? [y/n]')
    if update.lower() in ['y', 'yes']:
        sanitize_logs.updateLog()
    elif update.lower() in ['n', 'no']:
        break
    else:
        print('Please enter valid input')

# Regex Patterns
date_pattern = re.compile('[A-Z][a-z]{2} [0-9]{1,2}, [0-9]{4} [0-9]{1,2}:[0-9]{2} [A-Z]{2}')

# Empty array
lines = []

# Loop through each line in final logs
with open('Talk_logs.txt', 'r') as f:
    for line in f:
        # Split user and message
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
