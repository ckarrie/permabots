#from telegram import emoji
from six import iteritems, PY2

"""
Depreciated, use direct

    http://www.unicode.org/emoji/charts/full-emoji-list.html
    
Infos:

    https://github.com/python-telegram-bot/python-telegram-bot/issues/387
    https://github.com/python-telegram-bot/python-telegram-bot/wiki/Emoji
"""

def create_emoji_context():
    context = {}
    #for key, value in iteritems(emoji.Emoji.__dict__):
    #    if '__' not in key:
    #        if PY2:
    #            value = value.decode('utf-8')
    #        context[key.lower().replace(" ", "_")] = value
    return context
