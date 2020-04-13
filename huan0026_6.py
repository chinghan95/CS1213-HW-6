"""
Ching Han Huang
113510994
11/20/19

Assignment 6 : Working with File(s)
"""
import random
# Prompt the user to enter a filename / path to read
file = open(input('What file would you like to process?'))
print('')
### file = open('Desktop/CS 1213/Projects/file.txt')

# Create names list and items list
names, items = [], []
# Read each line of the user-specificed file
line = file.readline()
# Check if there still has line to read 
while line != '':
    theLine = line.strip()
    # if line starts with 'name', ignore 'name' and store the rest content in names list
    if theLine.startswith('name'):
        space, name = theLine.split('name ')
        if name != '':
            names.append(name)
    # if line starts with 'item', ignore 'item' and store the rest content in items list
    elif theLine.startswith('item'):
        space, item = theLine.split('item ')
        if item != '':
            items.append(item)
    line = file.readline()

# Randomly choice item in items list for a name
for x in names:
    randomItem = random.choice(items)
    items.remove(randomItem)
    print(x, ' - ', randomItem)
# Close the file
file.close()

print('')
print('Thanks for using my program.')