#!/usr/bin/python3
"""
Lock boxes
"""


def canUnlockAll(boxes):
    """Function determines if all boxes can be opened"""
    unlocked = [0]
    for b_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked \
               and key != b_id:
                unlocked.append(key)

    if len(unlocked) == len(boxes):
        return True
    return False
