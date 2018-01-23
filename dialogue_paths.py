import misc
import random
import time


def end_game():
    print('Thank you for playing!')


def mayor():
    print('No! I do not need anymore people to come in here and tell me how to do my job. ')
    time.sleep(1)
    print('I am sorry but you have to leave.')
    time.sleep(3)
    print('...')
    print('You misunderstand, mayor. I have come to slay this dragon.')
    time.sleep(3)
    print('...')
    print('...')
    time.sleep(3)
    print('The room becomes quiet as you tell the mayor your task.')
    time.sleep(3)
    print('...')
    print('Well... In that case, please stay and let\'s discuss your task.')
    time.sleep(5)
    print('Everyone! As you just heard, this adventurer seeks to slay the dragon! Please allow us to speak in private.')
    time.sleep(5)
    print('...')
    print('As people begin to leave, the mayor escorts you to his private study.')
    time.sleep(5)
    print("""We really appreciate what you hope to accomplish. If there is anything you need, I am sure that we can 
        furnish it for you.""")
    time.sleep(4)
    print('...')
    print('What do you need?')
    options = ['Request a map', 'Request a weapon', 'Request armor', 'Request nothing']
    print_options(options)
    request = input(choice_prompt)
    if request == '0':
        time.sleep(3)
        print('...')
        print('A map? Sure. I shall have a ranger draw one for you. Anything else?')
        have_map = True
        options = ['Request a weapon', 'Request armor', 'Request nothing']
        print_options(options)
        request_map = input(choice_prompt)
        if request_map = '0':
            time.sleep(3)
            print('...')
            print('A weapon? Sure. I shall have the blacksmith bring you his finest sword. Anything else?')
            have_sword = True
            options = ['Request armor', 'Request nothing']


def tavern_options():
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
    print('What do you want to do now?')
    options = ['Stay in the tavern', 'Leave the tavern', 'Leave the game']
    print_options(options)
    leave = input(choice_prompt)
    if leave == '0':
        time.sleep(5)
        print('Well, this is getting us nowhere. Let\'s leave.')
    elif leave == '1':
        time.sleep(5)
        print('Alright, let\'s go.')
    else:
        end_game()
    print('Well, we got some useful information.')
    time.sleep(1)
    print('What is the plan now?')
    options = ['Go to the townhall', 'Listen to the townsfolk']
    print_options(options)
    tavern1 = input(choice_prompt)
    if tavern1 == '0':
        town_hall_options()
    elif tavern1 == '1':
        gossip_options()



def town_hall_options():
    print("You walk through the town until you see a large longhouse with a sign out front that reads:")
    time.sleep(1)
    print('Dragon business and inquiries only.')
    time.sleep(2)
    print('Well, this must be the right place')
    time.sleep(2)
    print('As you walk into the townhall, you hear a bunch of yelling.')
    time.sleep(3)
    print('Now people, I understand your concerns about the dragon but there is nothing that we can do')
    time.sleep(1)
    print('There aren\'t enough soldiers to fend off the dragon and protect our town.')
    print('...')
    time.sleep(1)
    print('YOU ARE A COWARD! YOU RISK THE LIVES OF ALL OF THE PEOPLE IN THIS TOWN BY NOT DEALING WITH IT!')
    print('...')
    time.sleep(3)
    print('Wow, tough crowd for the mayor, huh?')
    print('...')
    print('...')
    print('...')
    time.sleep(3)
    print('What? I\'m the narrator I can say what I want.')
    print('...')
    time.sleep(3)
    print('Fine. what do you want to do?')
    options = ['Go up to the mayor', 'Wait for the mob to leave']
    print_options(options)
    townhall = input(choice_prompt)



def gossip_options():
    print('As you listen, you hear that the mayor is offering a large reward for slaying the dragon. ')
    print('...')
    time.sleep(1)
    options = ['Go to the townhall', ' Go to the tavern']
    print_options(options)
    gossip = input(choice_prompt)
    if gossip == '0':
        town_hall_options()
    elif gossip == '1':
        tavern_options()



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
      tavern_options()


    elif selection == '1':
       town_hall_options()
    elif selection == '2':
        gossip_options()
