import random

class Character:
    def action(self,verb,Character):
        if verb == 'look':
            if Character.size == 3:
                print 'You are extremely tall!'
            elif Character.size == 2:
                print 'You are your regular, gorgeous self.'
            elif Character.size == 1:
                print 'You are verrrry small.'
            else:
                print 'You are not sure what to make of yourself.'
        else:
            print 'You can\'t %s yourself.' % (verb)

class Mushroom:
    def action(self,verb,Character):
        if verb == 'look':
            print 'One side makes you taller, the other side makes you smaller. Unfortunately, it\'s hard to define "sides" when something is a circle.'
        elif verb == 'eat':
            grow = random.randrange(2)
            if grow == 1:
                if Character.size == 3:
                    print 'Your bones tingle but you don\'t change size.'
                elif Character.size <= 2:
                    Character.size += 1
                    print 'Your knees quake as you suddenly sprout! You are taller.'
            else:
                if Character.size == 1:
                    print 'Your bones tingle but you don\'t change size.'
                elif Character.size >= 2:
                    Character.size -= 1
                    print 'You find yourself quickly shrinking! You are smaller.'
        elif verb == 'love':
            print 'You love the mushroom, but it will never love you back.'
        else:
            print 'You can\'t %s a mushroom.' % (verb)


mushroom = Mushroom()
ME = Character()
ME.size = 2

objectDictionary = {'mushroom': mushroom, 'me': ME}
characterList = {'me': ME}
verbList = {'look','love','eat'} # {TO-DO: For my reference. Make attempting one-word commands print messages specific to the verb, like with 'exit'.}

def executePlayerCommand(verb,character,thing):
    if thing in objectDictionary and character in characterList:
        objectDictionary[thing].action(verb,characterList[character])
        playerAction()
    elif thing not in objectDictionary:
        print 'You don\'t see %s here.' % (thing)
        playerAction()
    elif character not in characterList:
        print 'You don\'t see %s here.' % (character)
        playerAction()
    else:
        print 'You don\'t see %s or %s here.' % (thing,character)
        playerAction()


def playerAction():
    print 'You are %s sizes tall.' % ME.size #Debugging line.
    print 'What would you like to do?'
    playerCommand = raw_input()
    playerCommandWords = playerCommand.split(' ')
    if len(playerCommandWords) <= 1:
        verb = playerCommandWords[0]
        if verb == 'exit':
            print 'Thanks for playing!' # {TO-DO: Prompt user before exiting game.}
        else:
            print 'You can\'t %s.' % (verb)
            playerAction()
    elif len(playerCommandWords) == 2:
        verb, thing = playerCommandWords
        character = 'me'
        executePlayerCommand(verb,character,thing)
    elif len(playerCommandWords) == 3:
        verb, character, thing = playerCommandWords
        executePlayerCommand(verb,character,thing)
    elif len(playerCommandWords) >= 4:
        print 'You don\'t know how to %s.' % (playerCommand)
        playerAction()
    else:
        print 'Sorry, I don\'t understand what that means.'
        playerAction()

playerAction()
