"""
Project: milestone 2
Author: UmangA
Date: 25 April, 2020
Description:
            The program asks an user to input names of 3 friends. If the names are found in the database it assumes that the friends are present in the
            same city. Thus, the program will add those names to the file, nearby friends.
            operations for the program:
                file: friends
                        - reads the file for accessing the content
                file: nearby_friends
                        - writes to the file
                        - reads the file for printing the content

Algorithm:
    -temporary lists:
            ->friends to save user input
            ->nearby_friends_list to save nearby friends generated from the process
    - open and read the contents of file friends
    - compare each friend in the friends files to the entries in the friends list containing user input
    - if true append the friend along with a new line char to the nearby friends list
    - finally open nearby friends file and write a string to the file.[NOTE: You cannot write a list to the file, only strings.]
    - read the nearby_friends file to show the updated contents of the file.

Issues:
    - White spaces must be removed instead of adding them to the user input.
    - Use .strip() function to remove the whitespaces and new line char
"""
#initialization -------------------------------------------------------------- Active
friends = []
nearby_friends_list = []
#user input ------------------------------------------------------------------ Active
for _ in range(0,3):
    friend = input("Enter the name of friend: ")
    friends.append(friend+"\n")
print(friends)

#contents of file friends ----------------------------------------------------- Active
friends_file = open("friends.txt","r")
file_content = friends_file.readlines()
friends_file.close()
#printing content ------------------------------------------------------------- Debugging
print(f"the file content is as follows: \n{file_content}\n\n")

#process ----------------------------------------------------------------------
for content in file_content:
    for friend in friends:
        if friend == content:
            nearby_friends_list.append(friend)
            break                                                              #stop the loop when found, saves time!

# update nearby_friends file -------------------------------------------------- Active
nearby_friends = open("nearby_friends.txt","w")
print(nearby_friends_list)
for _ in nearby_friends_list:
    nearby_friends.write(_ +"\n")
nearby_friends.close
#show update ------------------------------------------------------------------ Active/Debugging
nearby_friends = open("nearby_friends.txt","r")
print(f"nearby friends: {nearby_friends.read()}")
nearby_friends.close


"""
Better implementation
Author: Jose Salvatierra (https://jslvtr.com)
Code Location: https://github.com/jslvtr

# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to `nearby_friends.txt`

friends = input('Enter three friend names, separated by commas (no spaces, please): ').split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()


"""


