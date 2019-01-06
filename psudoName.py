"""Creating a false name from a collection of strings"""
import random

"""Introduction of the sillyness"""
print ('We are sinceerly grateful that you have elected to download our "Silly Psudoname Selection System".')
print ('Everyone here on the team in Stonewick, Scotland, was loosing hope anybody would find this actualy.')
print ('It looks like a number of us owe Sammy around 5 pounds, anyways please use this as you see fit.')

"""List of the Silly"""
first_N = ('Action', 'Hannah', 'Leo', 'Amber', 'Carson', 'Malardy', 'Wyatt', 'Terry')

nick_N = ('"Corn Nut"', '"Sonny"', 'Rocket', 'Vulture', '"Buttercup"')

last_N = ('Aqua', 'Castle', 'Peters', 'Steps', 'Daybreak', 'Fourteen')

"""The thing that does something with the silly"""
while True:
	first_Name = random.choice(first_N)

	nick_Name = random.choice(nick_N)

	sur_Name = random.choice(last_N)

	print ("\n")
	print('{} {} {}'.format(first_Name, nick_Name, sur_Name))
	print ('\n')

	try_Again = input("Is this silly enough for you? If so press 'x' otherwise the enter key. \n")
	if try_Again.lower() == 'x':
		break

"""Stopping the silly"""
input('\nPress enter to exit.')
