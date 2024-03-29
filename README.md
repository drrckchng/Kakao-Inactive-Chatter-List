# Kakao Inactive Chatter List
Return a list of inactive chatters from Kakao Open Chat logs.

Often times, Kakao Open Chat rooms felt daunting due to the amount of people in them. However, many of these users are actually inactive and just stay in the room.

This script was created to help in moderation of a Kakao Open Chat where we try to encourage active user participation.

# Requirements

Pandas

## Configuration
By default, inactive period is set to 30 days.

This can be changed by modifying the `timedelta`
```
start_date = end_date - timedelta(days=30)
```

## Usage
To run this script, extract the contents of a Kakao Chat log archive into `logs/` directory.

Files MUST be ordered sequentially in the `logs/` directory.

After organizing the chat logs, simply run:
```
python main.py
```

## Warnings
This script has not been tested with Korean logs.

My Kakao app is set in English and thus the automated messages are in English. For Korean (or any other language) users, you might need to modify the conditional statements to account for the different messages.

Date format could also be different depending on region. You would need to modify the RegEx to select the date properly.
