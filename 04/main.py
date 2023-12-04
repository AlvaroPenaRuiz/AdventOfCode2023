from functools import reduce
import re
from typing import List
rawdata = ""

with open("data.txt", "r") as file:
    rawdata = file.read()

def get_objects_from_data(data: str):
    splitted = data.split('\n')
    structured_data =[]

    for rawcard in splitted:
        card = {}
        card['game'] = [game[0] for game in re.finditer('\d+', rawcard.split(':')[0])][0]
        halves = rawcard.split(':')[1].split('|')
        card['winning_numbers'] = [card[0] for card in re.finditer('\d+', halves[0])]
        card['numbers'] = [card[0] for card in re.finditer('\d+', halves[1])]
        structured_data.append(card)

    return structured_data

structured_data = get_objects_from_data(rawdata)


def add_more_info(cards: List[str]):
    for card in cards:
        card['quantity'] = 1
        card['score'] = 0
        matches = []

        for winning_number in card['winning_numbers']:
            for number in card['numbers']:
                if winning_number == number: matches.append(number)

        for match in matches:
            card['score'] = 1 if card['score'] == 0 else card['score'] * 2
        
        card['matches'] = len(matches)
    return cards

add_more_info(structured_data)


def get_amount_of_cards_you_really_deserve(cards: List[str]):
    for index,card in enumerate(cards):
        for subindex in range(1, card['matches']+1):
            for copy in range(1, card['quantity']+1):
                cards[index+subindex]['quantity'] += 1


# Exercise 1
total_score = reduce(lambda a,b : a+b, [card['score'] for card in structured_data])
print(total_score)

# Exercise 2
get_amount_of_cards_you_really_deserve(structured_data)
total_quantity = reduce(lambda a,b : a+b, [card['quantity'] for card in structured_data])
print(total_quantity)