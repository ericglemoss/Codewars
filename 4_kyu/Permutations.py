# In this kata you have to create all permutations of an input string and remove duplicates, if present.
# This means, you have to shuffle all letters from the input in all possible orders.

# Examples:

# permutations('a'); # ['a']
# permutations('ab'); # ['ab', 'ba']
# permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

# The order of the permutations doesn't matter.

def permutations(string):
    out = set([string])
    if len(string) == 2:
        out.add(string[1]+string[0])
    elif len(string) > 2:
        for k, m in enumerate(string):
            for i in permutations(string[:k] + string[k+1:]):
                out.add(m+i)
    return list(out)
