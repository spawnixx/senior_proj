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
    
    
    def armory_options():
    actions = {'1': 'leave', '2': 'investigate', '3':'quit'}
    results = {'leave': 'you exit the location', 'investigate':'you see a bright shiny ball', 'quit':'thank you for playing'}
    print 'You are currently in the armory...'
    selection = decide(actions)

    return results.get(actions.get(selection), 'invalid input')

def tavern_options():
    actions = {'1': 'leave', '2': 'investigate', '3':'quit'}
    results = {'leave': 'you exit the location', 'investigate':'you see a bright shiny ball', 'quit':'thank you for playing'}
    print 'You are currently in the tavern...'
    selection = decide(actions)

    return results.get(actions.get(selection), 'invalid input')

def fortress_options():
    actions = {'1': 'leave', '2': 'investigate', '3': 'go to', '4':'quit'}
    results = {'leave': 'you exit the location', 'investigate': investigate,
               'quit':'thank you for playing', 'go to': goto}
    observations = {'people':['a Squire','a Servant'],
                    'things':['bags of food', 'bales of hay', 'piles of rubbish'],
                    'destinations':['Tower Keep', 'Armory', 'Kitchen', 'Exit']}

    print 'You are currently in the fortress...'
    selection = decide(actions)
    result = results.get(actions.get(selection), 'invalid input')
    if callable(result):
        if result.func_name == 'investigate':
            return result(observations)
        else:
            return result()
    else:
        return results.get(actions.get(selection), 'invalid input')

def goto(myHero, location=None, location_options=None):
    if not location:
        options = {}
        for i in xrange(len(location_options)):
            options[str(i)]= location_options[i].lower()
        selection = decide(options)
        location = options.get(selection)


    func = GLOBAL_LOCATIONS.get(location,'nothing')
    if not callable(func):
        print 'Not a valid destination'
    myHero.location = location
    return func()

def investigate(observations):
    if observations['people']:
        print 'You see several people milling about as well as {0}'.format(' and '.join(observations['people']))
    else:
        print 'You see no one of interest.'
    if observations['things']:
        print 'There are {0} scattered around.'.format(' and '.join(observations['things']))
    if observations['destinations']:
        print 'These places are accessible:\n{0}'.format('\n'.join(observations['destinations']))
    print '...'
    actions = {'1':'speak to someone','2': 'go to', '3': 'quit'}

    selection = decide(actions)
    if selection == '2':
        return goto(location_options=observations['destinations'])
    return actions.get(selection,'nothing')

def decide(options):
    print 'What is your pleasure?...'
    keys = options.keys()
    keys.sort()
    for k in keys:
        print '{0}) {1}'.format(k, options[k])
    selection = raw_input('Enter your choice:')
    return selection




GLOBAL_LOCATIONS = {'fortress': fortress_options,
         'tavern': tavern_options,
         'armory': armory_options}



