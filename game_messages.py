import tcod as libtcod

import textwrap


class Message:
    def __init__(self, text, color=libtcod.white):
        self.text = text
        self.color = color


class MessageLog:
    def __init__(self, x, width, height):
        self.messages = []
        self.x = x
        self.width = width
        self.height = height

    def add_message(self, message):
        # Splits messages if necessary across multiple lines
        new_msg_lines = textwrap.wrap(message.text, self.width)

        for line in new_msg_lines:
            # If the buffer is full, removes the first line to make room for new ones
            if len(self.messages) == self.height:
                del self.messages[0]

            # Adds the new line as a object
            self.messages.append(Message(line, message.color))
