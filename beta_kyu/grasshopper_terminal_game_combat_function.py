# Create a combat function that takes the player's current health and the amount of damage received, and returns the player's new health.

def combat(health=0,damage=0):
    return (0 if damage > health else health-damage)
