#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import random
import datetime
import csv
import re
import telepot

'''
A simple Telegram bot that announces weekly cleaning chores.
Only talks in a given channel (group chat) and doesn't respond to anything.
'''

token = ''
channel = ''
bot = telepot.Bot(token)

week = datetime.date.today().isocalendar()[1] # current week number
assert(1 <= week <= 53), 'invalid week number'

# read a csv file of the format:
# week, suffix, [suffix], [suffix], suffix
schedule = csv.reader(open('schedule.csv', 'r'))
chores = []
for row in schedule:
    if (int(row[0]) == week):
        chores = row[1:5] # the suffix for this week
# there should be 4 chores which are either assigned to A-H or unassigned
r = re.compile('^[A-H]?$')
assert(len(chores) == 4 and all(r.search(chore) for chore in chores)),\
        'invalid chores'

# read a csv file of the format:
# suffix, name
people = csv.reader(open('people.csv', 'r'))
people_map = dict((row[0],row[1]) for row in people) # convert to a dict
# there are eight people living in our house and all of them have a name
assert(len(people_map) == 8 and all(person != '' for person in people_map)),\
        'invalid people_map'

people_map[''] = '' # add nameless room and person for the replacement below
chores = [people_map[x] for x in chores] # replace every suffix by name

message = 'This week (' + str(week) + ') the chores are divided as follows:\n<b>'
message += chores[0] + '</b>  kitchen unit\n<b>'
if (chores[2] == ''):
    message += chores[1] + '</b>  floor kitchen\n<b>'
else:
    message += chores[2] + '</b>  floor hallway<b>'
message += chores[3] + '</b>  waste paper, garbage and glass'

# checks if the message looks roughly what we expect it to be
assert(0 < len(message) <= 200), 'message is either empty or too long'
assert(len(re.findall('\n', message)) == 3), 'message has wrong format'

bot.sendMessage(channel, message, parse_mode='HTML')
