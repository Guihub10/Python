filename = 'test_file.txt'
path = '/home/shihao/workspace/python_work/'
with open(path + filename) as file_object:
	for line in file_object:
		print(line)
	for line in file_object:
		print(line.rstrip())

	lines = file_object.readlines()
	for line in lines:
		print(line.rstrip())

filename = 'programming.txt'
with open (filename,'w') as file_object:
	file_object.write("I love programming! It is 'w' mode, everytime you called it, old centexts will be lost")

with open (filename,'a') as file_object:
	file_object.write("It is 'a' mode, old contexts won't be deleted!")


def get_formatted_name(first, last):
	full_name = first + ' ' + last
	return full_name.title()
	
	
