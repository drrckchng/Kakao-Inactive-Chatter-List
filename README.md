# Kakao Inactive Chatter List
Return a list of inactive chatters from Kakao Open Chat logs.

Often times, Kakao Open Chat rooms felt daunting due to the amount of people in them. However, many of these users are actually inactive and just stay in the room.

This script was created to help in moderation of a Kakao Open Chat where we try to encourage active user participation.

## Configuration
By default, inactive period is set to 30 days.

This can be changed by modifying the `timedelta`
```
start_date = end_date - timedelta(days=30)
```

## Usage
To run this script extract the contents Kakao Chat log archive into to `logs/` directory.

Files MUST be ordered by time in the `logs/`

After organizing the chat logs, simply run:
```
python main.py
```

## Warnings
This script has not been tested with Korean logs.

My Kakao is set in English and automated messages are in English. For Korean (or other language) users, you might need to modify the conditional statements to account for the different messages.

Date format could also be different depending on region. You would need to modify the RegEx to select the date properly.
