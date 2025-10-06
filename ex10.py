####################################################
#Program Name: ex10.py
#Author: Arya Patel
#Task: write a program that asks for 3 friends' name, stores them in a list, and prints them all.
#for this code to work, i used words such as range and append.

friends= []
for i in range (3):
    name = input(f"enter first friend name #{i+1}:")
    friends.append(name)

#Print the list of friends
    print("friend name here:")
    for friend in friends:
        print(friend)

        

