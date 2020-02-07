import tcod as libtcod


def handle_keys(key):
    key_char = chr(key.c)
    # Movement keys
    if key.vk == libtcod.KEY_KP8 or key_char == "k":
        return {"move": (0, -1)}
    elif key.vk == libtcod.KEY_KP2 or key_char == "j":
        return {"move": (0, 1)}
    elif key.vk == libtcod.KEY_KP4 or key_char == "h":
        return {"move": (-1, 0)}
    elif key.vk == libtcod.KEY_KP6 or key_char == "l":
        return {"move": (1, 0)}
    elif key.vk == libtcod.KEY_KP7 or key_char == "l":
        return {"move": (-1, -1)}
    elif key.vk == libtcod.KEY_KP9 or key_char == "l":
        return {"move": (1, -1)}
    elif key.vk == libtcod.KEY_KP1 or key_char == "l":
        return {"move": (-1, 1)}
    elif key.vk == libtcod.KEY_KP3 or key_char == "l":
        return {"move": (1, 1)}

    if key_char == "g":
        return {"pickup": True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {"fullscreen": True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {"exit": True}

    # No key was pressed
    return {}
