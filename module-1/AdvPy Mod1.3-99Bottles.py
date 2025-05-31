# -*- coding: utf-8 -*-
"""
Created on Sat May 31 18:26:35 2025

@author: nitai
"""
'''
Nitai Paonessa, 05/31/2025, Module 1.3 Assignment.

This code will represent the song "99 bottles of beer on the wall" 
-Ask the use rhow many bottles there are then count down
-Unuique message at end when no bottles left 
'''

def Bottles_Song(starting_bottle_count):
    """
    Prints the 'Bottles of Beer' song lyrics starting from the given number of bottles
    Counts down to Zero using Range func - Special verse for when 1 bottle singular - not plural
    """
    for bottle_count in range(starting_bottle_count, 0, -1):
        if bottle_count > 1:
            # Verses with more than one bottle
            print(f"{bottle_count} bottles of beer on the wall, {bottle_count} bottles of beer.")
            print(f"Take one down and pass it around, {bottle_count - 1} {'bottle' if bottle_count - 1 == 1 else 'bottles'} of beer on the wall.\n")
        else:
            # Verse when there is only one bottle left
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")

    # Final verse after all bottles are gone
    print("No more bottles of beer on the wall, no more bottles of beer.")


def main():
    """
    Main function that prompts the user for input and starts the song countdown.
    Ends with a reminder to buy more beer.
    """
    try:
        # Ask user how many bottles to start with
        starting_bottles = int(input("How many bottles of beer are on the wall? "))
        
        if starting_bottles < 1:
            # Message for more than 1 bottle needed
            print("You need at least 1 bottle to start the song!")
        else:
            # Calling the function
            Bottles_Song(starting_bottles)
            
            print("\nGo to the store and buy some more, cheers!")
    except ValueError:
        # Input Validation
        print("\nYou might be drunk, Please enter a valid number.")


main()










'''
Resources
- https://www.w3resource.com/projects/python/python-projects-4.php
- W3schools Python
- Textbook/class resources 
'''