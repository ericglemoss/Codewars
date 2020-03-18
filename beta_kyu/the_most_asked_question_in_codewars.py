# You need to write a function detect that will check if a string starts with Can someone explain, case sensitive.
# Return true if so, false otherwise.

def detect(comment):
    q = 'Can someone explain'
    if q not in comment or comment.find(q) != 0:
        return False
    else:
        return True
