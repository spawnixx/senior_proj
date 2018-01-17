# Senior Project game.py


import dialogue_paths
import time

print('Not DnD by Gabriel Thornburgh')
time.sleep(1)
print('Welcome to Definitely not Dungeons and Absolutely not Dragons: a Text-based Adventure Game.')
time.sleep(3)

choice_prompt = 'Enter your choice: '


def print_options(option_list):
    for i in range(len(option_list)):
        print('{0}) {1}'.format(i, option_list[i]))


class MyHero:
    alive = True
    if alive:

        print('Well, I am the narrator so I suppose I should know who you are.')
        character = (input('Who are you? '))
        print('Oh, hi %s!' % character)
        time.sleep(2)
        print('''Your adventure begins as you approach the town Heimndal,
        a small town in the kingdom of Eastmane.
        You have heard rumors that a dragon resides near the town''')
        time.sleep(3)
        print('When you reach the outskirts of the town, you are met by a knight atop his horse.')
        time.sleep(4)
        print('Well, don\'t just sit there')
        print('...')
        options = ['Go up to him.', 'Do nothing.']
        print_options(options)
        talk1 = None
        while talk1 not in ['0','1']:
            talk1 = input(choice_prompt)
    dialogue_paths.knight_convo(talk1)
    print('Well, now you are inside the town.')
    time.sleep(1)
    print('What do you want to do?')
    options = ['Go to the tavern', 'Go to the townhall', 'Listen to the townsfolk talk']
    print_options(options)
    explore = None
    while explore not in ['0', '1', '2']:
        explore = input(choice_prompt)
    dialogue_paths.village(explore)


