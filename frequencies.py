"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    strItems = []
    frequencies = {}
    for item in items:  #Convert all items to strings
        converted_key = str(item)
        strItems.append(converted_key)

    for strItem in strItems:    #Check membership and then update the value in hashmap.
        if strItem in frequencies:
            frequencies[strItem] = frequencies.get(strItem, 0) + 1
        else:
            frequencies[strItem] = 1
    return frequencies
