This module alerts a user when their Nuuly outfit goes from unavailable to available. I wrote it in an hour for my wife so it is simply an infinite loop that sleeps for 30 seconds; an item usually becomes available same day, so I'm fine with running it and leaving my computer on all day till its available.
Change the slot with "YOUR PHONE NUMBER" in the applescript to your phone number
Run from the command line with:

python3 nuuly.py --url='URL_TO_YOUR_OUTFIT' --size='YOUR_SIZE'
