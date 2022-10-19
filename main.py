from datetime import datetime
import re
import sanitize_logs
import pandas as pd

# Ask user input to update logs
while True:
    update = input('Update logs? [y/n]')
    if update.lower() in ['y', 'yes']:
        sanitize_logs.updateLog()
    elif update.lower() in ['n', 'no']:
        break
    else:
        print('Please enter valid input')

lines = []
with open('Talk_logs.txt', 'r') as f:
    for line in f:
        lines.append(line)

df = pd.DataFrame(columns=['date', 'user', 'message'])

date_pattern = re.compile('[A-Z][a-z]{2} [0-9]{1,2}, [0-9]{4} [0-9]{1,2}:[0-9]{2} [A-Z]{2}')

for i in range(len(lines)):
    date = pd.to_datetime(date_pattern.search(lines[i]).group())
    user = 'user'
    message = 'message'
    
    df.loc[i] = pd.Series({
        'date':date,
        'user':user,
        'message':message
    })

print(df)
