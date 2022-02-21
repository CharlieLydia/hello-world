"""
TM112 21D TMA03 Q2 starter code
TM112 Module Team 17/12/2020
"""

from random import *


def show_flashcard():
    """ 
        The program asks the user to enter s to show a flashcard or q to quit.
        If the user inputs an s the program takes 2 random keys from the glossary and outputs one to the user,
        the program then outputs two definitions from the glossary, one wrong and one right and then
        asks the user to choose the correct one by entering either 1 or 2,
        If the user enters the right key the output will be correct otherwise the output will be incorrect.
        The program will then ask the user to enter s to show a flashcard or q to quit.
    """

    # Get glossary keys.
    keys = list(glossary)

    # Choose two random glossary keys.
    random_key1 = choice(list(glossary))
    random_key2 = choice(list(glossary))
    # Keep checking random_key2 until
    # it is different from random_key1
    while random_key2 == random_key1:
      random_key2 = choice(list(glossary))   

    # Display random glossary key.
    print('Here is a glossary entry:', random_key1)

    # Choose a random order to display the definitions in
    # '1' means the correct definition
    #  should be printed first.
    #
    # '2' means the correct definition
    # should printed second.
    #
    correct_def = choice(['1', '2'])

    # INSERT YOUR CODE IMMEDIATELY BELOW.

        
    print ('Here are two possible definitions.')
    if correct_def == '1':
        print ('\n','1.',glossary[random_key1],'\n','2.', glossary[random_key2])
    if correct_def == '2':
        print ('\n','1.',glossary[random_key2],'\n','2.', glossary[random_key1])
        

    user_input = input ('Which definition is correct? Enter either 1 or 2')
    if correct_def == '1' and user_input == '1' or correct_def == '2' and user_input == '2':
        print('Correct')
    else:
        print ('incorrect')
  
    
 



# DO NOT CHANGE ANYTHING IN THE NEXT SECTION    

# Set up the glossary

glossary = {'word1':'definition1',
            'word2':'definition2',
            'word3':'definition3'}

# The interactive loop

exit = False
while not exit:
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')
                       

