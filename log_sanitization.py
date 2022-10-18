import re

# Open consolidated log file
final_log_txt= open('Talk_logs.txt', 'w')

# Read log file (testing)
log_txt = open('logs/Talk_2022.10.19 02:18-1.txt', 'r')
log = log_txt.readlines()

# Delete first 5 lines of each new log file
del log[0:5]

# Regex pattern for valid chat message
pattern = re.compile('[A-Z][a-z]{2} [0-9]{1,2}, [0-9]{4} [0-9]{1,2}:[0-9]{2} [A-Z]{2},.*')

# Loop through log file
for x in log:
    if pattern.match(x):
        final_log_txt.write(x)
    
