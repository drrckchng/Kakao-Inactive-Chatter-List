import os
import re

# Open consolidated log file
final_log_txt= open('Talk_logs.txt', 'w')


for filename in sorted(os.listdir('logs/'), key=str.lower):
    # Read log file (testing)
    log_txt = open('logs/' + filename, 'r')
    log = log_txt.readlines()

    # Delete first 5 lines of each new log file
    del log[0:5]

    # Regex pattern for valid chat message
    pattern = re.compile('[A-Z][a-z]{2} [0-9]{1,2}, [0-9]{4} [0-9]{1,2}:[0-9]{2} [A-Z]{2},.*')

    # Loop through log file
    for x in log:
        if pattern.match(x):
            final_log_txt.write(x)
    print('inserted' + filename)
        
