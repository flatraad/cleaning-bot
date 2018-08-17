# cleaning-bot

This is a simple [Telepot](https://github.com/nickoala/telepot/) bot for sending announcements about cleaning chores to a Telegram channel. It is supplementary to [`gen-clean-shed`](https://github.com/flatraad/gen-clean-shed).

## Usage

If you are not familiair with Telegram bots, refer to [the official documentation](https://core.telegram.org/bots) for obtaining a bot account.
Next, make sure that the python module `telepot` is installed.
After that, set the `token` and `channel` variables to the values you received from the BotFather. 
It expects two files to be present, `schedule.csv` and `people.csv`. The format of `schedule.csv` is detailed [in the readme of `gen-clean-shed`](https://github.com/flatraad/gen-clean-shed). `people.csv` contains eight lines with two values. The first one is the room suffix and the second one is the name associated with that room.
After that, test if running `python3 cleaning_bot.py` indeed sends a message to the specified channel. If everything is alright, it sends one message each time it is invoked. To make it send notification with a fixed interval, use `cron` or a different task scheduler.

## Possible improvements

* use command-line arguments instead of hardcoding settings
* support multiple languages
* run in the background

Note: I am no longer using this script, so don't expect any of this being implemented anytime soon.
