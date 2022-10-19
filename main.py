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

