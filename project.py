# MadLibs

import random

story = input("Choose the story 1, 2 or 3. If you can't decide which story to choose, input 0 for a random story: ")


def template1():

    number = (input("Input a number: "))  # I Don't convert to integer cuz this number I will concatenate with strings
    timeMeasure = input("Measure of time: ")
    transportationMode = input("Input mode of transportation: ")
    adjective = input("Input adjective (feeling): ")
    adjective_2 = input("Input adjective again (feeling): ")
    noun = input("Input noun: ")
    color = input("Input a color: ")
    bodyPart = input("Input part of body: ")
    number_2 = input("Input a number again: ")
    noun_2 = input("Isnput a noun again: ")
    noun_3 = input("Input a noun again: ")
    bodyPart_2 = input("Input a part of body again: ")
    verb = input("Input a verb: ")
    noun_4 = input("Input a noun again: ")
    adjective_3 = input("Input adjective again (feeling): ")
    silly_word = input("Input a silly word: ")

    return f'''
    It was about {number} {timeMeasure} ago when I arrived at the hospital in a {transportationMode}.  The hospital is a/an {adjective} place, there are a lot of {adjective_2} {noun} here.  There are nurses here who have {color} {bodyPart}. If someone wants to come into my room I told them that they have to (verb) first. I’ve decorated my room with {number_2} {noun_2}. Today I talked to a doctor and they were wearing a {noun_3} on their {bodyPart_2}. I heard that all doctors {verb} {noun_4} every day for breakfast. The most {adjective_3} thing about being in the hospital is the {silly_word} {noun} ! 
         '''


def template2():

    persons_name = input("Input person name: ")
    noun = input("Input noun: ")
    adjective = input("Input adjective (feeling): ")
    adjective_2 = input("Input adjective again (feeling): ")
    verb_2 = input("Input na verb again: ")
    verb = input("Input verb (ending in ing): ")
    adverb = input("Input adverb (ending in ly: ")
    timeMeasure = input("Input measure of time: ")
    color = input("Input a color: ")
    animal = input("Input an animal: ")
    number = input("input number: ")
    silly_word = input("Input silly word: ")
    noun_2 = input("Input noun again: ")

    return f'''
    This weekend I am going camping with {persons_name}. I packed my lantern, sleeping bag, and {noun}. I am so {adjective} to {verb} in a tent. I am {adjective_2} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb_2}. I have heard that the {color} lake is great for {verb}. Then we will {adverb} hike through the forest for {number} {timeMeasure}. If I see a {color} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {number} {silly_word} stories and roast {noun_2} around the campfire!!
          '''


def template3():

    persons_name = input("Input person name: ")
    adjective = input("Input adjective (feeling): ")
    color = input("Input a color: ")
    animal = input("Input an animal: ")
    place = input("Input a place: ")
    adjective_2 = input("Input adjective again (feeling): ")
    magical_creature = input("Input magical creature (plural): ")
    adjective_3 = input("Input adjective again (feeling): ")
    magical_creature_2 = input("Input magical creature again (plural): ")
    room_in_a_house = input("Input room in a house: ")
    noun = input("Input noun: ")
    noun_2 = input("Input noun again: ")
    noun_3 = input("Input noun again (plural): ")
    adjective_4 = input("Input adjective again (feeling): ")
    noun_4 = input("Input noun again (plural): ")
    number = input("Input a number: ")
    timeMeasure = input("Input measure of time: ")
    verb = input("Input verb (ending in ing): ")
    adjective_5 = input("Input adjective again (feeling): ")
    noun_5 = input("Input noun again (plural): ")

    return f'''
    Dear {persons_name}, I am writing to you from a {adjective} castle in an enchanted forest. I found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjective_2} {magical_creature} and {adjective_3} {magical_creature_2} here! In the {room_in_a_house} there is a pool full of {noun}. I fall asleep each night on a {noun_2} of {noun_3} and dream of {adjective_4} {noun_4}. It feels as though I have lived here for {number} {timeMeasure}. I hope one day you can visit, although the only way to get here now is {verb} on a {adjective_5} {noun_5}!!
         '''


def choice (story):
    if story == '1':
        print(template1())
    elif story == '2':
        print(template2())
    elif story == '3':
        print(template3())

if story == '0':
    stories = ['1', '2', '3']
    rand = random.choice(stories)
    choice(rand)