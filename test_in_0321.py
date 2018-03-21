alien_0 = {'color' : 'green', 'points':5}

alien_0['position'] = (0,10);
alien_0['speed'] = 'fast'
alien_0['speed_1'] = 'medium'
del alien_0['speed_1']
print(alien_0 ,"\n")

for key,value in alien_0.items():
	print("key is " + key.title() +", value is " , value , "\n")

for key in sorted(alien_0.keys()):
	print('key:' + key.title())

favorite_languages = {
    'Kai' : 'python',
    'Dennis' : 'c++',
    'Alex' : 'java',
    'Hao' : 'python'
}
print('\n')
for language in set(favorite_languages.values()):
	print(language)

prompt = "test while, input 'quit' to stop this.\n"
message = ""
while message != 'quit':
	message = input(prompt);
	print(message)
	
def describe_pets( animal_type,  animal_age,animal_name = 'unknown'):
	print('I am a ' + animal_type, ',my name is ',animal_name.title(), '. I am ', animal_age, 'years old.\n' )
	return 0 
describe_pets('dog', 5,'coco')
describe_pets(animal_type = 'cat', animal_age = '3')
