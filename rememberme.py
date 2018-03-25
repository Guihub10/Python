import json
def greet_user():
	"""Greet user and point out his or her name."""
	filename = "username.json"
	try:
		with open(filename) as file_object:
			username = json.load(file_object)
	except FileNotFoundError:# If you don't want to do anything about this error, you can use 'pass' here.
		username = input("What is your name? ")
		with open(filename,'w') as file_object:
			json.dump(username,file_object)
			print("We will remember you when you come back, " + username +"! ")
	else:
		print("Welcome back, " + username + "! ")

greet_user()
