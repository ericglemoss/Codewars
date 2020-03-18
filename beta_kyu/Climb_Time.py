# You have a rope that you know the length of in meters and a guide book that tells you the height of your climb in feet.
# If the rope is long enough to complete the climb, you're golden to send a stellar climb (return true).

def can_climb(rope_length,climb_height):
    if isinstance(rope_length,str) != True and isinstance(rope_length,bool) != True and isinstance(climb_height,str) != True and isinstance(climb_height,bool) != True and rope_length is not None and climb_height is not None:
        return True if int(rope_length) > int(climb_height)*0.304799 else False
    return None
