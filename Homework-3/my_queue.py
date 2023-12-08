"""A] Write a program that takes in an input file and prints out a list with the final
order of who’s in the queue.
You are expected to use the provided input file hw3_q1.txt to develop and test your
solution.

The first word on each line will either be “JUMP” or “JOIN” and the second word the
name of the person, the word “JUMP” means the person in question has gone to
the front of the queue, if the word is “JOIN” it means they have joined the back of
the queue.

You are expected to identify and use a container from the collections module for
your solution."""
from typing import List, Any
from collections import deque


people: list[str | Any] = ['JUMP Amal',
          'JUMP Belle',
          'JUMP Charlie',
          'JUMP Dylan',
          'JOIN Evelyn',
          'JUMP Frankie',
          'JUMP Gloria',
          'JOIN Helen',
          'JOIN Iman',
          'JOIN Joey',
          'JOIN Kimberley',
          'JUMP Lauren',
          'JOIN Marie',
          'JUMP Nuria',
          'JUMP Odette',
          'JUMP Priyanka',
          'JOIN Quinn',
          'JOIN Romily',
          'JOIN Sofia',
          'JUMP Theresa',
          'JUMP Una',
          'JUMP Violet',
          'JOIN Wanda',
          'JUMP Xanthe',
          'JOIN Yvonne',
          'JOIN Zara']

#added to the front
def createQueue(people):
    my_deqeue = deque()
    for person in people:
        person_split = person.split()
        new_list = person_split[1] + ' ' + person_split[0].lower().replace('jump', 'appendleft').replace('join', 'append')
        person_plus_instruction = [new_list.split()]
        for entries in person_plus_instruction:
            if entries[1] == 'appendleft':
                my_deqeue.appendleft(entries[0])
            elif entries[1] == 'append':
                my_deqeue.append(entries[0])
    return my_deqeue

print(createQueue(people))

"""QUESTION B: What is the time and space complexity of your solution? if you are making any assumptions list them"""

"""The time complexity of this solution is O(n) as it has a loop. I at first was thinking it was O(n2) because of 
the nested loop but as the nested loop is only performing on each 'person' in the list of people, therefore it should 
not increase the time and space complexity. The rest of the entries e.g. split and replace should have a minor effect
on time and space complexity it also exists outside of a function so it should not have the added time complexity
involved in calling the function"""

