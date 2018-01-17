import misc
import random
import time



choice_prompt = 'Enter your choice: '


def print_options(option_list):
    """Prints an enumerated list"""
    for i in range(len(option_list)):
        print('{0}) {1}'.format(i, option_list[i]))


def knight_convo(selection, playername):
    """This is where you talk about what the method does"""
    options = ['Answer his questions', 'Make up a lie', 'Do nothing.']
    if selection == '0':
        print('Who are you and why do you come to my village?')
        print('...')
    else:
        print('Who are you and why do you come to my village?'.upper())
        print('...')
    time.sleep(0)
    print_options(options)
    print('...')
    answer1 = input(choice_prompt)
    if answer1 == '0':
        print('I am %s and I am here on business to remove the dragon from this village.' % playername )
        print('...')
        print('By all means, enter. Good luck!')
        return
    elif answer1 == '1':
        print(random.choice(misc.lies))
        print('...')
        print('That sounds suspicious. Why are you here again?')
    elif answer1 == '2':
        print('I need you to answer my questions!'.upper())
    print_options(options)
    answer1 = input(choice_prompt)
    if answer1 == '0':
        print('I am %s and I am here on business to remove the dragon from this village.' % playername)
        print('...')
        print('By all means, enter. Good luck with the dragon!')
        return
    else:
        print('The knight had enough of your silly games and slices your head clean off.')
        print('...')
        print('What were you thinking?')
        print('...')
        print('Game Over.')
        """You died"""
        return


def village(selection):

    if selection == '0':
        print('As you approach the tavern, you smell the stench of unkempt men and molding food. ')
        print('...')
        print('You walk up to the tavern keeper and say:')
        time.sleep(1)
        print('There\'s rumor that a dragon is skulking around the town. Any truth in that?')
        time.sleep(3)
        print('...')
        print('Aye. There be talk that the dragon lay in a cave to the south of the town.')
        time.sleep(1)
        print('I think the mayor is offering a large bounty for the death of the dragon.')
        time.sleep(1)
        print('I suggest you speak to him for any dragon business.')
        time.sleep(3)
        print('...')
        print('That\'s some useful information.')
        print('What do you want to do now?')
        options = ['Stay in the tavern', 'Leave the tavern']
        print_options(options)
        tavern = input(choice_prompt)
        if tavern == '0':
            time.sleep(5)
            print('Well, this is getting us nowhere. Let\'s leave.')
        else:
            print('Alright, let\'s go.')

    elif selection == '1':
        print("You walk through the town until you see a large longhouse with a sign out front that reads:")
        time.sleep(1)
        print('Dragon business and inquiries only.')
        time.sleep(2)
        print('Well, this must be the right place')
        time.sleep(2)
        print('As you walk into the townhall, you hear a bunch of yelling.')
        time.sleep(2)
        print('Now people, I understand your concerns about the dragon but there is nothing that we can do')
        time.sleep(1)
        print('There aren\'t enough soldiers to fend off the dragon and protect our town.')
        print('...')
        time.sleep(1)
        print('YOU ARE A COWARD! YOU RISK THE LIVES OF ALL OF THE PEOPLE IN THIS TOWN BY NOT DEALING WITH IT!')
        print('...')
        time.sleep(1)
        print('Wow, tough crowd for the mayor, huh?')
        print('...')
        time.sleep(1)
        print('What? I\'m the narrator I can say what I want.')
        print('...')
        time.sleep(1)
        print('Fine. what do you want to do?')




