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

people = ['JUMP Amal',
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

for person in people:
    person.split()
    print(person)