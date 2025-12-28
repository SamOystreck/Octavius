# Octavius
Self-management tool for things such as schedule, reminders and statistics. 

Current (start of development) thoughts:
- Create a Python baseline to work with that is fully functional independantly
    - Database in SQL
    - End goal is to have a python-hosted server running that both the PC and mobile will be able to communicate and sync with
- Create mobile app to compliment the Python in Kotlin and communicate between the two using


# Notes
Currently there is no support for the SQL server, when development is a little further along this will be rectified

Vosk models need to be added to gitignore (they are for you Sam)




Current implementation goals (will change if they do not meet standards):
    - Porcupine wake word
    - Vosk for Speech to text


Planning for python implementation of food
    - When adding new meal, if it's been a new day (past 12am) then some global mealID should be set to 0
    - After adding a new meal, this global should be incremented
    - When calulating food:
        - I had 2 apples
        - Fetch apple stats
        - Calculate everything for the meal
        - Put all of this into meal
        - Good to go!