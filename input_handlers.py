import tcod as libtcod

from game_states import GameStates


def handle_keys(key, game_state):
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key)
    elif game_state == GameStates.SHOW_INVENTORY:
        return handle_inventory_keys(key)

    return {}


def handle_player_turn_keys(key):
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

    elif key_char == "i":
        return {"show_inventory": True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {"fullscreen": True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {"exit": True}

    # No key was pressed
    return {}


def handle_player_dead_keys(key):
    key_char = chr(key.c)

    if key_char == "i":
        return {"show_inventory": True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {"fullscreen": True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exits the menu
        return {"exit": True}

    return {}


def handle_inventory_keys(key):
    index = key.c - ord("a")

    if index >= 0:
        return {"inventory_index": index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+enter: toggle full screen
        return {"fullscreen": True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exits the menu
        return {"exit": True}

    return {}
