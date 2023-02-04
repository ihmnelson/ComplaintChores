import json

with open('data/chores.json', 'r') as f:
    chores = json.load(f)
with open('data/people.json', 'r') as f:
    people = json.load(f)

print(chores)
print(people)
