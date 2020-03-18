# Write a function dirReduc which will take an array of strings and returns an array of strings with the needless 
# directions removed (W<->E or S<->N side by side).

def dirReduc(arr):
    cases = {"NORTH":"SOUTH","SOUTH":"NORTH",
            "EAST":"WEST", "WEST":"EAST"}
    out = []
    for elem in arr:
        if out and cases[elem] == out[-1]:
            out.pop()
        else:
            out.append(elem)
    return out
