import json
from stuff import *

with open('data/chores.json', 'r') as f:
    chores = json.load(f)
with open('data/people.json', 'r') as f:
    people = json.load(f)

print(chores)
print(people)

guy = Person(1)

