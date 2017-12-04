#!/usr/bin/env python3
"""
User class & related
"""

# local imports
import env
import pickle
import unicodedata

class User:
    """
    User object that represents a nick speaking in a chan
    """
    max_hist = env.MAX_HIST

    def __init__(self, nick, chan):
        self.nick = nick
        self.chan = chan
        self.lines = []

    def spoke(self, msg):
        """
        Append to tracked message history, automatically truncates old history
        """
        self.lines.append(msg)
        self.lines = self.lines[:self.max_hist]

    def save(self, loc=env.SAVE_LOC):
        filename = loc + "/" + self.chan + "____" + self.nick
        # FIXME:                        fix ^
        # FIXME: politely steal from https://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename
        # TODO: pickle! (http://www.diveintopython3.net/serializing.html)
        with open()
