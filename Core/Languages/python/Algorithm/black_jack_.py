'''
from collections import Counter


def instancekey(letters):
    return tuple(sorted(Counter(letters).values()))


memo = {}


def permcount(letters):
    if not letters:
        return 1
    key = instancekey(letters)
    count = memo.get(key)
    if count is None:
        count = 0
        for letter, lettercount in Counter(letters).items():
            rest = letters
            for i in range(lettercount):
                j = rest.find(letter)
                rest = rest[:j] + rest[j + 1:]
                if i % 2 == 0:
                    count += permcount(rest)
                else:
                    count -= permcount(rest)
        memo[key] = count
    return count

print(permcount("aaabb"))
'''
'''
from itertools import permutations 
  
# Get all permutations of [1, 2, 3] 
perm = permutations(['a', 'a', 'b','b']) 
  
for i in perm:
    for j in perm

'''
hand_1=['3', '9']
hand_2=['8']
def pick_ace_value(val):
    if val + 11 > 21:
        return  1
    return 11

def total_card_value(hand):
    face_card = ['K','A','J','Q']
    value=0
    
    for i in hand:
        if i not in face_card:
            value += int(i)
        elif i != 'A':
                value += 10
    total_value= value
    
    for i in hand:
        if i =='A':
            total_value += pick_ace_value(value)
    return total_value

def blackjack_hand_greater_than(hand_1, hand_2):
    hand_1_value = total_card_value(hand_1)
    hand_2_value = total_card_value(hand_2)
    if hand_1_value > hand_2_value or hand_2_value>21:
        if hand_1_value <= 21:
            return True
    
    return False

print(blackjack_hand_greater_than(hand_1,hand_2))