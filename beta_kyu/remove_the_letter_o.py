# Create a function removeO to remove all of the letters o in a string.
# There's no need to worry about uppercase letters.

def removeO(string):
    return ''.join([c for c in string if c !='o'])
